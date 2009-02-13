class FileDiff(object):
    """The set of changes needed to transform one revision of a file to another."""
    def __init__(self):
        super(FileDiff, self).__init__()
    
#    def apply_to(self, file):
#        """Apply this FileDiff to a File and return the transformed file."""
#        raise NotImplementedError 