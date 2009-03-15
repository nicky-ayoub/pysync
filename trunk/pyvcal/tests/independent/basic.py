import modulespecific
import unittest

# Basic sanity test.


class TestBasic(modulespecific.ModuleSpecificTestCase):        
    def setUp(self):
        self.basic_repo = self.test_module.BasicRepository()
        self.repo = self.basic_repo.repo()

    def runTest(self):
        self.assertTrue(self.repo)
        revisions = self.repo.revisions
        self.assertEquals(len(revisions), 4)
        
    def tearDown(self):
        self.basic_repo.teardown()
        
#    suite = unittest.TestLoader().loadTestsFromTestCase(TestBasic)
    