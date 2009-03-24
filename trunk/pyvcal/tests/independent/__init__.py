from unittest import TestSuite, TestCase

from basic import TestBasic
from branch import *
from repository import *
from revision import *
from revisionproperties import *
from user import TestUserAuthor

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
        TestRevisionPropertiesRevisionID,
        TestRevisionPredecessors,
        TestRevisionGetProperties,
        TestRevisionDiffWithParents,
        TestUserAuthor
        ]
    
    result = TestSuite([case(test_module) for case in tests])
    
    return result  

