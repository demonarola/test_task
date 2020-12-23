"""Module to get content of first file"""
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    # Create a folder with name filelist and add files in it
    files = os.listdir(os.path.join(BASE_DIR, "filelist"))
    if files:
        file = sorted(files)[0]
        with open('filelist/'+file) as f:
            s = f.read()
            print(s)
except Exception:
    print("Create a folder with name filelist and add files in it")
