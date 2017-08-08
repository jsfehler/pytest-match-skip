# -*- coding: utf-8 -*-

import re

import pytest
from _pytest.mark import MarkInfo


def __matches_in_test_marks(mark_list, test_marks):
    matches = []
    for mark in mark_list:
        for test_mark in test_marks:
            match = re.match(mark, test_mark)
            if match:
                matches.append(match.group(0))

    return matches


def check_skip_prefixes(item):
    """Checks a test item for any skip marks."""
    reason = None

    all_skip_marks = item.config.getini('skip_marks')

    if all_skip_marks == '':
        # No skip_marks were found.
        return

    all_skip_marks = all_skip_marks.split(' ')

    # Get the marks used on the test.
    test_marks = [
        k for k, v in item.keywords.items() if isinstance(v, MarkInfo)
    ]

    # Check if one of the marks on the test matches a skip_mark
    matches = __matches_in_test_marks(all_skip_marks, test_marks)
    if len(matches) > 0:
        str_matches = ', '.join(matches)
        msg = 'Skipping {item.name} due to marks: {str_matches}'
        reason = msg.format(**locals())

        # The test will be skipped, now check the important marks
        all_important_marks = item.config.getini('important_marks').split(' ')
        important_marks = __matches_in_test_marks(
            all_important_marks, test_marks
        )
        str_important_marks = ', '.join(important_marks)

    else:
        return

    if item.config.getini('run_skips') == 'true':
        msg = ('Running {item.name} despite the following skip marks:'
               ' {str_matches}.')
        item.config.hook.pytest_match_skip_run_skip_warning(
            request=item,
            message=msg.format(**locals())
        )
        return

    if len(important_marks) > 0:
        msg = ('Skipping {item.name} despite the following important marks:'
               ' {str_important_marks}')
        item.config.hook.pytest_match_skip_important_warning(
            request=item,
            message=msg.format(**locals())
        )

    item.config.hook.pytest_match_skip_reason(request=item, message=reason)

    if item.config.getini('xfail_skips') == 'true':
        pytest.xfail(reason)
    else:
        pytest.skip(reason)
