# Introduction #

Perforce is a centralized version control system. Of particular note:
  * The centralized server keeps track of client workspaces and even which files are open in the workspaces
  * Branches are directories but p4 keeps track of the origins of files
  * A depot is just a container for a numbered series of changesets.
  * A revision of a file is uniquely identified by a domain, depot, path and any of {changeset id, date, file revision #}. A revision of a file is connected to its many ancestors.
  * A job is a versioned blob of data. A jobspec defines the format of that blob. Jobs are meant to allow external tools such as bug trackers store their information in Perforce.
  * Perforce filespecs (not pictured) are a syntax for referring to perforce objects. A view uses filespecs to refer to file revisions, however, the filespec may not refer to a specific revision.
  * A workspace contains concrete versions of the files referred to by a view.

# Diagram #
![http://pysync.googlecode.com/svn/wiki/media/perforce.png](http://pysync.googlecode.com/svn/wiki/media/perforce.png)

Notational limitations prevent one-directional arrows.