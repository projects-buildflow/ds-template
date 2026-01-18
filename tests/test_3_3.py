"""Tests for Task 3.3: Query Optimization

Objective: Optimize the slow SQL query and document the changes.

This test DECISIVELY verifies:
1. Optimized SQL file exists
2. Optimization notes file exists
3. Query is different from the original slow query
4. Query maintains correct SQL structure
5. Notes explain what was slow
6. Notes explain the optimizations made
7. Query applies optimization best practices
"""

import pytest
import re
from pathlib import Path


@pytest.fixture
def week3_path(student_folder):
    """Get path to student's week-3 folder."""
    if not student_folder:
        pytest.skip("Student folder not provided")
    return Path(student_folder) / "week-3"


@pytest.fixture
def optimized_sql(week3_path):
    """Load the optimized SQL query."""
    sql_path = week3_path / "optimized_query.sql"

    if not sql_path.exists():
        pytest.fail(
            f"SQL file not found at {sql_path}\n\n"
            "Create: cohort/{your-github-username}/week-3/optimized_query.sql"
        )

    return sql_path.read_text()


@pytest.fixture
def optimization_notes(week3_path):
    """Load the optimization notes."""
    notes_path = week3_path / "optimization_notes.md"

    if not notes_path.exists():
        pytest.fail(
            f"Notes file not found at {notes_path}\n\n"
            "Create: cohort/{your-github-username}/week-3/optimization_notes.md"
        )

    return notes_path.read_text()


@pytest.fixture
def original_slow_query():
    """Load the original slow query for comparison."""
    # Try multiple possible locations
    possible_paths = [
        Path(__file__).parent.parent / "week-3" / "task-3.3" / "slow_query.sql",
        Path(__file__).parent.parent / "tasks" / "week-3" / "task-3.3" / "slow_query.sql",
    ]

    for path in possible_paths:
        if path.exists():
            return path.read_text()

    return None


class TestFilesExist:
    """Verify required files exist."""

    def test_optimized_sql_exists(self, week3_path):
        """optimized_query.sql must exist."""
        sql_path = week3_path / "optimized_query.sql"
        assert sql_path.exists(), (
            f"SQL file not found at {sql_path}\n\n"
            "Create: cohort/{your-github-username}/week-3/optimized_query.sql"
        )

    def test_optimization_notes_exist(self, week3_path):
        """optimization_notes.md must exist."""
        notes_path = week3_path / "optimization_notes.md"
        assert notes_path.exists(), (
            f"Notes file not found at {notes_path}\n\n"
            "Create: cohort/{your-github-username}/week-3/optimization_notes.md"
        )


class TestQueryContent:
    """Verify the optimized query has valid content."""

    def test_query_is_not_empty(self, optimized_sql):
        """Query must have content."""
        assert len(optimized_sql.strip()) > 50, (
            "Optimized query file is too short.\n"
            "Write a complete, optimized SQL query."
        )

    def test_query_is_valid_sql_structure(self, optimized_sql):
        """Query must have valid SQL structure."""
        sql_lower = optimized_sql.lower()

        # Must have SELECT
        assert 'select' in sql_lower, (
            "Query must have a SELECT statement."
        )

        # Must have FROM
        assert 'from' in sql_lower, (
            "Query must have a FROM clause."
        )

    def test_query_is_different_from_original(self, optimized_sql, original_slow_query):
        """Query must be different from the original slow query."""
        if original_slow_query is None:
            pytest.skip("Original slow query not found for comparison")

        # Normalize for comparison
        optimized_normalized = "".join(optimized_sql.lower().split())
        original_normalized = "".join(original_slow_query.lower().split())

        assert optimized_normalized != original_normalized, (
            "Optimized query is identical to the original slow query.\n"
            "You need to actually optimize it!"
        )


class TestOptimizationTechniques:
    """Verify query applies optimization techniques."""

    def test_avoids_select_star_in_main_query(self, optimized_sql):
        """Query should avoid SELECT * in the main query."""
        sql_lower = optimized_sql.lower()
        lines = sql_lower.split('\n')

        # Count SELECT * occurrences that aren't in comments
        select_star_count = 0
        for line in lines:
            line = line.strip()
            if line.startswith('--'):
                continue
            if 'select *' in line or 'select  *' in line:
                select_star_count += 1

        # Allow one SELECT * if it's in a CTE/subquery, but flag if main query
        if select_star_count > 1:
            pytest.fail(
                f"Found {select_star_count} instances of SELECT *.\n"
                "Best practice: Select only needed columns, not SELECT *."
            )

    def test_uses_explicit_columns(self, optimized_sql):
        """Query should select explicit column names."""
        sql_lower = optimized_sql.lower()

        # After SELECT, should have column names
        select_match = re.search(r'select\s+(\w+)', sql_lower)
        if select_match:
            first_after_select = select_match.group(1)
            # Should be a column name, not *
            assert first_after_select != '*', (
                "Main SELECT should use explicit column names, not *."
            )

    def test_mentions_join_or_cte(self, optimized_sql):
        """Query should use JOINs or CTEs for optimization."""
        sql_lower = optimized_sql.lower()

        has_join = 'join' in sql_lower
        has_cte = 'with ' in sql_lower or 'with\n' in sql_lower

        # At least one optimization technique should be present
        assert has_join or has_cte or 'where' in sql_lower, (
            "Query should use JOINs, CTEs, or WHERE clauses for optimization."
        )


class TestNotesContent:
    """Verify optimization notes explain the changes."""

    def test_notes_have_substance(self, optimization_notes):
        """Notes must have substantial content."""
        word_count = len(optimization_notes.split())

        assert word_count >= 100, (
            f"Notes have only {word_count} words.\n"
            "Explain what made the query slow and how you fixed it."
        )

    def test_notes_explain_original_problem(self, optimization_notes):
        """Notes must explain what was slow about the original."""
        content_lower = optimization_notes.lower()

        problem_terms = [
            'slow', 'performance', 'inefficient', 'problem', 'issue',
            'bottleneck', 'expensive', 'time', 'long', 'cost'
        ]
        found_problem = any(term in content_lower for term in problem_terms)

        assert found_problem, (
            "Notes should explain what made the original query slow.\n"
            "Describe the performance issues you identified."
        )

    def test_notes_explain_changes(self, optimization_notes):
        """Notes must explain the optimizations made."""
        content_lower = optimization_notes.lower()

        change_terms = [
            'changed', 'replaced', 'removed', 'added', 'optimized',
            'improved', 'instead', 'now', 'use', 'using'
        ]
        found_changes = sum(1 for term in change_terms if term in content_lower)

        assert found_changes >= 2, (
            f"Found only {found_changes} change-related terms.\n"
            "Explain what specific changes you made to optimize the query."
        )

    def test_notes_mention_specific_techniques(self, optimization_notes):
        """Notes should mention specific optimization techniques."""
        content_lower = optimization_notes.lower()

        technique_terms = [
            'select *', 'join', 'index', 'subquery', 'nested',
            'cte', 'common table', 'column', 'filter', 'where',
            'group by', 'order', 'limit'
        ]
        found_techniques = sum(1 for term in technique_terms if term in content_lower)

        assert found_techniques >= 2, (
            f"Found only {found_techniques} optimization technique mentions.\n"
            "Discuss specific techniques:\n"
            "- Avoiding SELECT *\n"
            "- Using proper JOINs instead of subqueries\n"
            "- Filtering early with WHERE\n"
            "- Using CTEs for clarity"
        )


class TestNotesStructure:
    """Verify notes have proper structure."""

    def test_notes_have_sections(self, optimization_notes):
        """Notes should have organized sections."""
        header_count = optimization_notes.count('#')

        assert header_count >= 2, (
            f"Found only {header_count} headers.\n"
            "Organize notes with sections:\n"
            "## Problem Analysis\n"
            "## Changes Made\n"
            "## Expected Improvement"
        )

    def test_notes_are_professional(self, optimization_notes):
        """Notes should be professionally written."""
        # Should have multiple paragraphs or bullet points
        has_structure = '\n\n' in optimization_notes or '- ' in optimization_notes or '* ' in optimization_notes

        assert has_structure, (
            "Notes should be well-structured.\n"
            "Use paragraphs, bullet points, or numbered lists."
        )


class TestQueryQuality:
    """Additional quality checks for the query."""

    def test_query_has_comments(self, optimized_sql):
        """Query should have comments explaining the optimization."""
        # Look for SQL comments
        has_comments = '--' in optimized_sql or '/*' in optimized_sql

        # This is a soft check - good practice but not required
        if not has_comments:
            pass  # Note: Consider adding comments to explain your query

    def test_query_is_formatted(self, optimized_sql):
        """Query should be properly formatted (not all on one line)."""
        line_count = len([l for l in optimized_sql.split('\n') if l.strip()])

        assert line_count >= 3, (
            "Query should be formatted across multiple lines for readability.\n"
            "Don't write the entire query on one line."
        )

    def test_query_handles_grouping(self, optimized_sql):
        """If query has aggregation, it should have proper GROUP BY."""
        sql_lower = optimized_sql.lower()

        has_aggregation = any(func in sql_lower for func in ['sum(', 'count(', 'avg(', 'max(', 'min('])

        if has_aggregation:
            has_group_by = 'group by' in sql_lower
            # This is expected but not always required depending on the query
            if not has_group_by:
                pass  # May be intentional
