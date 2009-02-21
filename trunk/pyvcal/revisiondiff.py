class RevisionDiff(object):
    """The set of changes needed to transform one revision into another."""

class NullRevisionDiff(RevisionDiff):
    """A fake diff"""
        


class MultipleParentNullRevisionDiff(NullRevisionDiff):
    """A fake diff for when a revision doesn't have a unique parent."""
    
