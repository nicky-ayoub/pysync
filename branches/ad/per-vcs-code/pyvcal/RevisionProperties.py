class RevisionProperties(object):
    """Metadata for a revision"""
    def __init__(self):
        super(RevisionProperties, self).__init__()
    
    def get_revision(self):
        """Return the revision to which these properties apply."""
        pass
        
    def get_commit_message(self):
        """Return a unicode string containing the commit message for the Revision."""
        pass
        
    def get_committer(self):
        """Get the User who committed the Revision"""
        pass
        
    def get_time(self):
        """Return the (TODO dataformat) of the revision"""
        pass