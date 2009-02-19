import git, perforce, subversion

USAGE_STRING = """
Usage: vcs_api = pyvcal.get_api(<arguments>)

General arguments:
  - vcs: Specify the vcs type from 'git', 'svn', 'perforce'. (required)

Git arguments:

Subversion arguments:

Perforce arguments:

"""

def get_api(**kwargs):
    if not 'vcs' in kwargs:
        print "Must specify vcs."
        print USAGE_STRING
        return

    if kwargs['vcs'] == 'git':
        return git
    elif kwargs['vcs'] == 'svn':
        return subversion
    elif kwargs['vcs'] == 'perforce':
        return perfoce
    else:
        print "Invalid vcs type: ", kwargs['vcs']
        print USAGE_STRING

