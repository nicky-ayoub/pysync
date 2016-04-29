# Introduction #

Branching requires a view that includes branches/and trunk/ but everyday work just uses trunk.

# Details #

I have a folder /Users/aran/Projects/.

Under projects, there are two subfolders, pyvcal and pyvcal-all.

pyvcal is a checkout of trunk, via

```
svn checkout https://pysync.googlecode.com/svn/trunk/ pyvcal --username aran.donohue
```

pyvcal-all is a checkout of the root of the repository via

```
svn checkout https://pysync.googlecode.com/svn/ pyvcal-all --username aran.donohue
```

For everyday work, I live in Projects/pyvcal

To branch, I use pyvcal-all.

```
Projects aran$ cd pyvcal-all/
pyvcal-all aran$ svn up
U    trunk/README.txt
A    trunk/pyvcal/RevisionProperties.py
U    trunk/pyvcal/revision.py
U    trunk/pyvcal/file.py
U    trunk/pyvcal/tree.py
A    trunk/pyvcal/resource.py
Updated to revision 55.
pyvcal-all aran$ svn cp trunk/ branches/ad/per-vcs-code
A         branches/ad/per-vcs-code
pyvcal-all aran$ svn ci -m "Create branch to test per-vcs-code."
Adding         branches/ad/per-vcs-code

Committed revision 56.
pyvcal-all aran$ cd ../pyvcal
pyvcal aran$ svn up
At revision 56.
pyvcal aran$ svn sw https://pysync.googlecode.com/svn/branches/ad/per-vcs-code
 U   .
Updated to revision 56.
pyvcal aran$ cd pyvcal/
pyvcal aran$ svn mkdir perforce
A         perforce
pyvcal aran$ svn mkdir git
A         git
pyvcal aran$ svn mkdir subversion
A         subversion
pyvcal aran$ touch perforce/__init__.py
pyvcal aran$ touch git/__init__.py
pyvcal aran$ touch subversion/__init__.py
pyvcal aran$ svn add git/*.py
A         git/__init__.py
pyvcal aran$ svn add perforce/*.py
A         perforce/__init__.py
pyvcal aran$ svn add subversion/*.py
A         subversion/__init__.py
pyvcal aran$ svn status
A      git
A      git/__init__.py
A      subversion
A      subversion/__init__.py
A      perforce
A      perforce/__init__.py
pyvcal aran$ svn commit -m "Attempt to commit to a branch."
Adding         pyvcal/git
Adding         pyvcal/git/__init__.py
Adding         pyvcal/perforce
Adding         pyvcal/perforce/__init__.py
Adding         pyvcal/subversion
Adding         pyvcal/subversion/__init__.py
Transmitting file data ...
Committed revision 57.
pyvcal aran$ 

```

Now I can work in pyvcal, my usual directory, but commit to a branch.