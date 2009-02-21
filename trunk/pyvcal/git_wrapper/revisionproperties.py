class RevisionProperties(object):
    """Metadata for a revision"""
    def __init__(self, identity, repo):
        super(RevisionProperties, self).__init__()
        self._id = identity # should be a 40char git commit hash id
        self._repo = repo # repo this belongs to
    
    def get_revision(self):
        """Return the Revision obj to which these properties apply."""
        return Revision(self._id, self._repo)
        
    def get_commit_message(self):
        """Return a unicode string containing the commit message for the Revision."""
        # return self._log
        return self._repo.commit(self._id).message

        
    def get_committer(self):
        """Get the User who committed the Revision"""
        # TODO: Implement User class
        return User(self._repo.commit(self._id).committer.name)
        raise NotImplementedError
        
    def get_time(self):
        """Return the (TODO dataformat) of the revision"""
        # currently returns a python timedate obj
        return self._repo.commit(self._id).committed_date
    
    def get_revision_id(self):
        """Return the revision identifier of the revision."""
        return self._id
    
    revision = property(get_revision)
    commit_message = property(get_commit_message)
    committer = property(get_committer)
    time = property(get_time)
    revision_id = property(get_revision_id)