from unittest import TestSuite, TestCase
from basic import TestBasic
from repository import *

def tests(test_module):
    """return a testsuite that may use API"""
    
    tests = [
        TestBasic, 
        TestRepositoryRevisions,
        TestRepositoryBranches,
        TestRepositoryURI,
        TestRepositoryCreate
        ]
    
    result = TestSuite([case(test_module) for case in tests])
    
    return result  

