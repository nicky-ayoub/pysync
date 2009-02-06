class RevisionDiff(object):
    """The set of changes needed to transform one revision into another."""
    def __init__(self):
        super(RevisionDiff, self).__init__()

class NullRevisionDiff(RevisionDiff):
    """A fake diff"""
    def __init__(self):
        super(NullRevisionDiff, self).__init__()
        


class MultipleParentNullRevisionDiff(NullRevisionDiff):
    """A fake diff for when a revision doesn't have a unique parent."""
    def __init__(self):
        super(MultipleParentNullRevisionDiff, self).__init__()

