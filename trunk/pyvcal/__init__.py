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
    if not 'vcs' in kwargs:
        raise ValueError(USAGE_STRING)
    
    try:
        vcs = {
            'git' : git,
            'svn' : subversion,
            'perforce' : perforce
        }[kwargs['vcs']]
    except KeyError, e:
        raise ValueError(USAGE_STRING)

    vcs.SETTINGS = kwargs
    
    return vcs

