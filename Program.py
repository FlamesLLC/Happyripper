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

    ## Sync a .apk file with android service and extract the contents to your /Documents folder

    varAPK=input("Please your .apk file path: ")
    if varAPK == "":
        print("Please enter a valid path")
        sys.exit()
    else:
        zipfile=varAPK+"_apk.zip.".extract.all()
        print("Extracting contents to " + zipfile)
        print("Sync to the Documents folder")
        ## extract varAPK png files to documents folder
        extractAPKPictuesToDocument=input("Please your .apk file path: ")
        if extractAPKPictuesToDocument == "":
            print("Please enter a valid path")
            sys.exit()
        else:
            print("Extracting contents to " + extractAPKPictuesToDocument)
            print("Sync to the Documents folder")
            ## extract varAPK jpeg files to documents folder
            extractAPKPictuesToDocument=input("Please your .apk file path: ")
            if extractAPKPictuesToDocument == "":
                print("Please enter a valid path")
                sys.exit()
            else:
                print("Extracting contents to " + extractAPKPictuesToDocument)
                print("Sync to the Documents folder")
                ## extract varAPK jpeg files to documents folder
                extractAPKPictuesToDocument=input("Please your .apk file path: ")
                if extractAPKPictuesToDocument == "":
                    print("Please enter a valid path")
                    sys.exit()
                else:
                    print("Extracting contents to " + extractAPKPictuesToDocument)
                    print("Sync to the Documents folder")
                    ## extract varAPK jpeg files to documents folder
                    extractAPKPictuesToDocument=input("Please your .apk file path: ")
                    if extractAPKPictuesToDocument == "":
                        print("Please enter a valid path")
                        sys.exit()
                    else:
                        print("Extracting contents to " + input("Enter folder you would like to extract to "))
                        print("Sync to the Documents folder")
                        ## extract varAPK jpeg files to documents folder
                        extractAPKPictuesToDocument=input("Please your .apk file path: ")
                        if extractAPKPictuesToDocument == "":
                            print("Please enter a valid path")
                            sys.exit()
                        else:
                            print("Extracting contents to " + extractAPKPictuesToDocument)
                            print("Sync to the Documents folder")
                            ## extract varAPK jpeg files to documents folder
                            extractAPKPictuesToDocument=input("Please your .apk file path: ")
                            if extractAPKPictuesToDocument == "":
                                print("Please enter a valid path")
                                sys.exit()
                            else:
                                print("Done!")
                                sys.exit()