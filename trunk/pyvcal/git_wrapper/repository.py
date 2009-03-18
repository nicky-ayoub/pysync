from git import *

from .revision import Revision
from .branch import Branch

class Repository(object):
    """A Git repository."""
    
    def __init__(self, path=None): # replace kwargs with whatever you need to init
        """Initialize a Git repository. Local path is needed."""
        super(Repository, self).__init__()
        self._path = path
        self._repo = Repo(self._path)
    
    def get_uri(self):
        """Return path of repository"""
        return self._path
        
    def get_branches(self):
        """Return the branches available in the repository as a list"""
        branch_list = list((Branch(b.name, Revision(b.commit.id, self._repo), self._repo)) for b in self._repo.branches)
        return branch_list
    
    def get_latest_revision(self, branch_id='master'):
        # Return latest revision obj in the specified branch; default is 'master'
        """
        Return latest Revision object in the optional specified branch (string);
        Default behavior is 'master' branch.
        """
        gitrev = self._repo.commits(start=branch_id)[0] # git.Commit at head of specified branch
        return Revision(gitrev.id, self._repo)
    
    def get_revisions(self, revision_id=None):
        """
        Return a dictionary of last 10 revisions; key is revid (40-char hash)
        and value is a corresponding Revision obj
        """
        revision_dict = dict((r.id, Revision(r.id, self._repo)) for r in self._repo.commits())
        return revision_dict
        

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
        
        DEPRECATED. Leaving it in just in case something still uses it.
        TODO: Find anything that still depends on this.
        """
        return None
        # rev = Revision()
        # rev.id = gitrev.id() # return the abbreviated id, not the whole 40-char string
        # return rev
        
    uri = property(get_uri)
    branches = property(get_branches)
    revisions = property(get_revisions)
