"""
This module represents an interface to a version control system.
Except get_api, the code is not intended to be run---it is documentation in 
Python syntax.

For usage information for get_api(), see USAGE_STRING.

Version control system api implementors should copy the following import 
statements which allow a user of get_api() to use e.g. 

get_api(...).Repository

"""

from branch import Branch
from file import File
from filediff import FileDiff
from path import Path
from repository import Repository
from revision import Revision
from revisiondiff import RevisionDiff
from revisionproperties import RevisionProperties
from tree import Tree
from user import User

import perforce, subversion, git_wrapper as git

USAGE_STRING = """
Usage: vcs_api = pyvcal.get_api('<vcs>')
         where <vcs> can be:
         - git
         - subversion
         - perforce

"""

def get_api(system):
    try:
        vcs = {
            'git' : git,
            'subversion' : subversion,
            'perforce' : perforce
        }[system]
    except KeyError, e:
        raise ValueError(USAGE_STRING)

    return vcs

