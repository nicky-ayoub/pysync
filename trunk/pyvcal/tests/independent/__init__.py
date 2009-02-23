from unittest import TestSuite, TestCase
from basic import TestBasic

def tests(test_module):
    """return a testsuite that may use API"""
    
    tests = [TestBasic]
    
    result = TestSuite([case(test_module) for case in tests])
    
    return result  

