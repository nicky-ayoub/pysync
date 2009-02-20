import sys
import platform
import urllib
import tarfile

try:
    import P4
    print("Perforce python bindings already installed.")
    quit()
except ImportError, e:
    print("Perforce python bindings not installed.")


print("Downloading C API...")
PERFORCE_FTP_URL = "ftp://ftp.perforce.com/perforce/"
PERFORCE_API_VERSION = "r08.2"

def perforce_c_api_identifier():
    """
    Perforce's internal identifier for the client platform.
    """

    return sys.platform + \
        {
        'i386' : "80x86",
        'i686' : "6x86",
        }[platform.machine()] + \
        {
        '32bit' : "",
        }[platform.architecture()[0]]

# TODO Generalize to Windows
C_API_FILENAME = "p4api.tgz"

def perforce_c_api_location():
    return "%(ftp_root)s%(version)s/bin.%(platform)s/%(filename)s" % {
        "ftp_root" : PERFORCE_FTP_URL,
        "version" : PERFORCE_API_VERSION,
        "platform" : perforce_c_api_identifier(),
        "filename" : C_API_FILENAME
        }
        

# TODO Automated tests that work across platoforms

retrieved_c_api_filename = urllib.urlretrieve(perforce_c_api_location(), C_API_FILENAME)[0]

print("Extracting C API...")
tarfile.open(name=retrieved_c_api_filename).extractall()

# TODO Compile extracted files

# Get Python API
print("Downloading Python API...")

PYTHON_API_FILENAME = "p4python.tgz"

def perforce_python_api_location():
    return "%(ftp_root)s%(version)s/tools/%(filename)s" % {
        "ftp_root" : PERFORCE_FTP_URL,
        "version" : PERFORCE_API_VERSION,
        "filename" : PYTHON_API_FILENAME
    }


retrieved_python_api_filename = urllib.urlretrieve(perforce_python_api_location(), PYTHON_API_FILENAME)[0]
print("Extracting Python API...")
tarfile.open(name=retrieved_python_api_filename).extractall()

# TODO Fix up p4python setup.cfg
# TODO invoke setup.py to install the python api
