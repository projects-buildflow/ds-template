"""Tests for Task 2.4: Code Review Guidelines

Objective: Create a comprehensive code review checklist for data cleaning pipelines.

This test DECISIVELY verifies:
1. Checklist file exists at the correct path
2. Checklist has substantial content (not a placeholder)
3. Checklist covers data correctness
4. Checklist covers error handling
5. Checklist covers code readability
6. Checklist covers performance
7. Checklist covers testing
8. Checklist has actionable checkbox items (at least 15)
9. Checklist includes examples or specific scenarios
"""

import pytest
import re
from pathlib import Path


@pytest.fixture
def checklist_path(student_folder):
    """Get path to the code review checklist file."""
    if not student_folder:
        pytest.skip("Student folder not provided")
    return Path(student_folder) / "week-2" / "code_review_checklist.md"


@pytest.fixture
def checklist_content(checklist_path):
    """Load checklist content."""
    if not checklist_path.exists():
        pytest.fail(
            f"Checklist not found at {checklist_path}\n\n"
            "Create: cohort/{your-github-username}/week-2/code_review_checklist.md"
        )
    return checklist_path.read_text()


class TestChecklistExists:
    """Verify the checklist file exists and has content."""

    def test_checklist_file_exists(self, checklist_path):
        """Checklist file must exist at the correct path."""
        assert checklist_path.exists(), (
            f"Checklist not found at {checklist_path}\n\n"
            "Create: cohort/{your-github-username}/week-2/code_review_checklist.md"
        )

    def test_checklist_has_substantial_content(self, checklist_content):
        """Checklist must have substantial content - not a placeholder."""
        char_count = len(checklist_content)
        word_count = len(checklist_content.split())

        assert char_count >= 500, (
            f"Checklist is too short ({char_count} characters).\n"
            "Expected a comprehensive checklist with multiple sections and items."
        )

        assert word_count >= 200, (
            f"Checklist has only {word_count} words.\n"
            "A useful code review checklist needs more detail."
        )

    def test_checklist_is_markdown(self, checklist_content):
        """Checklist should be properly formatted markdown."""
        has_headers = '#' in checklist_content

        assert has_headers, (
            "Checklist should use markdown headers (# or ##) to organize sections."
        )


class TestRequiredSections:
    """Verify checklist has all required topic areas."""

    def test_has_correctness_section(self, checklist_content):
        """Checklist must cover data correctness."""
        content_lower = checklist_content.lower()

        correctness_keywords = [
            'correct', 'accurate', 'valid', 'output', 'result',
            'expected', 'input', 'data quality'
        ]
        found_correctness = sum(1 for kw in correctness_keywords if kw in content_lower)

        assert found_correctness >= 2, (
            "Missing section on data correctness.\n"
            "Add: ## Data Correctness\n"
            "Cover: input validation, output verification, data integrity"
        )

    def test_has_error_handling_section(self, checklist_content):
        """Checklist must cover error handling."""
        content_lower = checklist_content.lower()

        error_keywords = [
            'error', 'exception', 'edge case', 'handle', 'fail',
            'catch', 'try', 'null', 'missing', 'invalid'
        ]
        found_errors = sum(1 for kw in error_keywords if kw in content_lower)

        assert found_errors >= 2, (
            "Missing section on error handling.\n"
            "Add: ## Error Handling\n"
            "Cover: exception handling, edge cases, null values"
        )

    def test_has_readability_section(self, checklist_content):
        """Checklist must cover code readability."""
        content_lower = checklist_content.lower()

        readability_keywords = [
            'readable', 'readability', 'naming', 'comment', 'docstring',
            'documentation', 'style', 'clear', 'understandable', 'maintain'
        ]
        found_readability = sum(1 for kw in readability_keywords if kw in content_lower)

        assert found_readability >= 2, (
            "Missing section on code readability.\n"
            "Add: ## Code Readability\n"
            "Cover: naming conventions, comments, documentation"
        )

    def test_has_performance_section(self, checklist_content):
        """Checklist must cover performance."""
        content_lower = checklist_content.lower()

        performance_keywords = [
            'perform', 'efficien', 'optim', 'memory', 'speed',
            'scalab', 'large', 'batch', 'chunk'
        ]
        found_performance = sum(1 for kw in performance_keywords if kw in content_lower)

        assert found_performance >= 1, (
            "Missing section on performance.\n"
            "Add: ## Performance\n"
            "Cover: efficiency, memory usage, scalability"
        )

    def test_has_testing_section(self, checklist_content):
        """Checklist must cover testing."""
        content_lower = checklist_content.lower()

        testing_keywords = [
            'test', 'unit', 'assert', 'verify', 'check',
            'coverage', 'mock', 'fixture'
        ]
        found_testing = sum(1 for kw in testing_keywords if kw in content_lower)

        assert found_testing >= 2, (
            "Missing section on testing.\n"
            "Add: ## Testing\n"
            "Cover: unit tests, test coverage, test data"
        )


class TestChecklistItems:
    """Verify checklist has actionable items."""

    def test_has_checkbox_items(self, checklist_content):
        """Checklist must have checkbox items (at least 15)."""
        # Count checkbox patterns: - [ ] or * [ ] or - [x]
        checkbox_pattern = r'[-*]\s*\[\s*[xX\s]?\s*\]'
        checkboxes = re.findall(checkbox_pattern, checklist_content)

        assert len(checkboxes) >= 15, (
            f"Found only {len(checkboxes)} checklist items.\n"
            "A comprehensive code review checklist needs at least 15 items.\n\n"
            "Format items like:\n"
            "- [ ] Are variable names descriptive?\n"
            "- [ ] Is error handling present for edge cases?"
        )

    def test_items_are_actionable(self, checklist_content):
        """Checklist items should be actionable questions or statements."""
        content_lower = checklist_content.lower()

        # Should contain question words or action words
        action_indicators = [
            '?', 'is ', 'are ', 'does ', 'do ', 'has ', 'have ',
            'check ', 'verify ', 'ensure ', 'confirm ', 'review '
        ]
        found_actions = sum(content_lower.count(ind) for ind in action_indicators)

        assert found_actions >= 10, (
            "Checklist items should be actionable.\n"
            "Phrase items as questions: 'Is X done?' or 'Are there Y?'\n"
            "Or as verifications: 'Check that X', 'Verify Y'"
        )

    def test_items_are_specific_to_data(self, checklist_content):
        """Checklist items should be specific to data cleaning."""
        content_lower = checklist_content.lower()

        data_terms = [
            'dataframe', 'df', 'column', 'row', 'null', 'nan',
            'duplicate', 'missing', 'pandas', 'data', 'csv',
            'clean', 'valid', 'invalid', 'age', 'email'
        ]
        found_data_terms = sum(1 for term in data_terms if term in content_lower)

        assert found_data_terms >= 5, (
            f"Found only {found_data_terms} data-related terms.\n"
            "Checklist items should be specific to data cleaning pipelines.\n"
            "Include items about: DataFrames, null values, duplicates, data types, etc."
        )


class TestCommonIssues:
    """Verify checklist documents common issues."""

    def test_has_common_issues_section(self, checklist_content):
        """Checklist should document common issues to watch for."""
        content_lower = checklist_content.lower()

        issues_indicators = [
            'common issue', 'common mistake', 'watch for', 'pitfall',
            'gotcha', 'frequent', 'often', 'typical error', 'warning'
        ]
        found_issues = any(ind in content_lower for ind in issues_indicators)

        assert found_issues, (
            "Missing 'Common Issues' section.\n"
            "Add: ## Common Issues / Pitfalls\n"
            "Document 3+ common mistakes reviewers should watch for."
        )

    def test_mentions_null_handling(self, checklist_content):
        """Checklist should mention null/missing value handling."""
        content_lower = checklist_content.lower()

        null_terms = ['null', 'nan', 'none', 'missing', 'empty', 'na']
        has_null_handling = any(term in content_lower for term in null_terms)

        assert has_null_handling, (
            "Checklist should mention handling of null/missing values.\n"
            "This is a critical data quality issue."
        )

    def test_mentions_duplicates(self, checklist_content):
        """Checklist should mention duplicate handling."""
        content_lower = checklist_content.lower()

        assert 'duplicate' in content_lower, (
            "Checklist should mention duplicate detection/handling.\n"
            "Duplicates are a common data quality issue."
        )


class TestChecklistQuality:
    """Additional quality checks for the checklist."""

    def test_has_examples(self, checklist_content):
        """Checklist should include examples or specific scenarios."""
        content_lower = checklist_content.lower()

        example_indicators = [
            'example', 'e.g.', 'for instance', 'such as',
            '```',  # Code blocks
            'scenario', 'case'
        ]
        has_examples = any(ind in content_lower or ind in checklist_content for ind in example_indicators)

        assert has_examples, (
            "Checklist should include examples.\n"
            "Add code snippets or specific scenarios to illustrate issues."
        )

    def test_organized_structure(self, checklist_content):
        """Checklist should have organized structure with sections."""
        # Count section headers
        section_pattern = r'^#{1,3}\s+\w+'
        sections = re.findall(section_pattern, checklist_content, re.MULTILINE)

        assert len(sections) >= 4, (
            f"Found only {len(sections)} section headers.\n"
            "Organize checklist into sections:\n"
            "- Data Correctness\n"
            "- Error Handling\n"
            "- Code Quality\n"
            "- Performance\n"
            "- Testing"
        )

    def test_reasonable_detail(self, checklist_content):
        """Each section should have reasonable detail."""
        # Split by headers and check each section
        sections = re.split(r'^#{1,3}\s+', checklist_content, flags=re.MULTILINE)

        # At least some sections should have meaningful content
        substantial_sections = [s for s in sections if len(s.split()) > 20]

        assert len(substantial_sections) >= 3, (
            "Checklist sections are too brief.\n"
            "Each section should have at least 3-4 checklist items with explanations."
        )

    def test_professional_formatting(self, checklist_content):
        """Checklist should have professional formatting."""
        # Check for consistent checkbox format
        has_checkboxes = '[ ]' in checklist_content or '[x]' in checklist_content.lower()

        # Check for proper markdown headers
        has_proper_headers = bool(re.search(r'^#{1,3}\s+[A-Z]', checklist_content, re.MULTILINE))

        assert has_checkboxes and has_proper_headers, (
            "Checklist should use professional formatting:\n"
            "- Use markdown headers (## Section Name)\n"
            "- Use checkbox format (- [ ] Item)"
        )


class TestDataPipelineSpecific:
    """Verify checklist covers data pipeline-specific concerns."""

    def test_covers_data_types(self, checklist_content):
        """Checklist should mention data type validation."""
        content_lower = checklist_content.lower()

        type_terms = ['dtype', 'data type', 'type', 'int', 'str', 'float', 'datetime', 'cast', 'convert']
        found_types = sum(1 for term in type_terms if term in content_lower)

        assert found_types >= 1, (
            "Checklist should mention data type validation.\n"
            "Add items about: correct data types, type conversion, type checking"
        )

    def test_covers_data_transformations(self, checklist_content):
        """Checklist should mention data transformation validation."""
        content_lower = checklist_content.lower()

        transform_terms = [
            'transform', 'filter', 'aggregate', 'join', 'merge',
            'map', 'apply', 'group', 'sort'
        ]
        found_transforms = sum(1 for term in transform_terms if term in content_lower)

        assert found_transforms >= 1, (
            "Checklist should cover data transformations.\n"
            "Add items about: filter logic, aggregation correctness, join integrity"
        )

    def test_covers_logging(self, checklist_content):
        """Checklist should mention logging/monitoring."""
        content_lower = checklist_content.lower()

        logging_terms = ['log', 'monitor', 'debug', 'print', 'trace', 'audit']
        has_logging = any(term in content_lower for term in logging_terms)

        assert has_logging, (
            "Checklist should mention logging.\n"
            "Add items about: logging important steps, debugging output, audit trail"
        )
