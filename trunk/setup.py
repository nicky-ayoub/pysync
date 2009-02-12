from setuptools import setup, find_packages

setup(
   name='PyVCAL',
   version='0.01',
   description='Python Version Control Abstraction Layer',
   long_description="""\
   PyVCAL is a version control system abstraction layer.
	    
   Modern version control systems such as Git, Perforce and Subversion provide APIs. These APIs share many concepts but it is not easy to write code to support more than one API.
	    
   PyVCAL aims to provide a common interface to these APIs. It is analogous to ODBC or JDBC for databases.
   """,
   author='The PyVCAL Team',
   author_email='pysync-discuss@googlegroups.com',
   maintainer='The PyVCAL Team',
   maintainer_email='pysync-discuss@googlegroups.com',
   url='http://code.google.com/p/pysync',
   packages=find_packages(),
   classifiers=[ 
   'Development Status :: 1 - Planning',
   'Intended Audience :: Developers',
   'Intended Audience :: System Administrators',
   'License :: OSI Approved :: BSD License',
   'Natural Language :: English',
   'Programming Language :: Python',
   'Topic :: Software Development :: Libraries',
   'Topic :: Software Development :: Version Control'
   ],
   test_suite="pyvcal.tests.test_all"
   #	    ,platforms=""""""
)