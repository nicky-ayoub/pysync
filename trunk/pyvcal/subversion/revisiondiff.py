from filediff import FileDiff

import os

from subvertpy import repos, ra, NODE_DIR, NODE_FILE

class RevisionDiff(object):
    """ The set of changes needed to transform one revision into another """

    def __init__(self, revision1=None, revision2=None):
        super(RevisionDiff, self).__init__()
        
        self._rev1 = revision1
        self._rev2 = revision2
        
    def get_diff():
        resource1 = self._rev1.get_resource()
        resource2 = self._rev2.get_resource()
        
        if resource1.is_file() and resource2.is_file(): 
            return FileDiff(resource1, resource2)
            

class NullRevisionDiff(RevisionDiff):
    """ A fake diff """

    def __init__(self, null_rev=None):
        super(NullRevisionDiff, self).__init__()
        
        self.null_rev = null_rev
        

class MultipleParentNullRevisionDiff(NullRevisionDiff):
    """ A fake diff for when a revision doesn't have a unique parent """

    def __init__(self, null_rev=None):
        super(MultipleParentNullRevisionDiff, self).__init__()
        
        self.null_rev = NullRevisionDiff(null_rev)

