from repository import Repository
from property import ResourceProperties

class Resource(object):
    """ A versioned object """

    def __init__(self, ra_api, branch_path=None, path=None, revnum=None):
        super(Resource, self).__init__()
        
        self._ra_api = ra_api
        self._branch_path = branch_path
    	self._path = path
    	self._revnum = revnum

    	self._resource_proplist = ResourceProperties(self, revnum, path)
    
    def get_latest_revision(self):
        """ Return the last revision this was modified """
        raise NotImplementedError
        
    def get_properties(self):
        """ Return the properties of a resource """
	    # self.repo = Repository(path=_path)
	    # self.rev = repo.get_revisions()
    	# simply return the entry in the rev_prop dictionary entry _revnum
       	# return self.rev[self._revnum].get_properties()
    	# or .......
	    # return self._ra_api.rev_proplist(self._revnum)
        return self._resource_proplist
    
    def _get_ra_api(self):
        return self._ra_api

    def _full_path(self):
        """ Returns the full path of this Resource """
        return str(os.path.join(self._branch_path, _path))

    latest_revision = property(get_latest_revision)
    properties = property(get_properties)


