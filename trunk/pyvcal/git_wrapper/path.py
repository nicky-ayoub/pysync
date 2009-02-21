class Path(object):
    """A path to a versioned resource."""
    
    def __init__(self, rev):
        self._rev = rev # Revision object
        self._id = self._rev.identity
    
    def get_resource(self, revision):
        """Return the versioned resource at this path at the given revision or None"""
        return self._rev
        
    resource = property(get_resource)
