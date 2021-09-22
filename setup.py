#!/usr/bin/env python
from setuptools import setup


if __name__ == '__main__':
    setup(
        name='OrionExample',
        version='0.0.0',
        description='Orion example',
        author='Pierre Delaunay',
        packages=[
            'OrionExample',
        ],
        setup_requires=['setuptools'],
        tests_require=['pytest', 'flake8', 'codecov', 'pytest-cov'],
    )
