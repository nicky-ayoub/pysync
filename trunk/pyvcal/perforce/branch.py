## \brief  A coherent set of data that evolve together
class Branch(object):
    """A coherent set of data that evolves together.
    
    A PyVCAL branch maps to a Perforce codeline.
    
    We assume that each branch gets a folder under the depot root.
    """
    
    def get_head(self):
        """Return the latest Revision in the branch"""
        raise NotImplementedError 
        
    def get_name(self):
        """Return the user-defined name of the branch"""
        return self._name

    def __init__(self, name=None):
        super(Branch, self).__init__()
        self._name = name

    ## The latest revision in the branch.
    head = property(get_head)
    
    ## The user-specified name of the branch.
    name = property(get_name)
