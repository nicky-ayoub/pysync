from unittest import TestSuite

from git import test_git
from perforce import test_perforce
from subversion import test_subversion

test_all = TestSuite([test_git, test_perforce, test_subversion])
