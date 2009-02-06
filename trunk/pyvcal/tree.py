class Tree(object):
    """A versioned container of Files"""
    def __init__(self):
        super(Tree, self).__init__()

    def get_path(self):
        """Return the path to this tree in its container Repository"""
        raise NotImplementedError 
        
    def get_contents(self, recursive=True):
        """Return the contents of a tree as a list of Paths."""
        raise NotImplementedError 