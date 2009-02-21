import time

class Revision(object):
    def __init__(self, rev_id, repo):
        # all we need is the hash and repo; we let gitpython do the rest
        super(Revision, self).__init__()
        self._rev_id = rev_id
        self._repo = repo
        self._git_commit = self._repo.commit(self._rev_id)

    def get_predecessors(self):
        """Return a list of immediate Revisions that flow into this Revision"""
        parent_list = self._git_commit.parents # git.Commit[]
        return list(Revision(p.id, p.repo) for p in parent_list)
        
    def get_properties(self):
        """Get the RevisionProperties for this revision."""
        # rev = self._repo.commit(self._rev_id) # git.Commit obj representing _rev_id
        raise NotImplementedError
        author = User(self._git_commit.committer.name) # User(string)
        log = self._git_commit.message # string
        committed_timedate = self._git_commit.committed_date # python DateTime obj
        return RevisionProperties(self, self._rev_id, author, log, committed_timedate)
        
    def get_diff_with_parent(self, paths=None):
        """Return the RevisionDiff from this revision to its parent, optionally restricted to the given file(s) on paths
        
        If there is more than one parent, this method may return a fake RevisionDiff with no content to represent a merge.
        """
        # note to self: r1.diff(commit, commit.parents[0])
        diff = self._repo.diff(self._git_commit, self._git_commit.parents[0])
        # TODO: implement RevisionDiff to implement this
        raise NotImplementedError
    

        
    @classmethod
    def diff(cls, src, dst, paths=None):
        """Return the RevisionDiff from Revision src to Revision dst, optionally restricted to the given file(s) on paths"""
        # paths functionality not implemented yet
        # TODO: implement RevisionDiff to implement this
        
        raise NotImplementedError
    
    predecessors = property(get_predecessors)
    properties = property(get_properties)
    diff_with_parent = property(get_diff_with_parent)
