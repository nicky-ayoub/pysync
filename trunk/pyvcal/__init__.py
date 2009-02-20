import perforce, subversion, git_wrapper as git

USAGE_STRING = """
Usage: vcs_api = pyvcal.get_api('<vcs>')
         where <vcs> can be:
         - git
         - svn
         - perforce

"""

def get_api(system):
    try:
        vcs = {
            'git' : git,
            'svn' : subversion,
            'perforce' : perforce
        }[system]
    except KeyError, e:
        raise ValueError(USAGE_STRING)

    return vcs

