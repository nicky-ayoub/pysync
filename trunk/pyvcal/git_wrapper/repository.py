from git import *

class Repository(object):
    def __init__(self):
        super(Repository, self).__init__()
        
    def connect(self, uri):
        """Initialize a connection to the repository; uri is a string."""
        self.repo = git.Repo(uri)
        self.uri = uri

    def get_uri(self):
        return self.uri
        
    def get_branches(self):
        # stolen blatantly from pyvcs/git_backend.py. also, totally broken. lolz
        # return dict((b.name, Branch(b, self)) for b in self.repo.branches)
        raise NotImplementedError
    
    def get_revisions(self, revision_id=None):
        """Return a dictionary of all revisions chronologically from `master`"""
        revision_dict = dict((r.id, _log(r)) for r in self.repo.commits)
        return revision_dict
        # if revision_id is None
        #     # default behavior is to return the HEAD
        #     # gitrev = self.repo.commits()[0]
        #     gitrev = self.repo.heads[0].commit
        #     return _log(gitrev)
        # elsif
        #     gitrev = self.repo.commit(revision_id) # git.Commit object
        #     return _log(gitrev) # convert git.Commit to pyvcal.GitRevision for now

    
    def _log(gitrev):
        """
        Takes a git.Commit object returns a corresponding GitRevision obj
        This is called _log since it's analogous to the SVN equivalent in
        /pyvcall/pyvcal/subversion
        """
        rev = GitRevision()
        rev.id = gitrev.id() # return the abbreviated id, not the whole 40-char string
        return rev
        

# class Repository(object):
#     """A container for codelines"""
#     def __init__(self):
#         super(Repository, self).__init__()
#     
#     def get_uri(self):
#         """Return the URI of the repository"""
#         raise NotImplementedError 
#         
#     def get_branches(self):
#         """Return the branches available in the repository"""
#         raise NotImplementedError 
#         
#     def get_revision(self, revision_id):
#         """Return the Revision object corresponding to revision_id"""
#         raise NotImplementedError 
#     
#     uri = property(get_uri)
#     branches = property(get_branches)
#     revision = property(get_revision)