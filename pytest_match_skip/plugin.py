# -*- coding: utf-8 -*-
from pytest_match_skip import check_skip_prefixes


def pytest_addhooks(pluginmanager):
    """Register plugin hooks."""
    from pytest_match_skip import hooks
    pluginmanager.add_hookspecs(hooks)


# Default implementations of the hooks
def pytest_match_skip_reason(request, message):
    """The reason the test was caught by match_skip."""
    print(message)


def pytest_match_skip_run_skip_warning(request, message):
    """The warning message when running tests that should be skipped."""
    print(message)


def pytest_match_skip_important_warning(request, message):
    """The warning message when skipping important tests."""
    print(message)


def pytest_runtest_setup(item):
    check_skip_prefixes.check_skip_prefixes(item)


def pytest_addoption(parser):
    parser.addini(
        'skip_marks',
        'Tests with a matching mark will be skipped'
    )
    parser.addoption(
        '--skip_marks',
        type=str,
        action='append',
        help='Tests with a matching mark will be skipped'
    )
    parser.addini(
        'important_marks',
        'User will be warned if tests with this tag are skipped.'
    )
    parser.addoption(
        '--important_marks',
        type=str,
        action='append',
        help='User will be warned if tests with this tag are skipped.'
    )
    parser.addini(
        'run_skips',
        'If true, runs tests that are tagged for skipping.'
    )
    parser.addoption(
        '--run_skips',
        type=bool,
        help='If true, runs tests that are tagged for skipping.'
    )
    parser.addini(
        'xfail_skips',
        'Instead of skipping, xfail the tagged tests'
    )
    parser.addoption(
        '--xfail_skips',
        type=bool,
        help='Instead of skipping, xfail the tagged tests'
    )
