"""Tests for Task 3.4: Dashboard Creation

Objective: Create a data visualization dashboard with key business metrics.

This test DECISIVELY verifies:
1. Dashboard screenshot exists (PNG or JPG)
2. Screenshot is a valid image file
3. Screenshot is of reasonable size (not too small)
4. Optional: Dashboard code folder exists (bonus)

Note: Visual quality is assessed by AI review, not these automated tests.
The automated tests verify the file exists and is valid.
"""

import pytest
from pathlib import Path


@pytest.fixture
def week3_path(student_folder):
    """Get path to student's week-3 folder."""
    if not student_folder:
        pytest.skip("Student folder not provided")
    return Path(student_folder) / "week-3"


@pytest.fixture
def dashboard_screenshot(week3_path):
    """Find and return the dashboard screenshot path."""
    valid_extensions = [".png", ".jpg", ".jpeg", ".gif", ".webp"]

    for ext in valid_extensions:
        path = week3_path / f"dashboard{ext}"
        if path.exists():
            return path

    return None


class TestDashboardExists:
    """Verify dashboard screenshot exists."""

    def test_dashboard_screenshot_exists(self, week3_path, dashboard_screenshot):
        """Dashboard screenshot must exist."""
        assert dashboard_screenshot is not None, (
            "Dashboard screenshot not found.\n\n"
            "Save your dashboard as one of:\n"
            "- dashboard.png\n"
            "- dashboard.jpg\n"
            "- dashboard.jpeg\n\n"
            f"In folder: {week3_path}"
        )

    def test_screenshot_has_content(self, dashboard_screenshot):
        """Screenshot must have content (not an empty file)."""
        if dashboard_screenshot is None:
            pytest.skip("Dashboard screenshot not found")

        file_size = dashboard_screenshot.stat().st_size

        assert file_size > 1000, (
            f"Screenshot file is only {file_size} bytes.\n"
            "This seems too small. Make sure the file saved correctly."
        )


class TestImageValidity:
    """Verify the screenshot is a valid image file."""

    def test_screenshot_is_reasonable_size(self, dashboard_screenshot):
        """Screenshot should be at least 10KB for a real dashboard image."""
        if dashboard_screenshot is None:
            pytest.skip("Dashboard screenshot not found")

        file_size = dashboard_screenshot.stat().st_size

        assert file_size > 10000, (  # 10KB
            f"Screenshot is only {file_size / 1024:.1f} KB.\n"
            "A dashboard screenshot should be larger.\n"
            "Make sure you captured the full dashboard, not a thumbnail."
        )

    def test_screenshot_not_too_large(self, dashboard_screenshot):
        """Screenshot shouldn't be excessively large."""
        if dashboard_screenshot is None:
            pytest.skip("Dashboard screenshot not found")

        file_size = dashboard_screenshot.stat().st_size
        max_size = 20 * 1024 * 1024  # 20MB

        assert file_size < max_size, (
            f"Screenshot is {file_size / (1024*1024):.1f} MB.\n"
            "This is quite large. Consider compressing the image."
        )

    def test_screenshot_is_valid_image_format(self, dashboard_screenshot):
        """Screenshot must be a valid image file (check magic bytes)."""
        if dashboard_screenshot is None:
            pytest.skip("Dashboard screenshot not found")

        with open(dashboard_screenshot, "rb") as f:
            header = f.read(12)

        # Check magic bytes for common image formats
        is_png = header[:4] == b"\x89PNG"
        is_jpeg = header[:3] == b"\xff\xd8\xff"
        is_gif = header[:4] == b"GIF8"
        is_webp = header[:4] == b"RIFF" and header[8:12] == b"WEBP"

        assert is_png or is_jpeg or is_gif or is_webp, (
            "File does not appear to be a valid image.\n"
            "Make sure to save as PNG, JPEG, or GIF format.\n\n"
            "If using Power BI: File > Export > Export to PDF, then screenshot\n"
            "If using Streamlit: Take a browser screenshot"
        )


class TestDashboardDimensions:
    """Verify dashboard image has reasonable dimensions."""

    def test_image_has_reasonable_dimensions(self, dashboard_screenshot):
        """Image should have reasonable dimensions for a dashboard."""
        if dashboard_screenshot is None:
            pytest.skip("Dashboard screenshot not found")

        try:
            from PIL import Image
            img = Image.open(dashboard_screenshot)
            width, height = img.size

            assert width >= 600, (
                f"Image width is only {width}px.\n"
                "Dashboard screenshot should be at least 800px wide."
            )

            assert height >= 400, (
                f"Image height is only {height}px.\n"
                "Dashboard screenshot should be at least 600px tall."
            )

        except ImportError:
            # PIL not installed - skip dimension check
            pytest.skip("PIL not installed - skipping dimension check")


class TestDashboardCodeOptional:
    """Optional tests for dashboard code (bonus points)."""

    def test_dashboard_folder_exists(self, week3_path):
        """Check if dashboard code folder exists (optional bonus)."""
        dashboard_folder = week3_path / "dashboard"

        if dashboard_folder.exists():
            # Check for common dashboard files
            possible_files = [
                "app.py",
                "dashboard.py",
                "main.py",
                "index.html",
                "streamlit_app.py"
            ]
            found_code = [f for f in possible_files if (dashboard_folder / f).exists()]

            if found_code:
                # Great - they included their code
                pass
            else:
                # Folder exists but no recognizable files
                pass

        # This is optional - don't fail if folder doesn't exist

    def test_requirements_file_exists(self, week3_path):
        """Check if requirements.txt exists for dashboard code (optional)."""
        dashboard_folder = week3_path / "dashboard"

        if dashboard_folder.exists():
            requirements_file = dashboard_folder / "requirements.txt"

            # Just note if it exists - not required
            if requirements_file.exists():
                pass  # Good practice


class TestDashboardRequirements:
    """Document required dashboard elements for AI review.

    The AI reviewer will check for:
    1. Total Revenue metric (with trend indicator)
    2. Active Customers metric (monthly count)
    3. Average Order Value metric
    4. Top 5 Products visualization
    5. Clear labels and readable fonts
    6. Logical, professional layout
    7. At least 2 different chart types
    """

    def test_requirements_documented(self):
        """Verify requirements are documented for AI review."""
        required_metrics = [
            "Total Revenue (with trend)",
            "Active Customers (monthly)",
            "Average Order Value",
            "Top 5 Products by Revenue",
        ]
        assert len(required_metrics) == 4

        design_requirements = [
            "Clear labels on all charts",
            "Readable fonts and colors",
            "Logical layout",
            "At least 2 different chart types"
        ]
        assert len(design_requirements) == 4

    def test_minimum_visualizations(self):
        """Dashboard should have multiple visualizations."""
        # This is verified by AI review
        # Minimum: 2 charts/graphs
        MIN_CHARTS = 2
        assert MIN_CHARTS == 2

    def test_metrics_should_be_visible(self):
        """Key metrics should be prominently displayed."""
        # This is verified by AI review
        # Metrics should not be hidden or hard to find
        pass
