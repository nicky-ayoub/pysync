class Resource(object):
    """A versioned object"""
    def __init__(self):
        super(Resource, self).__init__()
    
    def get_latest_revision(self):
        """Return the last revision this was modified"""
        raise NotImplementedError