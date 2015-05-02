# coding: utf-8
from __future__ import unicode_literals

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from favicon import __version__

test_requirements = [
    'pytest',
    'pytest-cov',
    'coveralls'
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))

setup(
    name='favicon',
    version=__version__,
    license='MIT',

    author='Tomáš Ehrlich',
    author_email='tomas.ehrlich@gmail.com',

    description='Favicon and touch icons generator',
    long_description=open('README.md').read(),
    url='https://github.com/tricoder42/favicon',

    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,

    cmdclass={'test': PyTest},
    tests_require=test_requirements,
    extras_require={
        'tests': test_requirements,
        'django': [
            'django'
        ],
    },

    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
