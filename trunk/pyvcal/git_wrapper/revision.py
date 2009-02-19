class Revision(Revision):
    def __init__(self):
        super(Revision, self).__init__()
        

    
    def _get_id(self):
        return self.id
    
    def _set_id(self, id):
        self.id = id
        
    id = property(_get_id, _set_id) 