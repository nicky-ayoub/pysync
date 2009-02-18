from pyvcal.resource import Resource

class File(Resource):
    """
	A snapshot of a versioned file.
	
	``repo``
		is the Repository
	
	``name``
		is the name in the filesystem
	
	"""
    def __init__(self, repo, name=None):
        super(File, self).__init__()
		self.repo = repo		
		self.name = name
		self.data = None
		self.size = None
		if self.repo.get_vcs() = GIT:
			# any git specific things that need to be done at init?

    
    def get_data(self):
        """Return a binary blob of the file contents"""
        raise NotImplementedError 
		

    data = property(get_data)