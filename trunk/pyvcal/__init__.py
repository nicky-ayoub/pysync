import perforce, subversion, git_wrapper as git

USAGE_STRING = """
Usage: vcs_api = pyvcal.get_api(<arguments>)

General arguments:
  - vcs: Specify the vcs type from 'git', 'svn', 'perforce'. (required)

Git arguments:

Subversion arguments:

Perforce arguments:

"""

def get_api(**kwargs):
    vcs = None
    
    if not 'vcs' in kwargs:
        print "Must specify vcs."
        print USAGE_STRING
        return vcs

    if kwargs['vcs'] == 'git':
        vcs = git
    elif kwargs['vcs'] == 'svn':
        vcs = subversion
    elif kwargs['vcs'] == 'perforce':
        vcs = perfoce
    else:
        print "Invalid vcs type: ", kwargs['vcs']
        print USAGE_STRING

    vcs.SETTINGS = kwargs
    
    return vcs

