import os

from subvertpy import repos, ra, NODE_DIR, NODE_FILE

class RevisionDiff(object):
    """ The set of changes needed to transform one revision into another """

    def __init__(self, revision1=None, revision2=None):
        super(RevisionDiff, self).__init__()
        
        self._rev1 = revision1
        self._rev2 = revision2
        
    def get_value():
        """Concatenation of Unified Diffs of resources between the revisions."""
        raise NotImplementedError 

    def get_diff():
        resource1 = self._rev1.get_resource()
        resource2 = self._rev2.get_resource()
        
    value = property(get_value)

