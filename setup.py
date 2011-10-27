#!/usr/bin/env python

from setuptools import setup
import os
import sys

PACKAGE_PATH = 'src'

sys.path.insert(0, PACKAGE_PATH)
import naturalsortfield

setup(
    name='django-naturalsortfield',
    url='https://github.com/nathforge/django-naturalsortfield',
    version=naturalsortfield.version_string(),
    description='Better ordering for Django CharFields.',
    long_description=open('README.txt').read(),
    
    author='Nathan Reynolds',
    author_email='email@nreynolds.co.uk',
    
    packages=['naturalsortfield'],
    package_dir={'': PACKAGE_PATH},
)
