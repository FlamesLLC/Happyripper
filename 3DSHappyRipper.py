## rips the contents of a .cia file and extracts the models into the unreal egngine 5 api
## then converts the models into a .fbx file
## also grab user interface, hud, and code from the .cia file

print("Welcome to the 3DS Happy Ripper")
print("This program will rip the contents of a .cia file and extract the models into the unreal engine 5 api")
print("then converts the models into a .fbx file")
var3DSCIA=input("Please enter the name of the .cia file you wish to rip: ")
var3DSCIA=var3DSCIA.lower()
import os
import  sys
import zipfile 
import numpy as np
import shutil
print("Syncing with .cia file...")
def syncCIA(var3DSCIA):
    if os.path.exists(var3DSCIA):
        print("File found!")
        print("Extracting file...")
        with zipfile.ZipFile(var3DSCIA, 'r') as zip_ref:
            zip_ref.extractall()
            print("File extracted!")
            print("Syncing complete!")
    else:
        print("File not found!")
        print("Please try again!")
        sys.exit()

        print("Would you like to convert the .cia models into .fbx models using the Unreal Engine 5 API?")
        print("Please note that this will take a while!")
    extracted = zipfile.ZipFile(var3DSCIA, 'r')
    extracted.extractall()
    print("Extracted!")
    print("Would you like to convert the .cia models into .fbx models using the Unreal Engine 5 API?")
    print("Please note that this will take a while!")
    var3DSCIA=input("Please enter the name of the .cia file you wish to rip: ")
    var3DSCIA=var3DSCIA.lower()
    import os
    import  sys
    import zipfile
    import numpy as np
    def Ecxtractor(filename):
        print("Extracting file...")
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall()
            print("File extracted!")
            print("Syncing complete!")

    def syncCIA(var3DSCIA):
        if os.path.exists(var3DSCIA):
            print("File found!")
            print("Extracting file...")
            with zipfile.ZipFile(var3DSCIA, 'r') as zip_ref:
                zip_ref.extractall()
                print("File extracted!")
                print("Syncing complete!")
        else:
            print("File not found!")
            print("Please try again!")
            sys.exit()



            def ConvertFile(filename):
                print("Converting file...")
                with zipfile.ZipFile(filename, 'r') as zip_ref:
                    zip_ref.extractall()
                    print("File extracted!")
                    print("Converting complete!")

                print("Convert the models to a readable format for Unreal Engine 5?")
                print("Please note that this will take a while!")
                ConvertFile(filename).png()==input("Please enter the name of the .cia file you wish to rip: ")
                ConvertFile(filename).png()==ConvertFile(filename).png().allfiles[0].png()
                # find all the 3d models in the .cia filename
                # convert them to .fbx
                ConvertFile(filename).png()==ConvertFile(filename).png().allfiles[0].png().tofile(filename).fbx()
