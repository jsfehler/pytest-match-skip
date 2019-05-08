pytest-match-skip
=================

.. image:: https://img.shields.io/pypi/v/pytest-match-skip.svg
    :target: https://pypi.org/project/pytest-match-skip
    :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/pytest-match-skip.svg
    :alt: PyPI - Python Version
    :target: https://github.com/jsfehler/pytest-match-skip

.. image:: https://img.shields.io/github/license/jsfehler/pytest-match-skip.svg
    :alt: GitHub
    :target: https://github.com/jsfehler/pytest-match-skip/blob/master/LICENSE

.. image:: https://travis-ci.org/jsfehler/pytest-match-skip.svg?branch=master
    :target: https://travis-ci.org/jsfehler/pytest-match-skip
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/jsfehler/pytest-match-skip?branch=master
    :target: https://ci.appveyor.com/project/jsfehler/pytest-match-skip/branch/master
    :alt: See Build Status on AppVeyor


Skip matching marks. Matches partial marks using wildcards.

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------

* Allows any tag to be used for a skip or xfail
* Wildcards can be used for tags with variable parts (ie: Specify bug\_.* for bug_123, bug_777)
* Important tags can be specified and the user will be warned when they're skipped
* Tags that should be skipped can be forced to run anyways


Installation
------------

You can install "pytest-match-skip" via `pip`_ from `PyPI`_::

    pip install pytest-match-skip


Usage
-----

command line options
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* The following pytest options can be used on the command line:
    - --skip_marks
    - --important_marks
    - --run_skips
    - --xfail_skips


pytest ini options
^^^^^^^^^^^^^^^^^^
* The following options can be added to a pytest.ini file:
    - skip_marks: List of marks that will be detected
    - important_marks: List of marks that will warn the user if skipped
    - run_skips: true or false to run tests with a skip mark
    - xfail_skips: true or false to xfail instead of skip the marked tests

    Example:

    .. code-block:: python

        [pytest]
        skip_marks = bug_.* .*_tracker .*_known_failure_.*
        important_marks = smoke .*_sanity important_.*
        run_skips = false
        xfail_skips = false

Hooks
^^^^^
The following pytest hooks are available:

- pytest_match_skip_reason(request, message) - Called if a test is skipped
- pytest_match_skip_run_skip_warning(request, message) - Called if run_skips is true and a test would otherwise be skipped.
- pytest_match_skip_important_warning(request, message) - Called when important_marks are skipped


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-match-skip" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/jsfehler/pytest-match-skip/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
