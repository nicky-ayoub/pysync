from __future__ import with_statement

from .revision import Revision

import P4



class Repository(object):    
    def __init__(self, user=None, password=None, host=None, port=str(1666), client=None, cwd=None):
        super(Repository, self).__init__()
        
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._client = client
        self._cwd = cwd

    def _init_client(self):
        return P4Client(self._user, self._password, self._host, self._port, self._client, self._cwd)

    def get_uri(self):
        """Return the URI of the repository"""
        with self._init_client() as p4c:
            return p4c.host + ":" + p4c.port
        
    def get_branches(self):
        """Return the branches available in the repository"""
        raise NotImplementedError 
        
    def get_revisions(self):
        """Return the Revision objects available in this repository"""
        with self._init_client() as p4c:
            raw_changes = p4c.run("changes")
            raw_revisions = [Revision(c) for c in raw_changes]
            result = {}
            for r in raw_revisions:
                result[r.properties.revision_id] = r   
            return result
            

    uri = property(get_uri)
    branches = property(get_branches)
    revisions = property(get_revisions)

    @classmethod
    def create(cls,**kwargs):
        """Create a new Repository and return it."""
        raise NotImplementedError

class P4Client(object):
    """
    with P4Client(user, password, host, port , client, cwd) as p4c:
        p4c.do_stuff()
    """
    
    def __init__(self, user, password, host, port, client, cwd):
        """Initializes a P4 object"""
        self._p4c = P4.P4()
        
        if user:
            self._p4c.user = user
        if host:
            self._p4c.host = host
        if port:
            self._p4c.port = port
        if client:
            self._p4c.client = client
        if cwd:
           self._p4c.cwd = cwd
        self._password = password
        
    def __enter__(self):
        """Connects a P4 object"""
        self._p4c.connect()
        if self._password:
            self._p4c.login(self._password)
        return self._p4c
    
    def __exit__(self, type, value, traceback):
        """Tear down the P4 object"""
        self._p4c.disconnect()

    @property
    def host(self):
        return self._p4c.host
        
    @property
    def port(self):
        return self._p4c.port

