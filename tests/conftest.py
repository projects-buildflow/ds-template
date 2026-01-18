"""Shared pytest configuration and fixtures for task tests."""

import os
import pytest
from pathlib import Path


def pytest_addoption(parser):
    """Add custom command-line options for pytest."""
    parser.addoption(
        "--student-folder",
        action="store",
        default=None,
        help="Path to student's submission folder (e.g., cohort/rahul-kumar)"
    )


@pytest.fixture
def student_folder(request):
    """Get path to student's submission folder from CLI argument or environment."""
    # First try CLI argument
    folder = request.config.getoption("--student-folder")

    # Fallback to environment variable
    if not folder:
        folder = os.environ.get("STUDENT_FOLDER")

    # For local testing, allow using a test folder
    if not folder:
        folder = os.environ.get("TEST_STUDENT_FOLDER")

    if folder:
        return str(Path(folder).resolve())

    return None


@pytest.fixture
def student_name(student_folder):
    """Extract student name from folder path."""
    if student_folder:
        return Path(student_folder).name
    return os.environ.get("STUDENT_NAME", "test_student")


@pytest.fixture
def student_path(student_folder):
    """Convert student_folder string to Path object."""
    if student_folder:
        return Path(student_folder)
    return None


@pytest.fixture
def data_path():
    """Get path to shared data folder."""
    return Path(__file__).parent.parent / "data"


@pytest.fixture
def sample_customers(data_path):
    """Load sample customers data."""
    import pandas as pd

    csv_path = data_path / "customers.csv"
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return None


@pytest.fixture
def sample_orders(data_path):
    """Load sample orders data."""
    import pandas as pd

    csv_path = data_path / "orders.csv"
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return None


@pytest.fixture
def sample_products(data_path):
    """Load sample products data."""
    import pandas as pd

    csv_path = data_path / "products.csv"
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return None
