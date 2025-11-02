"""Pytest configuration for consultant template tests.

Ensures tests run from the correct directory context.
Contract tests (consultant, identity, internal_state, wake) must run from project root.
"""

import os
import pytest
from pathlib import Path


@pytest.fixture(scope="session", autouse=True)
def ensure_project_root():
    """Ensure contract tests run from project root where .aget/ exists."""
    # Find project root by looking for .aget/version.json
    current = Path.cwd()

    # If already at project root, nothing to do
    if (current / ".aget" / "version.json").exists():
        return

    # If in tests/ subdirectory, move up
    if current.name == "tests" and (current.parent / ".aget" / "version.json").exists():
        os.chdir(current.parent)
        return

    # Otherwise, assume tests are running from project root
    # (this accommodates CI/CD environments)
    pass
