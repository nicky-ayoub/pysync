#!/usr/bin/env python

from distutils.core import setup

setup(name='PyVCAL',
	  version='0.01',
	  description='Python Version Control Abstraction Layer',
	  author='The PyVCAL Team',
	  author_email='pysync-discuss@googlegroups.com',
	  url='http://code.google.com/p/pysync',
	  packages=['pyvcal', 'pyvcal.util'],
	  package_dir={'pyvcal': 'src/pyvcal'})