#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='oblique',
    version='0.1',
    description='An indirect static site generator',
    install_requires=['lxml', 'cssselect'],
    setup_requires=['flake8'],
    license='GPL',
    packages=find_packages(),
    test_suite='oblique.tests',

    author='Nik Nyby',
    author_email='niknyby@riseup.net',
    url='https://github.com/nikolas/oblique',

    entry_points={
        'console_scripts': ['oblique = oblique.oblique:main'],
    },
)
