#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='kink',
    package_data={package: ["py.typed"] for package in find_packages()},
    packages=find_packages(),
)
