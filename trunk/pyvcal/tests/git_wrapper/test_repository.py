from unittest import TestCase

from git_wrapper import *

class TestRepository(ModuleSpecificTestCase):
    def __init__(self):
        super(TestRepository, self).__init__()

    # setup, runtest, takedown
    def setup(self):
        repo = Repository("/Users/jwl/Documents/univ")
        return repo
    
    def testCreation(self):
        r = self.setup()
        
    def testGetURI(self):
        r = self.setup()
        self.assertEqual(r.get_uri(), "/Users/jwl/Documents/univ")
    

    def testGetLatestRevision(self):
        r = self.setup()
        r.get_latest_revision()
    
    def testGetRevisions(self):
        r = self.setup()
        r.get_revisions()
    
    def testGetBranches(self):
        r = self.setup()
        r.get_branches()
        
        


if __name__=='__main__':
    unittest.main()


