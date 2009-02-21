from revision import Revision

import os

from subvertpy import repos, ra, NODE_DIR, NODE_FILE

class RevisionDiff(object):
    """ The set of changes needed to transform one revision into another """

    def __init__(self, revision1=None, revision2=None):
        super(RevisionDiff, self).__init__()

        self._rev1 = revision1
        self._rev2 = revision2


class NullRevisionDiff(RevisionDiff):
    """ A fake diff """

    def __init__(self):
        super(NullRevisionDiff, self).__init__()
        

class MultipleParentNullRevisionDiff(NullRevisionDiff):
    """ A fake diff for when a revision doesn't have a unique parent """

    def __init__(self):
        super(MultipleParentNullRevisionDiff, self).__init__()

