# -*- coding: utf-8 -*-
import pytest


def test_no_marks():
    """A test with no marks.
    This test should run and pass."""
    assert True


@pytest.mark.shipping_bug_777
def test_should_pass():
    """Tests a mark that technically contains a skip tag,
    but not in a place where the pattern should match.
    This test should run and pass. """
    assert True


@pytest.mark.important_stuff
def test_important():
    """If a mark is in the important_tags list,
    but doesn't have a skip tag, nothing should change.
    This test should run and pass."""
    assert True


def test_prefix_skipping_should_skip(testdir):
    testdir.makeini("""
        [pytest]
        skip_marks = bug_.* .*_tracker .*_known_failure_.*
        important_marks = smoke .*_sanity important_.*
        run_skips = false
        xfail_skips = false
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.mark.bug_666
        def test_prefix_skipping():
        # A mark with a prefix that indicates it should be skipped.
        # This test should be skipped.
            assert False


        @pytest.mark.bug_667
        @pytest.mark.bug_668
        @pytest.mark.bug_669
        def test_multiple_prefix_skipping():
            # Multiple marks with a prefix that indicate it should be skipped.
            # Every mark should be displayed in the skip reason.
            # This test should be skipped.
            assert False


        @pytest.mark.issue_known_failure_888
        def test_prefix_suffix_skipping():
            # A mark where there are multiple wildcards.
            # This test should be skipped.
            assert False


        @pytest.mark.bug_999
        @pytest.mark.smoke
        @pytest.mark.register_sanity
        class TestMultipleTags:

            def test_important_skipped(self):
                # Multiple marks. One to indicate the test should be skipped,
                # The other that the test is important.
                # This test should be skipped, but a warning should display.
                assert False
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_prefix_skipping SKIPPED',
        '*::test_multiple_prefix_skipping SKIPPED',
        '*::test_prefix_suffix_skipping SKIPPED',
        '*::test_important_skipped SKIPPED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_multiple_tags_should_skip(testdir):
    testdir.makeini("""
        [pytest]
        skip_marks = bug_.* .*_tracker .*_known_failure_.*
        important_marks = smoke .*_sanity important_.*
        run_skips = false
        xfail_skips = false
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.mark.bug_999
        @pytest.mark.smoke
        @pytest.mark.register_sanity
        class TestMultipleTags:

            def test_important_skipped(self):
                # Multiple marks. One to indicate the test should be skipped,
                # The other that the test is important.
                # This test should be skipped, but a warning should display.
                assert False
    """)

    result = testdir.runpytest('-sv')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_important_skipped Skipping test_important_skipped despite'
        ' the following important marks: smoke, register_sanity',
        '*Skipping test_important_skipped due to marks: bug_999',
        '*SKIPPED'
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_prefix_skipping_should_skip_options(testdir):
    testdir.makepyfile("""
        import pytest

        @pytest.mark.bug_666
        def test_prefix_skipping():
        # A mark with a prefix that indicates it should be skipped.
        # This test should be skipped.
            assert False


        @pytest.mark.bug_667
        @pytest.mark.bug_668
        @pytest.mark.bug_669
        def test_multiple_prefix_skipping():
            # Multiple marks with a prefix that indicate it should be skipped.
            # Every mark should be displayed in the skip reason.
            # This test should be skipped.
            assert False


        @pytest.mark.issue_known_failure_888
        def test_prefix_suffix_skipping():
            # A mark where there are multiple wildcards.
            # This test should be skipped.
            assert False


        @pytest.mark.bug_999
        @pytest.mark.smoke
        @pytest.mark.register_sanity
        class TestMultipleTags:

            def test_important_skipped(self):
                # Multiple marks. One to indicate the test should be skipped,
                # The other that the test is important.
                # This test should be skipped, but a warning should display.
                assert False
    """)

    result = testdir.runpytest(
        '-v',
        '--skip_mark=bug_.*', '--skip_mark=.*_tracker',
        '--skip_mark=.*_known_failure_.*',
        '--important_marks=smoke', '--important_marks=.*_sanity',
        '--important_marks=important_.*',
        '--run_skips=no',
        '--xfail_skips=false',
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_prefix_skipping SKIPPED',
        '*::test_multiple_prefix_skipping SKIPPED',
        '*::test_prefix_suffix_skipping SKIPPED',
        '*::test_important_skipped SKIPPED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
