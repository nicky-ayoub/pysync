from revisionproperties import RevisionProperties
from subvertpy import repos, ra, NODE_NONE, NODE_DIR, NODE_FILE

class Revision(object):
    """ The complete state of a branch at a given time """
	
    def __init__(self, revnum=None, author=None, log=None, date=None, paths=None, ra_api=None, branch_path=None):
	super(Revision, self).__init__()
		
        self.revnum = revnum
        self.author = author
        self.log = log
        self.date = date
        self.paths = paths
        self.ra_api = ra_api
        self.branch_path = branch_path
		
	self._proplist = RevisionProperties(self, revnum, author, log, date)

    def get_predecessors(self):
        """ Return a list of Revisions that flow into this Revision """
        raise NotImplementedError 
        
    def get_properties(self):
        """ Get the RevisionProperties for this revision """
        #prop = ra_api.rev_proplist(self.rev)
	return self._proplist
        
    def get_diff_with_parent(self, paths=None):
        """ Return the RevisionDiff from this revision to its parent, optionally 
	restricted to the given file(s) on paths
        
        If there is more than one parent, this method may return a fake RevisionDiff 
	with no content to represent a merge.
        """
        raise NotImplementedError
        
    @classmethod
    def diff(cls, src, dst, paths=None):
        """ Return the RevisionDiff from Revision src to Revision dst, optionally 
	restricted to the given file(s) on paths """
        raise NotImplementedError 

    predecessors = property(get_predecessors)
    properties = property(get_properties)
    diff_with_parent = property(get_diff_with_parent)

