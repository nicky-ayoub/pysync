from unittest import TestCase

class ModuleSpecificTestCase(TestCase):
    def __init__(self, test_module):
        super(ModuleSpecificTestCase, self).__init__()
        self.test_module = test_module
        
    def __str__(self):
        return str(self.__class__) + ": " + self.test_module.__name__