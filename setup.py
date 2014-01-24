#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='ffsm',
    version='0.1.0',
    description='ffsm is for finite state machines',
    long_description=readme + '\n\n' + history,
    author='Elevencraft Inc.',
    author_email='matt@11craft.com',
    url='https://github.com/fanscribed/ffsm',
    packages=[
        'ffsm',
    ],
    package_dir={'ffsm': 'ffsm'},
    include_package_data=True,
    tests_require=['pytest'],
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='ffsm',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    extras_require={
        'testing': ['pytest'],
    },
)
