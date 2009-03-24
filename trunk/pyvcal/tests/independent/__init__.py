from unittest import TestSuite, TestCase
from basic import TestBasic
from repository import *
from branch import *
from revisionproperties import*

def tests(test_module):
    """return a testsuite that may use API"""
    
    tests = [
        TestBasic, 
        TestRepositoryRevisions,
        TestRepositoryBranches,
        TestRepositoryURI,
        TestRepositoryCreate,
        TestBranchName,
        TestBranchHead,
        TestRevisionPropertiesRevision,
        TestRevisionPropertiesCommitMessage,
        TestRevisionPropertiesCommitter,
        TestRevisionPropertiesTime,
        TestRevisionPropertiesRevisionID
        ]
    
    result = TestSuite([case(test_module) for case in tests])
    
    return result  

