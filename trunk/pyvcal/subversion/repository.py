#from pyvcal.subversion import branch as ibranch
import os
from datetime import datetime
from subvertpy import repos, ra, NODE_NONE, NODE_DIR, NODE_FILE

class Repository(object):

	def __init__(self, path=None):
		""" Constructor for the SVN Repository object """
		super(Repository, self).__init__()

		self.path = path

	def get_uri(self):
        	""" Return the URI of the repository """
		self.connect(self.path)
		return self.ra_api.get_repos_root()
	
	def connect(self, path):
		""" Given a path, then connect to that path """
		self.path = path
		self.ra_api = ra.RemoteAccess(self.path)

	def get_revision(self):
		""" Return a dictionary of Revision objects where the key is the revision_id 
		and the value is the actual Revision object """
		self.connect(self.path)
		rev_id = self.ra_api.get_latest_revnum()
		self._log(rev=rev_id)
	
	def get_branches(self):
		""" Return the branches available in the repository """
	        # assume: /trunk, /branches
	        """branch_dict = {}

	        # The first element in the top level info is the list of files
		file_list = _file_list('', self.ra_api)
	        if 'trunk' in file_list:
		        branch_dict['trunk'] = ibranch('trunk', self.ra_api)

		if 'branches' in file_list:
			branch_list = _file_list('branches', self.ra_api)
			for branch in branch_list:
				branch_dict[branch] = ibranch(('branches/' + branch), self.ra_api)
		return branch_dict"""
		pass
	
	""" Helper methods for this class """
	def _log(self, path='', rev=None):
		""" Return a Revision object scoped to path with revision id as rev """
		rev = rev or self.ra_api.get_latest_revnum()
	    	log_path = path # may need to join it with the current branch's path?
		
		# dictionary containing the revisions of the repository as key-value pairs, where the key is the revision_id 
		# and the value would be a Revision object.
		revision_dict = {}

	        def cb(paths, revnum, props, has_children=False):
				paths = paths or {}
				revision_dict[revnum] = Revision(revnum,
                                       props.get('svn:author', ''),
                                       props.get('svn:log', ''),
                                       datetime.strptime(
                                               props['svn:date'].split('.')[0],
                                               "%Y-%m-%dT%H:%M:%S"),
                                       paths.keys(),
                                       self.ra_api,
                                       log_path)

	        self.ra_api.get_log(callback=cb, paths=[log_path],
                            start=0, end=rev,
                            discover_changed_paths=True,
                            revprops=["svn:date", "svn:author", "svn:log"])

        	return revision_dict

	uri = property(get_uri)
	branches = property(get_branches)
	revisions = property(get_revision)
