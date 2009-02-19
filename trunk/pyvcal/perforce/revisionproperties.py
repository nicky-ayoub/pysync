class RevisionProperties(object):
    """Metadata for a revision"""
    def __init__(self, revision, p4dict):
        super(RevisionProperties, self).__init__()
        self._revision = revision
        self._commit_msg = p4dict['desc']
        self._time = p4dict['time']
        self._committer = p4dict['user']
        self._revision_id = p4dict['change']
        
    def get_revision(self):
        """Return the revision to which these properties apply."""
        return self._revision
        
    def get_commit_message(self):
        """Return a unicode string containing the commit message for the Revision."""
        return self._commit_msg
        
    def get_committer(self):
        """Get the User who committed the Revision"""
        return self._committer
        # TODO Return User object here
        
    def get_time(self):
        """Return the (TODO dataformat) of the revision"""
        return self._time
        # TODO Return properly formatted time
        
    def get_revision_id(self):
        """Return the revision identifier for the revision."""
        return self._revision_id
        
    revision = property(get_revision)
    commit_message = property(get_commit_message)
    committer = property(get_committer)
    time = property(get_time)
    revision_id = property(get_revision_id)