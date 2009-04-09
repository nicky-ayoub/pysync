import yaml

from repository import Repository
from branch import Branch

# maximum YAML length, currently set to 1 megabyte
MAX_YAML_LENGTH = 1048576

# keys to repository
REPOSITORY_KEY = 'repository'
REPOSITORY_BRANCHES = 'branches'
REPOSITORY_PATH = 'path'
REPOSITORY_REVISIONS = 'revisions'

# keys to branch
BRANCH_KEY = 'branches'
BRANCH_HEAD = 'head'

def construct_repository(path, key=None):
    """ read_yaml takes a path to a yaml file """
    fsock = open(path)
    
    repository = None
    try:
        # read the entire file into yaml_string
        yaml_string = fsock.read(MAX_YAML_LENGTH)
        yaml_rep = yaml.load(yaml_string)
    
        # create repository object from YAML
        repository = process_repository(yaml_rep[REPOSITORY_KEY])
        process_branch(yaml_rep[BRANCH_KEY], repository)
    
    finally:
        fsock.close()
    
    if key:
        return repository[key]
    else:
        return repository

def get_value_default(dict, key, default):
    """ Returns dict[key] if exists, otherwise returns default """
    if key in dict:
        return dict[key]
    
    # otherwise return default
    return default

def process_repository(repo_dict):
    """ Takes a dictionary containing keys: path, branches and revisions and 
    returns a Repository object. This method should only be called by 
    read_yaml. """
    path = repo_dict[REPOSITORY_PATH]
    revisions = get_value_default(repo_dict, REPOSITORY_REVISIONS, [])

    branches = {}
    # if the fixture does have branches defined, set them to be None
    if REPOSITORY_BRANCHES in repo_dict:
        for branch_name in repo_dict[REPOSITORY_BRANCHES]:
            branches[branch_name] = None
    
    return Repository(path, branches, revisions, True)

def process_branch(branch_dict, repo):
    """ Takes a dictionary that has branch names as keys. This method sets
    branches created in """
    for branch_name in branch_dict:
        branch = branch_dict[branch_name]
        repo.get_branches()[branch_name] = Branch(branch[BRANCH_HEAD], branch_name)
    
    