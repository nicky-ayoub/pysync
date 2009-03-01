class Resource(object):
    """A versioned object"""
    
    def __init__(self, identity, revision, repo, isTree):
        super(Resource, self).__init__()
        self._id = identity # hash of this object
        self._revision = revision # revision this object belongs to
        self._repo = repo # repository this object belongs to
        self._isTree = isTree # Bool; if not Tree, we assume Blob/File
        if self._isTree:
            # self._obj = self._repo.
        else:
            # this Resource is a file (blob in git speak)
            self._obj = self._repo.blob(self._id)
    
    def get_latest_revision(self):
        """Return the last revision this was modified"""
        raise NotImplementedError
        
    def get_properties(self):
        """Return the properties of a resource"""
        raise NotImplementedError 
    
    latest_revision = property(get_latest_revision)
    properties = property(get_properties)
