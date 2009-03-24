import modulespecific
import unittest

class TestBranch(modulespecific.ModuleSpecificTestCase):
    """Test the Branch interface."""        
    def setUp(self):
        """Create, connect to a repository and grab a branch."""
        self.basic_repo = self.test_module.BasicRepository()
        self.repo = self.basic_repo.repo()
        self.branches = self.repo.branches['']
        
    def tearDown(self):
        """Destroy the created repository."""
        self.basic_repo.teardown()

class TestBranchName(TestBranch):
    """Test Branch.name"""
    def runTest(self):
        """Test that the 'basic' test Branch.get_name returns the proper name"""
        self.assertTrue(self.branches)
        name = self.branches.name
        self.assertEquals(name, '')

class TestBranchHead(TestBranch):
    """Test Branch.head"""
    def runTest(self):
        """Test that the 'basic' test Branch reports the latest revision in this branch."""
        latest_rev = self.branches.head._get_revision_number()
        self.assertEquals(latest_rev, 4)
        
