def pytest_match_skip_reason(request, message):
    """The reason the test was caught by match_skip."""
    pass


def pytest_match_skip_run_skip_warning(request, message):
    """The warning message when running tests that should be skipped."""
    pass


def pytest_match_skip_important_warning(request, message):
    """The warning message when skipping important tests."""
    pass
