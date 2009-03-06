from pyvcal.resource import Resource

class Tree(Resource):
    """A versioned container of Files"""

    def __init__(self, tree_id, repo):
        # all we need is the hash and repo; we let gitpython do the rest
        super(Tree, self).__init__()
        self._tree_id = tree_id
        self._repo = repo
        self._contents = dict()

    def get_path(self):
        """Return the path to this tree in its container Repository"""
        raise NotImplementedError 
        
    def get_contents(self, recursive=True):
        """Return the immediate contents of a tree as a list of Resources."""
        # TODO: implement Resource.py
        raise NotImplementedError 
    
    
    
    path = property(get_path)
    contents = property(get_contents)
