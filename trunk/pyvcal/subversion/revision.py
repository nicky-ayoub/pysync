from revisionproperties import RevisionProperties
from resource import Resource
from revisiondiff import RevisionDiff

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
        self._resource = Resource(self.ra_api, self.branch_path, self.paths, self.revnum)

    def get_predecessors(self):
        """ Return a list of Revision(s) that flow into this Revision """
        raise NotImplementedError 

    def get_resource(self):
        """ Return the Resource that belongs to this Revision """
        return self._resource
        
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
        
        self.diff_dict = {}
        paths = os.path.join(self.branch_path, paths)

        for path in self.paths:
            # We do not want a leading '/' on our path
            if path[0] == '/':
                path = path[1:]

            if not path.startswith(paths):
                continue
            src = Revision((self.revnum-1), self.author, self.log, 
                            self.date, self._get_node_path(path), 
                            self.ra_api, self.branch_path)
            dst = Revision(self.revnum, self.author, self.log, 
                            self.date, self._get_node_path(path), 
                            self.ra_api, self.branch_path)

            self.diff_dict[self._get_node_path(path)] = RevisionDiff(src, dst)

        return self.diff_dict

    def _get_node_path(self, path):
        """Return the node path of a given path which is everything
           after self.branch_path."""

        branch_path = os.path.join(self.branch_path, '')
        # The path should always be prefixed by the branch path, 
        #assert path.startswith(branch_path)
        
        return path[len(branch_path):]

    predecessors = property(get_predecessors)
    properties = property(get_properties)
    diff_with_parent = property(get_diff_with_parent)

