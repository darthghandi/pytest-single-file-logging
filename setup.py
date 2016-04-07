#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-single_file_logging',
    version='0.1.2',
    author='Chris Saxey',
    author_email='railesax@adobe.com',
    maintainer='Chris Saxey',
    maintainer_email='railesax@adobe.com',
    license='Apache Software License 2.0',
    url='https://github.com/darthghandi/pytest-single_file_logging',
    description='Allow for multiple processes to log to a single file',
    long_description=read('README.rst'),
    packages=['pytest_single_file_logging'],
    install_requires=['pytest>=2.8.1', 'gevent>=1.1.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'pytest-single_file_logging = pytest_single_file_logging:plugin',
        ],
    },
)
