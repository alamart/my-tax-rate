#!/usr/bin/env python

from setuptools import setup, find_packages

with open('requirements.txt') as f:
	required = f.read().splitlines()

import src

setup(
    name="My-Tax-Rate",
    version=src.__version__,

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=required,

    # Packages
    packages=find_packages(),

    # metadata to display on PyPI
    author="Alamart",
    author_email="me@example.com",
    description="Calculate your 2019 French tax rate",
    license="Apache License 2.0",
    keywords="tax france 2019",
    url="https://github.com/alamart/my-tax-rate",   # project home page, if any
    entry_points = {
        'console_scripts': [
            'mytax = src.impots:main',
        ],
    },
)