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
        self.ra_api = self._rev1._get_ra_api()
        # getting the revision id of the element to be diffed.
        self.rev1_num = self._rev1.properties.revision_number
        self.rev2_num = self._rev2.properties.revision_number
        
        resource1 = self._rev1.get_resource()
        resource2 = self._rev2.get_resource()
        
        #raise NotImplementedError 
        #do_diff(self, revision_to_update, diff_target, versus_url, diff_editor, 
        #recurse=True, ignore_ancestry=False, text_deltas=False, depth=None)
        return self.ra_api.do_diff(self.rev1_num, self.rev2_num, resource2.full_path(), 
                                    diff_editor, recurse=True, ignore_ancestry=False, 
                                    text_deltas=False, depth=None)

    def get_diff():
        resource1 = self._rev1.get_resource()
        resource2 = self._rev2.get_resource()
        
    value = property(get_value)

