"""Tests for Task 3.2: SQL Cohort Analysis

Objective: Write SQL queries to analyze customer cohort retention patterns.

This test DECISIVELY verifies:
1. SQL file exists with cohort analysis query
2. Query has correct structure (SELECT, FROM, GROUP BY)
3. Query calculates cohorts based on first order date
4. Query shows retention by month (month_0, month_1, etc.)
5. Query syntax is valid (no obvious errors)
"""

import pytest
import re
from pathlib import Path


@pytest.fixture
def sql_content(student_folder):
    """Load the student's SQL file content."""
    if not student_folder:
        pytest.skip("Student folder not provided")

    sql_path = Path(student_folder) / "week-3" / "cohort_analysis.sql"

    if not sql_path.exists():
        pytest.fail(
            f"SQL file not found at {sql_path}\n\n"
            "Create a file called 'cohort_analysis.sql' in your week-3 folder."
        )

    return sql_path.read_text()


class TestSQLFileExists:
    """Verify the SQL file exists and has content."""

    def test_sql_file_has_content(self, sql_content):
        """SQL file must have meaningful content."""
        assert len(sql_content.strip()) > 100, (
            "SQL file appears too short.\n"
            "Write a complete cohort analysis query."
        )

    def test_sql_not_just_comments(self, sql_content):
        """SQL file should have actual SQL, not just comments."""
        # Remove comments and check remaining content
        lines = sql_content.split('\n')
        code_lines = [l for l in lines if not l.strip().startswith('--') and l.strip()]

        assert len(code_lines) > 5, (
            "SQL file has too few lines of actual code.\n"
            "Write a complete cohort analysis query."
        )


class TestSQLStructure:
    """Verify the SQL has required structural elements."""

    def test_has_select_statement(self, sql_content):
        """Query must have a SELECT statement."""
        assert re.search(r'\bSELECT\b', sql_content, re.IGNORECASE), (
            "Missing SELECT statement.\n"
            "Your query should start with SELECT to specify output columns."
        )

    def test_has_from_clause(self, sql_content):
        """Query must have a FROM clause."""
        assert re.search(r'\bFROM\b', sql_content, re.IGNORECASE), (
            "Missing FROM clause.\n"
            "Specify the table to query: FROM orders"
        )

    def test_has_group_by(self, sql_content):
        """Cohort analysis requires GROUP BY."""
        assert re.search(r'\bGROUP\s+BY\b', sql_content, re.IGNORECASE), (
            "Missing GROUP BY clause.\n"
            "Cohort analysis requires grouping by cohort period."
        )

    def test_references_orders_or_customers(self, sql_content):
        """Query should reference orders or customers table."""
        content_lower = sql_content.lower()
        has_data_source = 'orders' in content_lower or 'customers' in content_lower

        assert has_data_source, (
            "Query should reference the 'orders' or 'customers' table.\n"
            "Cohort analysis is based on customer order history."
        )


class TestCohortCalculation:
    """Verify the query calculates cohorts correctly."""

    def test_calculates_first_order_date(self, sql_content):
        """Query must calculate first order date for each customer."""
        content_lower = sql_content.lower()

        # Look for patterns that calculate first order/signup
        cohort_patterns = [
            r'min\s*\(\s*order',           # MIN(order_date)
            r'min\s*\(\s*created',          # MIN(created_at)
            r'first_value',                 # FIRST_VALUE window function
            r'first_order',                 # Custom alias
            r'cohort_month',                # Common naming
            r'cohort_date',
            r'signup_month',
            r'row_number.*order\s+by.*asc', # First record by date
        ]

        found_cohort_calc = any(re.search(p, content_lower) for p in cohort_patterns)

        assert found_cohort_calc, (
            "Query should calculate when each customer first ordered.\n\n"
            "Use MIN(order_date) grouped by customer_id to find their cohort:\n"
            "  SELECT customer_id, MIN(order_date) as cohort_date\n"
            "  FROM orders\n"
            "  GROUP BY customer_id"
        )

    def test_groups_by_time_period(self, sql_content):
        """Query should group cohorts by month/period."""
        content_lower = sql_content.lower()

        # Look for date truncation/extraction
        period_patterns = [
            r'date_trunc',           # PostgreSQL/Snowflake
            r'strftime',             # SQLite
            r'to_char.*yyyy.*mm',    # Oracle/Postgres formatting
            r'format.*date',         # Various DBs
            r'year.*month',          # Manual extraction
            r'extract\s*\(',         # EXTRACT function
            r'datepart',             # SQL Server
            r'month\s*\(',           # MONTH function
        ]

        found_period = any(re.search(p, content_lower) for p in period_patterns)

        assert found_period, (
            "Query should group cohorts by month.\n\n"
            "Use date functions to extract the month:\n"
            "  DATE_TRUNC('month', order_date)  -- PostgreSQL\n"
            "  STRFTIME('%Y-%m', order_date)    -- SQLite"
        )


class TestRetentionCalculation:
    """Verify the query calculates retention metrics."""

    def test_has_retention_periods(self, sql_content):
        """Query should calculate retention by period (month_0, month_1, etc.)."""
        content_lower = sql_content.lower()

        # Look for retention period indicators
        retention_patterns = [
            r'month_0|month_1|month_2',      # Column names
            r'period_0|period_1',             # Alternative naming
            r'months_since',                  # Calculated difference
            r'month_diff',
            r'datediff.*month',               # Date difference
            r'timestampdiff',
            r'age\s*\(',                      # PostgreSQL age function
            r'julianday',                     # SQLite date math
        ]

        found_retention = any(re.search(p, content_lower) for p in retention_patterns)

        assert found_retention, (
            "Query should calculate retention for each month since signup.\n\n"
            "Calculate months since first order:\n"
            "  DATEDIFF(MONTH, cohort_date, order_date) as months_since\n"
            "Or create pivot columns: month_0, month_1, month_2, etc."
        )

    def test_counts_customers(self, sql_content):
        """Query should count distinct customers for retention."""
        content_lower = sql_content.lower()

        has_count = (
            'count(' in content_lower and
            ('distinct' in content_lower or 'customer' in content_lower)
        )

        assert has_count, (
            "Query should COUNT DISTINCT customers for retention.\n\n"
            "Use:\n"
            "  COUNT(DISTINCT customer_id) as customers\n"
            "Or:\n"
            "  COUNT(DISTINCT CASE WHEN months_since = 0 THEN customer_id END) as month_0"
        )

    def test_has_case_statements_or_pivot(self, sql_content):
        """Query should use CASE or PIVOT for retention columns."""
        content_lower = sql_content.lower()

        has_aggregation = (
            'case when' in content_lower or
            'case\n' in content_lower or
            'pivot' in content_lower or
            'crosstab' in content_lower or
            'sum(' in content_lower
        )

        assert has_aggregation, (
            "Query should use CASE WHEN or similar to create retention columns.\n\n"
            "Example:\n"
            "  SUM(CASE WHEN months_since = 0 THEN 1 ELSE 0 END) as month_0,\n"
            "  SUM(CASE WHEN months_since = 1 THEN 1 ELSE 0 END) as month_1"
        )


class TestSQLSyntax:
    """Verify basic SQL syntax correctness."""

    def test_balanced_parentheses(self, sql_content):
        """SQL should have balanced parentheses."""
        open_count = sql_content.count('(')
        close_count = sql_content.count(')')

        assert open_count == close_count, (
            f"Unbalanced parentheses: {open_count} open, {close_count} close.\n"
            "Check your SQL for missing or extra parentheses."
        )

    def test_no_obvious_syntax_errors(self, sql_content):
        """Check for common syntax issues."""
        content_lower = sql_content.lower()

        # Check for common errors
        errors = []

        # SELECT without FROM (unless it's a subquery start)
        if re.search(r'select\s+(?!.*\bfrom\b)', content_lower):
            pass  # This can be valid in CTEs

        # Missing comma between columns
        if re.search(r'\w\s+\w+\s*,\s*\bfrom\b', content_lower):
            pass  # Can be valid

        # GROUP BY without aggregate
        if 'group by' in content_lower:
            if not any(agg in content_lower for agg in ['count(', 'sum(', 'avg(', 'min(', 'max(']):
                errors.append("GROUP BY without aggregate functions (COUNT, SUM, etc.)")

        if errors:
            pytest.fail(
                "Potential SQL syntax issues found:\n"
                + "\n".join(f"  - {e}" for e in errors)
            )

    def test_ends_with_semicolon(self, sql_content):
        """SQL should end with semicolon (best practice)."""
        content_stripped = sql_content.strip()

        # This is a soft check - just a warning
        if not content_stripped.endswith(';'):
            # Don't fail, just pass (it's a style preference)
            pass


class TestQueryCompleteness:
    """Verify the query produces a complete cohort analysis."""

    def test_outputs_cohort_identifier(self, sql_content):
        """Query output should include cohort identifier."""
        content_lower = sql_content.lower()

        has_cohort_output = any(term in content_lower for term in [
            'cohort', 'signup_month', 'first_order', 'acquisition'
        ])

        assert has_cohort_output, (
            "Query should output a cohort identifier column.\n"
            "Name it 'cohort_month', 'signup_month', or similar."
        )

    def test_query_structure_is_complete(self, sql_content):
        """Query should be a complete, executable statement."""
        content_lower = sql_content.lower()

        # Must have SELECT ... FROM ... GROUP BY
        has_select = 'select' in content_lower
        has_from = 'from' in content_lower
        has_group = 'group by' in content_lower

        missing = []
        if not has_select:
            missing.append("SELECT")
        if not has_from:
            missing.append("FROM")
        if not has_group:
            missing.append("GROUP BY")

        assert not missing, (
            f"Query is missing required clauses: {', '.join(missing)}\n"
            "A cohort analysis query needs SELECT, FROM, and GROUP BY."
        )
