by Aran

# Introduction #
Dozens of version control systems exist. Most are open-source. I believe that the creation of a new system likely implies perceived fundamental architectural flaws in all previous systems. These architectural differences are interesting for pysync.

This document includes my notes as I explore the world of existing version control systems and the reasons for their creation.

## Why new version control systems probably represent changes in architecture ##

Each time a new version control system was created, one of the following scenarios is likely:

  1. An entrepreneur detected an opportunity to offer a proprietary advantage that would be hard to duplicate in competing systems
  1. A talented developer or group of developers wished for some functionality that was
    1. Not present in existing systems,
    1. Easier to create in a new system than in existing systems

All scenarios require difficulty of adding functionality to existing systems. This in turn implies a high cost of change, which implies fundamental architectural differences.

# History #

## SCCS ##
The [Source Code Control System](http://en.wikipedia.org/wiki/Source_Code_Control_System) [(paper)](http://basepath.com/aup/talks/SCCS-Slideshow.pdf) was the first version control system.

It only versions individual files. Its revision storage format is also used by bitkeeper and is not widely supported. It is called "interleaved deltas." The time to reconstruct any revision is proportional to the total size of all revisions. Branches on the latest revision of a file are supported (called "Releases"). Merging is not.

## RCS ##
The [Revision Control System](http://en.wikipedia.org/wiki/Revision_Control_System) [(html paper)](http://agave.garden.org/~aaronh/rcs/tichy1985rcs/html/) was created as a free successor to SCCS. It ended SCCS's dominance. Like SCCS it only operates on individual files. The fundamental unit of storage is called a "revision group." RCS supports branches within a file. It also allows merges. Locking is the only mechanism for conflict prevention. RCS commands are configured to a particular RCS file; collaboration is implemented by multiple Unix users' command-sets having access to the same file.

RCS storage on the mainline uses reverse deltas: The latest revision is stored intact but earlier revisions are (re)stored as deltas from the latest. On branches, revisions are stored as forward deltas. Thus, checking out branches is slow. Example:

Main line of code has 100 revisions. There is a branch at [revision 10](https://code.google.com/p/pysync/source/detail?r=10). This branch has 80 revisions. To check out the branch tip, RCS must: 1. Retrieve mainline [revision 100](https://code.google.com/p/pysync/source/detail?r=100); 2. Retrieve and apply reverse deltas from 99 down to 10; 3. Retrieve and apply 80 forward deltas on the branch.

RCS uses a clever algorithm called a piece table for storage. Piece tables are faster than interleaved deltas and thus RCS was faster than SCCS.

RCS uses an access list of Unix users for guarding writes.

When RCS was created, competitors included: IBM CLEAR/CASTER, AT&T SCCS (already discussed), CMU Software Development Control system and DEC Code Management System. At this time, Configuration Management was meaningfully different from Version Control. Configuration Management asks the question "Which group of revisions goes together to make a build?" MAKE and its ilk were the main answers to this. Version Control asks the question "How will we efficiently store changes to our files?"

This was an interesting distinction to me, because before I read the RCS paper I didn't understand how configuration management differed from Fancy Word For Version Control. Our modern way of storing repositories revisions as coherent sets of files is apparently obvious only in retrospect.

## CVS ##

[Concurrent Version System](http://www.nongnu.org/cvs/) [(paper)](http://grosskurth.ca/bib/1986/grune.pdf) is the earliest version control system I recognize (and I've used). It was originally a set of scripts operating over sets of RCS-controlled files. It achieved dominance after RCS.

CVS casts operations on groups of files as a series of operations on individual files.

Quoth the PRCS paper,
> "CVS cannot reconstruct change numbers from its repository. Since CVS treats each operation as a group of operations on individual RCS files in the repository, information such as this can only be obtained by check-in-time clustering or by carefully applying an immutable label at each commit. The issue of labeling each change to the project is of great importance. Without these labels, later reconstruction of the project's history is not as straight-forward as one might think. For example, with CVS it is difficult to request an operation such as display all changes made by user A during his last commit. One must examine the logs of all affected files, search for changes by user A and then request a list of all differences in the project between some time before and some time after the commit occurred."

and,

> "In CVS, branching is accomplished by first creating a label for the branch point, which is then used to name the new branch. Each file in the repository must be tagged with the new label---expensive for a large repository."

CVS allows client/server interaction with a repository.

## SVN ##
SVN aims to be "CVS done right." It re-architected CVS on a solid modern foundation without the baggage of CVS's long history.

  * Something about 1.5's merge assistance.
  * Something about CVS weaknesses SVN addresses
  * Something about svn:externals
  * SVN architecture

## SVK ##
[SVK](http://svk.elixus.org/) is a set of Perl programs that turn SVN into a distributed version control system.


## Piston ##
[Piston](http://piston.rubyforge.org/)

## BitKeeper ##
  * Why did Linux use this before Git?


## Git ##
  * Extended research here


## Mercurial ##
  * vs. git
  * something about revlogs

## Darcs ##
  * Something about theory of patches

## CodeVille ##
  * Something about a novel merging algorithm

## Monotone ##
  * Something about rosters...


## GNU Arch ##
## ArX ##
  * Why the fork?
## GNU Bazaar ##
  * Why the fork?


Maybes...
## PRCS ##
[Project Revision Control System](http://prcs.sourceforge.net/) ([paper](http://prdownloads.sourceforge.net/prcs/scm98.pdf))

Seems to be an attempt to be "CVS done better." Similar approach to Perforce, of keeping a database of project metainfo, though PRCS just uses a text file.

## CVSNT ##

## OpenCVS ##

## DCVS ##

## AccuRev ##

## Perforce ##
Uses RCS format for revision storage!

## Visual Sourcesafe ##
## SourgeGear Vault ##
  * Why the replacement?

## CMVC ##
  * Why replaced?
## Rational ClearCase ##

# Source Code APIs #
## Microsoft ##
## Eclipse ##
## DeltaV/WEBDAV ##

I've seen a Trac that was plugged into Git somewhere...

# Other Key Academic Publications About Version Control #
