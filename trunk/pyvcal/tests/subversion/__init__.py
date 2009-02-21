from unittest import TestSuite

import os
import subprocess

import pyvcal


api = pyvcal.get_api('subversion')

path = os.path.join(os.path.dirname(__file__), '..', 'repositories', 'subversion')

class BasicRepository(object):
    """Represents our 'basic' test repository"""
    def __init__(self):
        super(BasicRepository, self).__init__()
        os.chdir(path)
        subprocess.Popen(['bash', 'create_basic_repository.sh'], 
                         stdout=subprocess.PIPE).wait()
        
    def repo(self):
        """Return the PyVCAL Repository"""
        return api.Repository(path=os.path.join(path, 'svn-merge-branch'))

    def teardown(self):
        pass

test_subversion = TestSuite()