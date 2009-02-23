from modulespecific import ModuleSpecificTestCase

class TestBasic(ModuleSpecificTestCase):        
    def setUp(self):
        self.basic_repo = self.test_module.BasicRepository()
        self.repo = self.basic_repo.repo()

    def runTest(self):
        self.assertTrue(self.repo)
        self.assertEquals(len(self.repo.revisions), 4)
    
    def tearDown(self):
        self.basic_repo.teardown()