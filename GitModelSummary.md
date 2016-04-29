Git is a distributed VCS. Centralized VCS is a special case of distributed VCS, where one repository is singled out as the 'canonical' repo. Conceptually it should be possible to emulate the behavior of a centralized VCS like SVN over git, but not vice versa.

The following is an ER diagram outlining the Git model.

![http://pysync.googlecode.com/files/git_ER_diagram2.png](http://pysync.googlecode.com/files/git_ER_diagram2.png)

### Some things of notice ###
Git uses universal public identifiers based off of a SHA1 hash off of file contents. This hash becomes the name of the blob used to store the file contents. It is used by trees to map the human-made filename (which is of course the same across multiple versions) to a specific version of that given file (the blob representing the file contents of that version). Trees store no version information; commit objects contain the state of the tree they point to (along with appropriate meta-data) as well as its parent commit. Therefore a series of commit objects represents a repository's version history.

ALL objects also have SHA1 hashes of them; trees, commits, tags. This is nice in that renaming and moving directories as well as files can be done without futzing the version history of that directory or file.


### Explanation of ER Diagram ###
**What's a tree?**
A tree is used to represent a directory in Git's filesystem model.

**Where do submodules fit in?**
A submodule is a foreign repository embedded within the contents of a git repository. It is represented by a special tree object called a 'gitlink'. This is noted in a record in .gitmodules within the root of the repository. The .gitmodules record assigns the logical name and URL associated with the submodule. (source: http://www.kernel.org/pub/software/scm/git/docs/git-submodule.html)

**Why can't Git represent subdirectories?**
As a consequence of Git's design, the atomic unit of checking out is the repo. Unlike SVN, there is no .git directory in every subdirectory of the root directory of the repo. There is a single .git directory at the root responsible for storing the repo/versioning information.

### What I've learned that might help someone understand Git if they understand SVN ###
In SVN, a working copy (ie. what's created when you do a svn co http://etcetcetc) is intended to be an imperfect mirror of what's in the central repository. A local working copy is unable to analyze or even read version history of anything without phoning home to the central repository. Git is different. Each working copy is itself a repository. It is possible to look up previous versions of a file if you are working entirely offline for example.

The primary stumbling block for myself was in understanding the pragmatic aspect of this design. If for example, a code freeze is imminent, whose repository is considered canonical? As far as I am able to tell (please edit of I am mistaken), the intended use of git in this example is to have all active repositories sync with each other (or have all repos sync with some easily-accessible "central" repository, emulating the SVN design) and either present this central repo as the canonical source or make it so that each developer's repo is identical. The implementation of merging in git is designed to make either approach feasible. In fact, much of the "fanboyism" surrounding git revolves around its focus as branches as working copies and working copies and branches and the ease with which one can merge branches.


### What this means for PySync/PyVCS/Our eventual project name ###
To support git invisibly alongside centralized VCS' like SVN, it seems to me (please discuss) that having our library handle git by emulating a SVN design is the easiest approach. We can design our library to revolve around a centralized repo (which ties in well with the concept of Basie as a project portal; a place where developers go to as opposed to something everyone has an independent copy of).

I believe that foregoing the bells and whistles that supporting true distributed VCS provides would lead to far too many headaches. Furthermore, I believe that simply getting our library working is our first priority. However, I also realize that building ourselves into a corner in the design phase is a potential problem. I have heard that there are extensions to svn to enable it to behave in a distributed manner but I'm unsure as to what extent perforce can do the same.


### Git in PyVCAL (formerly PySync) ###
Since I am a lazy bastard, the best way I've found to get my meaty hooks into Git from Python is to use someone else's meaty hooks; [GitPython](http://blog.michaeltrier.com/2008/5/8/gitpython). GitPython is an interface to Git from Python. It provides, from what I can tell, all the basic CRUD needed to interact with Git repositories. Since we aren't worried about advanced Git features, these basics are all we need for PyVCAL at the moment. It also provides a way to issue direct command-line queries to the Git binary for us to implement any advanced or custom features that aren't necessarily covered by GitPython's existing API.

This means that our Git-specific code simply has to call the appropriate GitPython's functions and convert the returning values to whatever abstract VCS-independent form we choose for PyVCAL.

API (pg15-22): http://pysync.googlecode.com/files/GitPython.pdf