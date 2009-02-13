class Branch(object):
    """A coherent set of data that evolves together"""
    def __init__(self):
        super(Branch, self).__init__()
    
    def get_head(self):
        """Return the latest Revision in the branch"""
        raise NotImplementedError 
        
    def get_name(self):
        """Return the user-defined name of the branch"""
        raise NotImplementedError 
        
    head = property(get_head)
    name = property(get_name)