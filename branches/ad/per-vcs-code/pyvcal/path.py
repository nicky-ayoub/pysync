class Path(object):
    """A path to a versioned resource."""
    def __init__(self):
        super(Path, self).__init__()
    
    def get_resource(self, revision):
        """Return the versioned resource at this path at the given revision or None"""
        raise NotImplementedError 