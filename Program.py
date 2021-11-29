###this is a ripper that rips png and jpeg files from ipa and apk files


import os
import sys
import zipfile
import shutil
import argparse
import subprocess
print("Syncing with the ipa file of your choice")
varipa=input("Please your .ipa file path: ")
if varipa == "":
    print("Please enter a valid path")
    sys.exit()
else:
    print("ERROR 404 NO IPA FOUND:")
    sys.exit()