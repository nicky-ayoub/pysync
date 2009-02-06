class Revision(object):
    """The complete state of a branch at a given time"""
    def __init__(self):
        super(Revision, self).__init__()

    def get_predecessors(self):
        """Return a list of Revisions that flow into this Revision"""
        raise NotImplementedError 
        
    def get_properties(self):
        """Get the RevisionProperties for this revision."""
        raise NotImplementedError
        
    @classmethod
    def get_diff(cls, a, b, paths=None):
        """Return the diff from Revision a to Revision b, optionally restricted to the given file(s) on paths"""
        raise NotImplementedError 