#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    with open(file_path, 'r') as f:
        return f.read()


setup(
    name='pytest-match-skip',
    version='0.2.1',
    author='Joshua Fehler',
    author_email='jsfehler@gmail.com',
    maintainer='Joshua Fehler',
    maintainer_email='jsfehler@gmail.com',
    license='MIT',
    url='https://github.com/jsfehler/pytest-match-skip',
    description='Skip matching marks. Matches partial marks using wildcards.',
    long_description=read('README.rst'),
    packages=['pytest_match_skip'],
    install_requires=['pytest>=4.4.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'match-skip = pytest_match_skip.plugin',
        ],
    },
)
