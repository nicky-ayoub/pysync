SVN is a centralized VCS, meaning that only one master copy of the software is used.

<ul>
<blockquote><li> Subversion itself does not distinguish between a tag, a branch, and a directory<br>
</li>
<li> Natively client/server, layered library design.<br>
</li>
<li> The Subversion file system can be described as a three dimensional filesystem. Since most representations of a directory tree (e.g., tree view) are two dimensional, the added dimension is that of revisions. Each revision in a Subversion file system has its own root, which is used to access contents at that revision. Files are stored as links to the most recent change; thus a Subversion repository is quite compact.<br>
</li></blockquote>

<blockquote><li> The <i>svn:externals</i> property is that once it is set on a versioned directory, everyone who checks out a working copy with that directory also gets the benefit of the externals definition.<br>
</li>
<li> <i>svn:externals</i> can be set on any versioned directory, and its value is a multi-line table of subdirectories (relative to the versioned directory on which the property is set) and fully qualified, absolute Subversion repository URLs.<br>
</li>
<li> An externals definition can only point to directories, not files.<br>
</li>
<li> The externals definition cannot point to relative paths.<br>
</li>
<li>The working copies created via the externals definition support are still disconnected from the primary working copy.<br>
</li></blockquote>

<blockquote><li> Subversion provides interfaces for adding, modifying, and removing versioned metadata on each of your versioned directories and files ... <i>svn properties</i>
</li>
<li> Subversion uses the interfile branching model from Perforce to handle branches and tags.<br>
</li>
<li> An SVN working directory always contains two copies of each file: one for the user to actually work with and another hidden in .svn/ to aid operations such as status, diff and commit.<br>
</li>
<li> Subversion's revision numbers apply to entire trees, not individual files. Each revision number selects an entire tree, a particular state of the repository after some committed change. Another way to think about it is that revision N represents the state of the repository filesystem after the Nth commit.<br>
</li>
</ul></blockquote>


<b> I made a couple of basic ER diagrams showing the svn architecture </b>

<br />
![http://pysync.googlecode.com/files/svn_ER1.jpg](http://pysync.googlecode.com/files/svn_ER1.jpg)

<br />
<b> and its relationships: </b>
<br />
![http://pysync.googlecode.com/files/svn_er_diagram_.jpg](http://pysync.googlecode.com/files/svn_er_diagram_.jpg)