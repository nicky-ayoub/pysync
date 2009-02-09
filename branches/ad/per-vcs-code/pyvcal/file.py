from pyvcal.resource import Resource

class File(Resource):
    """A snapshot of a versioned file."""
    def __init__(self):
        super(File, self).__init__()
    
    def data(self):
        """Return a binary blob of the file contents"""
        raise NotImplementedError 
