# Introduction #

We we want some common version control workflows and implement them in each supported version control system for testing.

We'll also need a couple repositories for system-specific tests.

# Details #

### Test 1 ###
  1. Empty Repository
  1. Set a property on root folder

### Test 2 ###
  1. Create empty file "README.txt"
  1. Add "Hello, world" in UTF-8 to README.txt
  1. Rename README.txt to README
  1. Delete README

### Test 3 ###
  1. Create directory 'dir/' and put empty file 'file' in it

### Test 4 ###
  1. Add a valid .png file (with and without extension) and other difficult-to-recognize binary blob file in root folder

### Test 5 ###
  1. Create a file 'fruit.txt' with contents
```
apple
banana
cherry
```
  1. Create branch with contents
```
apple
banana
cherry
date
```
  1. In trunk, modify to
```
apples
bananas
cherry
```
  1. Merge branch into trunk

### Test 6 ###
  1. Create empty file 'file.txt'
  1. Create branch with additional file 'new.txt'
  1. In trunk, modify 'file.txt' to add text "All your rebase"
  1. In branch, pull in the trunk change
  1. In branch, modify 'file.txt' to append text "are belong to us"
  1. Merge branch into trunk

## Subversion only ##

### Test SVN1 ###
  1. Repository with branches/, tags/, trunk/,

### Test SVN2 ###
  1. Repository without branches/, tags/, trunk/