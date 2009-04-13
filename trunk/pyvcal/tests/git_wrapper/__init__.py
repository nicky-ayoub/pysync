from unittest import TestSuite
import os
import subprocess
import signal
import pyvcal
from ...util import rmrf

api = pyvcal.get_api('git')
path = os.path.join(os.path.dirname(__file__), '..', 'repositories', 'git')

class BasicRepository(object):
    """Represents our 'basic' test repository"""
    def __init__(self):
        """Run the create_basic_repository script"""
        super(BasicRepository, self).__init__()
        os.chdir(path)
        if (os.path.exists(os.path.join(path, 'testrepo01'))):
            self.teardown() 
        subprocess.Popen(['bash', 'create_basic_repository.sh'],    
                         stdout=subprocess.PIPE).wait()
        
    def repo(self):
        """Return a newly initiated PyVCAL Repository"""
        return api.Repository(path=os.path.join(path, 'testrepo01'))

    def teardown(self):
        """Clean up the created repository"""
        rmrf(os.path.join(path, 'testrepo01'))

test_git = TestSuite()

def test_create(testinstance):
    """Test Git repository creation."""
    repo = api.Repository.create(os.path.join(path, 'testrepo01'))
    testinstance.fail("Test not implemented yet")


