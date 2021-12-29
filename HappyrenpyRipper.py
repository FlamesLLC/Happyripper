##  The following code is for extract renpy game data from the game folder. and  sonud, images and code. and then it covnerts it to a log file with
## that has the original data. and then it can be used to rip the game.

print("Welcome to happyrenpyRipper.py")
print("This is a tool for ripping the game data from the game folder.")
print("This tool is for renpy game only.")
## use a shell command to cat -x and extract the data. from a selected .rpy file
## and then use the data to create a .dat file

import os
import re
import shutil
import sys
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import logging
import logging.handlers
import traceback
import zipfile
import tarfile
import shutil
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import sys
import os
import shutil
import re
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import sys
import os
import shutil
import re
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import sys
import os
import shutil
import re
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import sys
import os
import shutil
import re
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import sys
import os
import shutil
import re
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import sys
import os
import shutil
import re
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
import sys
import os
import shutil
import re
import subprocess
import zipfile
import tarfile
import glob
import time
import datetime
import platform
import hashlib
import struct
import json
import codecs
import argparse
zipfile.ZipFile.namelist = lambda self: [n for n in self.namelist() if n.endswith('/')]
zipfile.ZipFile.extractall = lambda self, path=None, members=None, pwd=None: extractall(self, path, members, pwd)
zipfile.ZipFile.extract = lambda self, member, path=None, pwd=None: extract(self, member, path, pwd)

 

zipfile.ZipFile.read = lambda self, name: self.open(name).read()
zipfile.ZipFile.extract = lambda self, name: self.extract(name, path=os.path.dirname(name))
zipfile.ZipFile.extractall = lambda self, path: self.extractall(path)
tarfile.TarFile.namelist = lambda self: [n for n in self.getnames() if n.endswith('/')]
tarfile.TarFile.read = lambda self, name: self.extractfile(name).read()
tarfile.TarFile.extract = lambda self, name: self.extract(name, path=os.path.dirname(name))
tarfile.TarFile.extractall = lambda self, path: self.extractall(path)
zipfile.ZipFile.extract = lambda self, name: self.extract(name, path=os.path.dirname(name))
zipfile.ZipFile.extractall = lambda self, path: self.extractall(path)
zipfile.ZipFile.read = lambda self, name: self.open(name).read()
zipfile.ZipFile.namelist = lambda self: [n for n in self.namelist() if n.endswith('/')]
zipfile.ZipFile.extract = lambda self, name: self.extract(name, path=os.path.dirname(name))
zipfile.ZipFile.extractall = lambda self, path: self.extractall(path)
tarfile.TarFile.extract = lambda self, name: self.extract(name, path=os.path.dirname(name))
tarfile.TarFile.extractall = lambda self, path: self.extractall(path)
tarfile.TarFile.read = lambda self, name: self.extractfile(name).read()
tarfile.TarFile.namelist = lambda self: [n for n in self.getnames() if n.endswith('/')]

 

def create_logger(logger_name, log_file_name, log_level):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

 


##

print(create_logger("happyrenpyRipper", "data.FT", logging.DEBUG))


# global variables
