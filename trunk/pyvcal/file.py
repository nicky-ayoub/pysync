class File(object):
    """A snapshot of a versioned file."""
    def __init__(self):
        super(File, self).__init__()
    
    def data(self):
        """Return a binary blob of the file contents"""
        raise NotImplementedError 
    def get_properties(self):
        """Return the properties of a file"""
        raise NotImplementedError 
        
