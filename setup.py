#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='zad2_justynamaciag',
    version='0.1.6',
    description="Estimating complexity od function",
    long_description=readme + '\n\n' + history,
    author="Justyna Maciąg",
    author_email='justynamaciag96@gmail.com',
    url='https://github.com/justynamaciag/zad2-justynamaciag',
    packages=[
        'zad2_justynamaciag',
    ],
    package_dir={'zad2_justynamaciag':
                 'zad2_justynamaciag'},
    entry_points={
        'console_scripts': [
            'zad2_justynamaciag=zad2_justynamaciag.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='zad2_justynamaciag',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
