import os

from git import Commit, Diff

class RevisionDiff(object):
    """The set of changes needed to transform one revision into another."""

    def __init__(self, r1, r2, repo):
        """r1 is the older revision, r2 is the newer revision.
        """
        super(RevisionDiff, self).__init__()
        self._r1 = r1
        self._r2 = r2
        self._repo = repo

    def get_value():
        """Concatenation of Unified Diffs of resources between the revisions.
        pg484 of Python in a Nutshell suggests the below method for big string
        concatenation; unified_diff =+ individual_diff apparently takes
        O(N^{2}) time. The below takes O(N) time.
        """
        d_list = Commit.diff(self._repo, self._r1, self._r2) # git.Diff[]
        unified_diff = ''.join(d_list) 
            

    value = property(get_value)