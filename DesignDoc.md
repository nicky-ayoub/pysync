### Overview ###
pysync is a Python library that allows a user to perform common version control actions using one API across multiple version control systems (VCS). pysync favors compatibility over preserving features of a specific VCS.

The motivation behind pysync is to ease development on other Python applications which rely on access to version control. pysync would enable them to support a wider variety of VCSs.

Over the course of development we will aim to at first enable "read" actions across multiple VCS'. After this first milestone we will expand to core APIs needed for a hypothetical bare-bones generic CLI client.

### Project Requirements ###
pysync will be the single layer used by projects such as Basie to access a source code repository regardless of the VCS used to manage that repository. Basie would only access pysync's read-only APIs but we hope to expand the pysync module to include commonly used actions which "write" to a repository.