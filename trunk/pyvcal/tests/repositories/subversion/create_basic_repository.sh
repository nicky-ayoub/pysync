reponame="svn-merge-branch"

mkdir $reponame
cd $reponame

# Creating a repository in this location
svnadmin create . 

svn_path=`pwd`

cd ../
mkdir repo05
cd repo05/

# Checking out the repository
svn co file://$svn_path

# Going into the repo dir
cd $reponame

# Adding branches/ trunk/ and tags/
mkdir branches/
mkdir tags/
mkdir trunk/

# add initial commit with empty README.txt
touch README.txt
svn add README.txt
svn ci -m "initial commit" README.txt

# put something into README.txt
echo "Hello world" > README.txt
svn ci -m "Edited README.txt" README.txt

# rename README.txt to README
svn move README.txt README 
svn ci -m "Rename README.txt to README"

# delete README
svn delete README
svn ci -m "Delete README"


cd ../ # back out of svnrepo01

