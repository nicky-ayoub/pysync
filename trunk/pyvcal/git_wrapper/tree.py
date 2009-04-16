from pyvcal.resource import Resource

class Tree(Resource):
    """A versioned container of Files"""

    def __init__(self, tree_id, repo):
        # all we need is the hash and repo; we let gitpython do the rest
        super(Tree, self).__init__()
        self.tree_id = tree_id
        self.repo = repo
        self.path = Path(self.repo)
        
        self._contents = {}
        gitTree = self.repo.tree(self.tree_id)
        for i in gitTree.items():
            self._contents[i[0]] = i[1]

    def get_path(self):
        """Return the path to this tree in its container Repository"""
        return self.path
        
    def get_contents(self, recursive=True):
        """Return the immediate contents of a tree as a list of Resources."""
        return get_data(recursive)
    
    def get_data(self, recursive=True):
        return self._contents        
    
    def get(self, key):
        return self._contents.get(key)
    
    def items(self):
        return self._contents.items()
        
    def keys(self):
        return self._contents.keys()
    
    def values(self):
        return self._contents.values()
    
    path = property(get_path)
    contents = property(get_contents)
    