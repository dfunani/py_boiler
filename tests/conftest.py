"""
Shared test fixtures and configuration for py_boiler tests.
"""

import pytest
import tempfile
import os
from pathlib import Path
from click.testing import CliRunner

from py_boiler.app import main


@pytest.fixture
def cli_runner():
    """Provide a Click CLI runner for testing."""
    return CliRunner()


@pytest.fixture
def temp_directory():
    """Provide a temporary directory for testing file operations."""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)
            yield Path(temp_dir)
        finally:
            os.chdir(original_cwd)


@pytest.fixture
def generated_files(temp_directory, cli_runner):
    """Generate the basic boilerplate files for testing."""
    result = cli_runner.invoke(main, ["new", "basic"])
    assert result.exit_code == 0
    return temp_directory


@pytest.fixture
def expected_file_list():
    """Provide the list of expected files for basic command."""
    return ["README.md", "app.py", ".gitignore", "__init__.py"]


@pytest.fixture
def sample_existing_files(temp_directory):
    """Create some existing files to test overwrite behavior."""
    existing_files = {
        "README.md": "Existing README content",
        "app.py": "Existing app content",
        "other_file.txt": "Some other content",
    }

    for filename, content in existing_files.items():
        (temp_directory / filename).write_text(content)

    return existing_files


@pytest.fixture
def mock_file_system():
    """Provide a mock file system for testing file operations."""
    import tempfile
    import os

    temp_dir = tempfile.mkdtemp()
    original_cwd = os.getcwd()

    try:
        os.chdir(temp_dir)
        yield temp_dir
    finally:
        os.chdir(original_cwd)


@pytest.fixture
def version_info():
    """Provide version information for testing."""
    from py_boiler import __version__

    return {"version": __version__, "expected_version": "2.0.1"}


@pytest.fixture
def template_constants():
    """Provide access to all template constants for testing."""
    from py_boiler.templates import (
        README_CODE,
        MAIN_CODE,
        GITIGNORE_CODE,
        PYPROJECT_TOML,
        VERSION_CODE,
    )

    return {
        "README_CODE": README_CODE,
        "MAIN_CODE": MAIN_CODE,
        "GITIGNORE_CODE": GITIGNORE_CODE,
        "PYPROJECT_TOML": PYPROJECT_TOML,
        "VERSION_CODE": VERSION_CODE,
    }


@pytest.fixture
def cli_commands():
    """Provide CLI command structure for testing."""
    return {"main": main, "new": "new", "basic": "basic"}


@pytest.fixture(autouse=True)
def cleanup_temp_files():
    """Automatically clean up temporary files after each test."""
    yield
    # This fixture runs after each test to ensure cleanup
    import gc

    gc.collect()


@pytest.fixture
def test_app_execution():
    """Provide a fixture for testing generated app execution."""

    def _execute_generated_app(app_path):
        import subprocess
        import sys

        result = subprocess.run(
            [sys.executable, str(app_path)], capture_output=True, text=True, timeout=10
        )
        return result

    return _execute_generated_app


@pytest.fixture
def test_app_import():
    """Provide a fixture for testing generated app import."""

    def _import_generated_app(app_path, temp_dir):
        import sys

        # Add temp directory to path
        sys.path.insert(0, str(temp_dir))

        try:
            # Import the app module
            import importlib.util

            spec = importlib.util.spec_from_file_location("app", app_path)
            app_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(app_module)

            return app_module
        finally:
            # Remove temp directory from path
            if str(temp_dir) in sys.path:
                sys.path.remove(str(temp_dir))

    return _import_generated_app


# Pytest configuration
def pytest_configure(config):
    """Configure pytest with custom settings."""
    # Add custom markers
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "cli: mark test as CLI test")


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names."""
    for item in items:
        # Add integration marker to integration tests
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)

        # Add slow marker to tests that might be slow
        if any(
            keyword in item.nodeid for keyword in ["concurrent", "memory", "unicode"]
        ):
            item.add_marker(pytest.mark.slow)

        # Add CLI marker to CLI tests
        if any(keyword in item.nodeid for keyword in ["cli", "command", "basic"]):
            item.add_marker(pytest.mark.cli)
