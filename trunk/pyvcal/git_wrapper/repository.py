from git import *

from .revision import Revision

class Repository(object):
    def __init__(self, path=None): # replace kwargs with whatever you need to init
        super(Repository, self).__init__()
        self._path = path
        self._repo = Repo(self._path)
    
    def get_uri(self):
        """Return path of repository(canonical), not working copy repo"""
        return self._path
        raise NotImplementedError
        
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
        # DEPRECATED by __init__? Keeping it in here for now
        # TODO: decide if this should be removed
        self._repo = Repo(uri)
        self._path = uri
        
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
