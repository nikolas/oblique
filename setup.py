#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='Oblique',
    version='0.1',
    description='An indirect static site generator',
    install_requires=['lxml'],
    license='GPL',
    packages=find_packages(),
    test_suite='oblique.tests',

    author='Nik Nyby',
    author_email='niknyby@riseup.net',
    url='https://github.com/nikolas/oblique',
)
