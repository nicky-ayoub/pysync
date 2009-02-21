from unittest import TestSuite, TestCase
    
def tests(test_module):
    """return a testsuite that may use API"""
    result = TestSuite([TestConnect(test_module)])
    
    return result  

class TestConnect(TestCase):
    def __init__(self, test_module):
        super(TestConnect, self).__init__()
        self.test_module = test_module
        
    def setUp(self):
        self.basic_repo = self.test_module.BasicRepository()
        self.repo = self.basic_repo.repo()

    def runTest(self):
        self.assertTrue(self.repo)
    
    def tearDown(self):
        self.basic_repo.teardown()
    
    def __str__(self):
        """Stringify self"""
        return "TestConnect: " + self.test_module.__name__