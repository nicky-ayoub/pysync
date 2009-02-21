mkdir svnrepo01
cd svnrepo01/

# Creating a repository in this location
svnadmin create . 

svn_path=`pwd`

cd ../
mkdir repo01
cd repo01/

# Checking out the repository
svn co file://$svn_path

# Going into the repo dir
cd svnrepo01/

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

