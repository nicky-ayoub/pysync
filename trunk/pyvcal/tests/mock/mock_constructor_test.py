import mock.mock_constructor as mc
import unittest
import yaml

def load_yaml(path, test_name):
    """ Convenience method for writing test cases. This will convert a string 
    in YAML syntax into a python object """
    fsock = open(path)
    
    try:
        yaml_string = fsock.read()
        yaml_obj = yaml.load(yaml_string)
        
    finally:
        fsock.close()

    return yaml_obj[test_name]

class Mock_Constructor_Test(unittest.TestCase):
    
    def test_process_repository_basic(self):
        repo_dict = load_yaml('test_fixtures.yaml', 'test1')
        repo = mc.process_repository(repo_dict[mc.REPOSITORY_KEY])
        
        self.assertEquals({}, repo.get_branches())
        self.assertEquals([], repo.get_revisions())
        self.assertEquals('http://www.somesvnpath.com/svn', repo.get_uri())
        
    def test_process_repository(self):
        repo_dict = load_yaml('test_fixtures.yaml', 'test2')
        repo = mc.process_repository(repo_dict[mc.REPOSITORY_KEY])
        
        self.assertEquals({'branch1': 'None', 'branch2': 'None'}, repo.get_branches())
        self.assertEquals([], repo.get_revisions())
        self.assertEquals('http://www.somesvnpath.com/svn2', repo.get_uri())
        
    def test_process_repository_with_revisions(self):
        repo_dict = load_yaml('test_fixtures.yaml', 'test3')
        repo = mc.process_repository(repo_dict[mc.REPOSITORY_KEY])
        
        self.assertEquals({'branch1': 'None', 'branch2': 'None'}, repo.get_branches())
        self.assertEquals(['revision1', 'revision2'], repo.get_revisions())
        self.assertEquals('http://www.somesvnpath.com/svn3', repo.get_uri())
        
        