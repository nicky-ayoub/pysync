class Repository(object):
    """A container for codelines"""
    def __init__(self, vcs):
        super(Repository, self).__init__()
        self.__vcs = vcs
    
    def get_uri(self):
        """Return the URI of the repository"""
        raise NotImplementedError 
        
    def get_branches(self):
        """Return the branches available in the repository"""
        raise NotImplementedError 
        
    def get_revision(self, revision_id):
        """Return the Revision object corresponding to revision_id"""
        raise NotImplementedError 
    
    def get_vcs(self):
        """Return underlying VCS for this repository"""
        return self.__vcs
    
    uri = property(get_uri)
    branches = property(get_branches)
    revision = property(get_revision)
    vcs = property(get_vcs)