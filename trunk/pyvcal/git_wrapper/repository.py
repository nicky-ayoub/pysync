from git import *

from .revision import Revision

class Repository(object):
    def __init__(self, **kwargs):
        super(Repository, self).__init__()
    
    def get_uri(self):
        return self.git_uri
        
    def get_branches(self):
        raise NotImplementedError
    
    def get_revisions(self, revision_id=None):
        raise NotImplementedError
        """Return a dictionary of all revisions chronologically from `master`"""
        revision_dict = dict((r.id, self._log(r)) for r in self.repo.commits())
        self.repo.commits()
        return revision_dict
        
        # if revision_id is None
        #     # default behavior is to return the HEAD
        #     # gitrev = self.repo.commits()[0]
        #     gitrev = self.repo.heads[0].commit
        #     return _log(gitrev)
        # elsif
        #     gitrev = self.repo.commit(revision_id) # git.Commit object
        #     return _log(gitrev) # convert git.Commit to pyvcal.GitRevision for now
    
    @classmethod
    def create(cls,**kwargs):
        """Create a new Repository and return it."""
        raise NotImplementedError

    def _connect(self, uri):
        """Initialize a connection to the repository; uri is a string."""
        self.repo = Repo(uri)
        self.git_uri = uri
        
    def _log(self, gitrev):
        """
        Takes a git.Commit object returns a corresponding GitRevision obj
        This is called _log since it's analogous to the SVN equivalent in
        /pyvcall/pyvcal/subversion
        """
        return None
        # rev = Revision()
        # rev.id = gitrev.id() # return the abbreviated id, not the whole 40-char string
        # return rev
        
    uri = property(get_uri)
    branches = property(get_branches)
    revisions = property(get_revisions)
