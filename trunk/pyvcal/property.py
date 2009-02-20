class Properties(object):
    """Properties of a versioned object"""
    def __init__(self):
        super(Properties, self).__init__()
        
class ResourceProperties(Properties):
    """Properties of a versioned object"""
    def __init__(self):
        super(Properties, self).__init__()

class FileProperties(ResourceProperties):
    """The properties of a File"""
    def __init__(self):
        super(FileProperties, self).__init__()

class TreeProperties(ResourceProperties):
    """The properties of a Tree"""
    def __init__(self):
        super(TreeProperties, self).__init__()
        
