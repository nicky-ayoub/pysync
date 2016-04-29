PyVCAL supports Perforce.

To run PyVCAL against perforce, you need P4Python, the official Python bindings for perforce.

P4Python in turn depends on the Perforce C/C++ API.

P4Python is listed as an optional dependency on the PyVCAL egg. It should install itself when installing the PyVCAL egg. If it doesn't, you can `easy_install P4Python`. If this still doesn't work, you might need to install the Perforce C/C++ API for your platform. This is free to download from Perforce the company. Go to their website, accept their terms, and find the right package for your platform.

To run the PyVCAL tests (a must for any would-be PyVCAL developer) you also need p4d, the perforce server, somewhere on your path. This is also a platform-specific free download from the perforce web site.