import os
import shutil

fromdir = "/Users/maitri/Downloads/project102"
todir = "/Users/maitri/Desktop/Document_Files"

listoffiles = os.listdir(fromdir)
print(listoffiles)

for filename in listoffiles:
    name, extension = os.path.splitext(filename)
    if extension == "":
        continue 
    if extension in ['.pdf']:
        path1 = fromdir + "/" + filename
        path2 = todir + "/" + "Document_Files"
        path3 = todir + "/" + "Document_Files" + "/" + filename
        if os.path.exists(path2):
            print("Moving " + filename + ".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + filename + ".....")
            shutil.move(path1,path3)
