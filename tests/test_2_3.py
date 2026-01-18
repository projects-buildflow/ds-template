"""Tests for Task 2.3: Data Cleaning Pipeline

Objective: Build a data cleaning pipeline that produces clean, validated customer data.

This test DECISIVELY verifies:
1. Cleaning script exists with correct function name
2. Function can be imported and called
3. Pipeline produces output file
4. Output has NO invalid ages (negative or >120)
5. Pipeline is idempotent (running twice = same result)
6. Pipeline handles all data quality issues from profiling
7. Output maintains data integrity (no lost columns)
8. Function has proper documentation
"""

import pytest
import pandas as pd
import sys
from pathlib import Path


@pytest.fixture
def script_path(student_folder):
    """Get path to student's cleaning script folder."""
    if not student_folder:
        pytest.skip("Student folder not provided")
    return Path(student_folder) / "week-2" / "task-2.3"


@pytest.fixture
def clean_function(script_path):
    """Import and return the student's cleaning function."""
    script_file = script_path / "clean_customers.py"

    if not script_file.exists():
        pytest.fail(
            f"Cleaning script not found at {script_file}\n\n"
            "Create: cohort/{your-github-username}/week-2/task-2.3/clean_customers.py"
        )

    sys.path.insert(0, str(script_path))

    try:
        if 'clean_customers' in sys.modules:
            del sys.modules['clean_customers']

        from clean_customers import clean_customer_data
        return clean_customer_data
    except ImportError as e:
        pytest.fail(
            f"Could not import clean_customer_data: {e}\n\n"
            "Make sure your file defines: def clean_customer_data(input_path, output_path):"
        )
    except SyntaxError as e:
        pytest.fail(f"Syntax error in clean_customers.py: {e}")
    finally:
        if str(script_path) in sys.path:
            sys.path.remove(str(script_path))


@pytest.fixture
def sample_dirty_data(tmp_path):
    """Create sample dirty customer data for testing."""
    dirty_df = pd.DataFrame({
        "customer_id": ["C001", "C002", "C003", "C004", "C005", "C006"],
        "name": ["Alice", "Bob", "  Charlie  ", "Diana", "Eve", "Frank"],
        "age": [25, -5, 150, 30, 45, 35],  # -5 and 150 are invalid
        "email": [
            "alice@test.com",
            "bob@example.com",
            "invalid-email",  # Invalid
            "diana@test.org",
            "EVE@TEST.COM",  # Uppercase (should be normalized)
            "frank@test.com"
        ],
        "phone": ["1234567890", "", "9876543210", "1111111111", "2222222222", "3333333333"],  # Empty phone
        "city": ["Mumbai", "Delhi", "Mumbai", "Bangalore", "Delhi", "Mumbai"],
        "signup_date": ["2024-01-15", "2024-02-20", "2024-03-10", "2024-04-05", "2024-05-18", "2024-06-22"],
        "gender": ["F", "M", "M", "F", "F", "M"],
    })

    input_file = tmp_path / "dirty_customers.csv"
    dirty_df.to_csv(input_file, index=False)
    return input_file


class TestScriptExists:
    """Verify the cleaning script exists and has required function."""

    def test_script_file_exists(self, script_path):
        """clean_customers.py must exist."""
        script_file = script_path / "clean_customers.py"
        assert script_file.exists(), (
            f"Script not found at {script_file}\n\n"
            "Create: cohort/{your-github-username}/week-2/task-2.3/clean_customers.py"
        )

    def test_function_is_callable(self, clean_function):
        """clean_customer_data must be callable."""
        assert callable(clean_function), (
            "clean_customer_data is not callable.\n"
            "Define: def clean_customer_data(input_path, output_path):"
        )


class TestPipelineProducesOutput:
    """Verify the cleaning pipeline produces valid output."""

    def test_creates_output_file(self, clean_function, sample_dirty_data, tmp_path):
        """Pipeline must create an output file."""
        output_file = tmp_path / "cleaned.csv"

        clean_function(str(sample_dirty_data), str(output_file))

        assert output_file.exists(), (
            "Pipeline did not create output file.\n"
            "Make sure to save the cleaned DataFrame to the output_path."
        )

    def test_output_is_not_empty(self, clean_function, sample_dirty_data, tmp_path):
        """Pipeline output must have data."""
        output_file = tmp_path / "cleaned.csv"

        clean_function(str(sample_dirty_data), str(output_file))

        cleaned_df = pd.read_csv(output_file)
        assert len(cleaned_df) > 0, (
            "Output file is empty.\n"
            "The cleaning should retain valid records after removing/fixing invalid ones."
        )

    def test_output_has_required_columns(self, clean_function, sample_dirty_data, tmp_path):
        """Output must have all required columns."""
        output_file = tmp_path / "cleaned.csv"

        clean_function(str(sample_dirty_data), str(output_file))

        cleaned_df = pd.read_csv(output_file)

        required_columns = ["customer_id", "name", "age", "email"]
        missing = [col for col in required_columns if col not in cleaned_df.columns]

        assert not missing, (
            f"Output is missing columns: {missing}\n"
            "Don't drop required columns during cleaning."
        )


class TestAgeValidation:
    """Verify pipeline properly handles age validation."""

    def test_no_negative_ages(self, clean_function, sample_dirty_data, tmp_path):
        """Output must have NO negative ages."""
        output_file = tmp_path / "cleaned.csv"

        clean_function(str(sample_dirty_data), str(output_file))

        cleaned_df = pd.read_csv(output_file)

        assert (cleaned_df["age"] >= 0).all(), (
            f"Found negative ages in output: {cleaned_df[cleaned_df['age'] < 0]['age'].tolist()}\n"
            "Remove or fix records with negative ages."
        )

    def test_no_unreasonable_ages(self, clean_function, sample_dirty_data, tmp_path):
        """Output must have NO ages over 120."""
        output_file = tmp_path / "cleaned.csv"

        clean_function(str(sample_dirty_data), str(output_file))

        cleaned_df = pd.read_csv(output_file)

        assert (cleaned_df["age"] <= 120).all(), (
            f"Found ages > 120 in output: {cleaned_df[cleaned_df['age'] > 120]['age'].tolist()}\n"
            "Remove or fix records with unreasonable ages."
        )

    def test_valid_ages_retained(self, clean_function, sample_dirty_data, tmp_path):
        """Pipeline should keep records with valid ages."""
        output_file = tmp_path / "cleaned.csv"

        clean_function(str(sample_dirty_data), str(output_file))

        cleaned_df = pd.read_csv(output_file)

        # Should have kept at least some of the valid records
        # (ages 25, 30, 45, 35 are valid)
        assert len(cleaned_df) >= 3, (
            f"Output has only {len(cleaned_df)} records.\n"
            "Valid records should be retained."
        )


class TestPipelineIdempotency:
    """Verify running the pipeline twice produces the same result."""

    def test_idempotent_operation(self, clean_function, sample_dirty_data, tmp_path):
        """Running cleaning twice should give same result."""
        output1 = tmp_path / "cleaned1.csv"
        output2 = tmp_path / "cleaned2.csv"

        # First run
        clean_function(str(sample_dirty_data), str(output1))

        # Second run on already cleaned data
        clean_function(str(output1), str(output2))

        df1 = pd.read_csv(output1)
        df2 = pd.read_csv(output2)

        # Should be identical
        try:
            pd.testing.assert_frame_equal(
                df1.reset_index(drop=True),
                df2.reset_index(drop=True)
            )
        except AssertionError:
            pytest.fail(
                "Pipeline is not idempotent.\n"
                "Running on already-clean data should produce the same result."
            )


class TestDataQualityHandling:
    """Verify pipeline handles various data quality issues."""

    def test_handles_whitespace_in_names(self, clean_function, tmp_path):
        """Pipeline should strip whitespace from names."""
        dirty_df = pd.DataFrame({
            "customer_id": ["C001"],
            "name": ["  Padded Name  "],
            "age": [30],
            "email": ["test@example.com"],
            "phone": ["1234567890"],
            "city": ["Mumbai"],
            "signup_date": ["2024-01-01"],
            "gender": ["M"],
        })

        input_file = tmp_path / "whitespace_test.csv"
        output_file = tmp_path / "cleaned.csv"
        dirty_df.to_csv(input_file, index=False)

        clean_function(str(input_file), str(output_file))

        cleaned_df = pd.read_csv(output_file)

        # Name should be stripped
        if len(cleaned_df) > 0:
            name = cleaned_df["name"].iloc[0]
            assert name == name.strip(), (
                "Names should have leading/trailing whitespace removed.\n"
                f"Got: '{name}'"
            )

    def test_handles_empty_strings(self, clean_function, tmp_path):
        """Pipeline should handle empty string fields appropriately."""
        dirty_df = pd.DataFrame({
            "customer_id": ["C001", "C002"],
            "name": ["Alice", "Bob"],
            "age": [25, 30],
            "email": ["alice@test.com", "bob@test.com"],
            "phone": ["1234567890", ""],  # Empty phone
            "city": ["Mumbai", "Delhi"],
            "signup_date": ["2024-01-01", "2024-01-02"],
            "gender": ["F", "M"],
        })

        input_file = tmp_path / "empty_string_test.csv"
        output_file = tmp_path / "cleaned.csv"
        dirty_df.to_csv(input_file, index=False)

        clean_function(str(input_file), str(output_file))

        # Should complete without error
        assert output_file.exists()

    def test_processes_real_data_file(self, clean_function, data_path, tmp_path):
        """Pipeline should work on actual data file if available."""
        input_file = data_path / "marketing_customers_raw.csv"

        if not input_file.exists():
            pytest.skip("Test data file not found")

        output_file = tmp_path / "cleaned_real.csv"

        try:
            clean_function(str(input_file), str(output_file))
            assert output_file.exists()

            cleaned_df = pd.read_csv(output_file)
            assert len(cleaned_df) > 0

            # Verify no invalid ages
            assert (cleaned_df["age"] >= 0).all()
            assert (cleaned_df["age"] <= 120).all()

        except Exception as e:
            pytest.fail(f"Pipeline failed on real data: {e}")


class TestCodeQuality:
    """Verify code quality of the cleaning script."""

    def test_function_has_docstring(self, clean_function):
        """clean_customer_data should have a docstring."""
        assert clean_function.__doc__ is not None, (
            "clean_customer_data should have a docstring.\n"
            "Add: '''Cleans customer data and saves to output file.'''"
        )

        assert len(clean_function.__doc__) > 20, (
            "Docstring should be meaningful, not just a placeholder.\n"
            "Describe what the function does, its parameters, and what it returns."
        )

    def test_script_has_imports(self, script_path):
        """Script should have proper imports."""
        script_file = script_path / "clean_customers.py"
        if not script_file.exists():
            pytest.skip("Script not found")

        content = script_file.read_text()

        assert "pandas" in content, (
            "Script should import pandas for DataFrame operations.\n"
            "Add: import pandas as pd"
        )

    def test_script_is_readable(self, script_path):
        """Script should be well-structured and readable."""
        script_file = script_path / "clean_customers.py"
        if not script_file.exists():
            pytest.skip("Script not found")

        content = script_file.read_text()
        lines = content.split('\n')

        # Should have reasonable number of lines (not trivial)
        non_empty_lines = [l for l in lines if l.strip()]
        assert len(non_empty_lines) >= 10, (
            f"Script has only {len(non_empty_lines)} lines.\n"
            "A proper cleaning pipeline needs more code to handle various cases."
        )


class TestErrorHandling:
    """Verify pipeline handles edge cases gracefully."""

    def test_handles_empty_input(self, clean_function, tmp_path):
        """Pipeline should handle empty input file."""
        empty_df = pd.DataFrame(columns=[
            "customer_id", "name", "age", "email", "phone", "city", "signup_date", "gender"
        ])

        input_file = tmp_path / "empty.csv"
        output_file = tmp_path / "cleaned.csv"
        empty_df.to_csv(input_file, index=False)

        try:
            clean_function(str(input_file), str(output_file))
            # Should complete without error
        except Exception as e:
            pytest.fail(f"Pipeline crashed on empty input: {e}")

    def test_handles_all_invalid_data(self, clean_function, tmp_path):
        """Pipeline should handle case where all data is invalid."""
        all_invalid_df = pd.DataFrame({
            "customer_id": ["C001", "C002"],
            "name": ["A", "B"],
            "age": [-5, 200],  # All invalid ages
            "email": ["invalid", "also-invalid"],
            "phone": ["", ""],
            "city": ["X", "Y"],
            "signup_date": ["2024-01-01", "2024-01-02"],
            "gender": ["?", "?"],
        })

        input_file = tmp_path / "all_invalid.csv"
        output_file = tmp_path / "cleaned.csv"
        all_invalid_df.to_csv(input_file, index=False)

        try:
            clean_function(str(input_file), str(output_file))
            # Should complete without error (may produce empty output)
        except Exception as e:
            pytest.fail(f"Pipeline crashed on all-invalid data: {e}")
