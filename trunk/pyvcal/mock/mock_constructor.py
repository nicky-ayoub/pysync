import yaml

from repository import Repository

# maximum YAML length, currently set to 1 megabyte
MAX_YAML_LENGTH = 1048576

# keys to repository
REPOSITORY_KEY = 'repository'
REPOSITORY_PATH = 'path'
REPOSITORY_BRANCHES = 'branches'
REPOSITORY_REVISIONS = 'revisions'

def construct_repository(path):
    """ read_yaml takes a path to a yaml file """
    fsock = open(path)
    
    repository = None
    try:
        # read the entire file into yaml_string
        yaml_string = fsock.read(MAX_YAML_LENGTH)
        yaml_rep = yaml.load(yaml_string)
    
        # create repository object from YAML
        repository = process_repository(yaml_rep[REPOSITORY_KEY])
    
    finally:
        fsock.close()
        
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
    branches = get_value_default(repo_dict, REPOSITORY_BRANCHES, {})
    revisions = get_value_default(repo_dict, REPOSITORY_REVISIONS, [])
    
    return Repository(path, branches, revisions)
    