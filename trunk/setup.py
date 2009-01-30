#!/usr/bin/env python

from distutils.core import setup

setup(name='PySync',
	  version='0.01',
	  description='Python Version Control Abstraction Layer',
	  author='The PySync Team',
	  author_email='pysync-discuss@googlegroups.com',
	  url='http://code.google.com/p/pysync',
	  packages=['pysync', 'pysync.util'],
	  package_dir={'pysync': 'src/pysync'})