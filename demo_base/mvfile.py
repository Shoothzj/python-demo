import os
import subprocess

listdir = os.listdir()
for file in listdir:
    if os.path.isdir(file):
        newPath = file.replace("-", "_")
        print("file " + file)
        print("newPath " + newPath)
        subprocess.run(["mv", file, newPath])