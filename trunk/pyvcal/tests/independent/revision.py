import modulespecific
import unittest

class TestRevision(modulespecific.ModuleSpecificTestCase):
    """Test the RevisionProperties interface."""        
    def setUp(self):
        """Create and connect to a repository."""
        self.basic_repo = self.test_module.BasicRepository()
        self.repo = self.basic_repo.repo()
		
	"""Get the latest revision from that repository."""
	self.revisions = self.repo.revisions
	self.head = self.revisions[len(self.revisions)]
        
    def tearDown(self):
        """Destroy the created repository."""
        self.basic_repo.teardown()

class TestRevisionPredecessors(TestRevision):
    """Test RevisionProperties.predecessors"""
    def runTest(self):
        """Test that the latest revision returns the expected predecessor i.e: Revision(rev_num - 1)."""
        latest_rev = self.head.predecessors
        #self.assertEquals(latest_rev, self.head)

class TestRevisionGetProperties(TestRevision):
    """Test RevisionProperties.properties"""
    def runTest(self):
        """Test that the 'basic' test Revision.properties returns a non-null properties object."""
        props = self.head.properties
        self.assert_(props)
        self.assert_(props.committer)
        self.assert_(props.time)
        self.assert_(props.commit_message)	
        
class TestRevisionDiffWithParents(TestRevision):
    """Test RevisionProperties.diff_with_parents"""
    def runTest(self):
        """Test the get diff with parents returns a valid RevisionDiff object."""
        self.assertRaises(NotImplementedError, self.head.diff_with_parent)

