import modulespecific
import unittest

class TestRepository(modulespecific.ModuleSpecificTestCase):        
    def setUp(self):
        self.basic_repo = self.test_module.BasicRepository()
        self.repo = self.basic_repo.repo()
        
    def tearDown(self):
        self.basic_repo.teardown()

class TestRepositoryRevisions(TestRepository):
    def runTest(self):
        self.assertTrue(self.repo)
        revisions = self.repo.revisions
        self.assertEquals(len(revisions), 4)

class TestRepositoryBranches(TestRepository):
    def runTest(self):
        branches = self.repo.branches
        self.assertEquals(len(branches), 1)
        
class TestRepositoryURI(TestRepository):
    def runTest(self):
        uri = self.repo.uri
        # No throw exception
        
class TestRepositoryCreate(modulespecific.ModuleSpecificTestCase):
    def runTest(self):
        self.test_module.api.test_create()
        
    
        