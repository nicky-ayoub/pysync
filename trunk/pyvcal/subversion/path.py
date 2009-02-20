from subvertpy import repos, ra, NODE_DIR, NODE_FILE

class Path(object):
    """ A path to a versioned resource """
    def __init__(self, revision=None, branch_path=None, node_path=None):
        super(Path, self).__init__()

        self._branch_path = branch_path
        self._node_path = node_path
        self._revnum = revision
    
    def get_resource(self, revision, branch_path=None, node_path=None):
        """ Return the versioned resource at this path at the given revision or None """

        kind = ra_api.check_path(os.path.join(self._branch_path, self._node_path), self._revnum)

        kinds = {NODE_FILE: File, NODE_DIR: Tree}

        if kind in kinds:
            return kinds[kind](self._branch_path, self._node_path, ra_api, self._revnum)
        else:
            return None

    resource = property(get_resource)


    """ dir_contents[branch_node_path] = Resource.get(self.ra_api,
                                          self.rev,
                                          self.branch_path,
                                          branch_node_path) """


