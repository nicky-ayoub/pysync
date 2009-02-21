class RevisionProperties(object):
    """Metadata for a revision"""
    
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
    
    def get_revision_id(self):
        """Return the revision identifier of the revision."""
        pass
    
    revision = property(get_revision)
    commit_message = property(get_commit_message)
    committer = property(get_committer)
    time = property(get_time)
    revision_id = property(get_revision_id)
