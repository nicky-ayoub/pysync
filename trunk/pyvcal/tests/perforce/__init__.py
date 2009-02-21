from unittest import TestSuite
import os
import subprocess
import signal
import pyvcal

api = pyvcal.get_api('perforce')


path = os.path.join(os.path.dirname(__file__), 
                    '..', 
                    'repositories', 
                    'perforce')

class BasicRepository(object):
    """Represents our 'basic' test repository"""
    def __init__(self):
        super(BasicRepository, self).__init__()
        os.chdir(path)
        subprocess.Popen(['bash', 'create_basic_repository.sh'],
                         stdout=subprocess.PIPE).wait()
        os.chdir(os.path.join('basic', 'repo'))
        self.p4d = subprocess.Popen(['p4d'], stdout=subprocess.PIPE)
        
    def repo(self):
        """Return the PyVCAL Repository"""
        return api.Repository()

    def teardown(self):
        os.kill(self.p4d.pid, signal.SIGKILL)

test_perforce = TestSuite()

