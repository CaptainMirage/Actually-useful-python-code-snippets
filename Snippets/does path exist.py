from pathlib import Path

MyFile = Path("Your path here")


#  for files
if MyFile.is_file():
    print("this file exists!")
else:
    print("this file does not exist!")


# for directory
if MyFile.is_dir():
    print("this Directory exists!")
else:
    print("this Directory does not exist! (or its not accessable by code)")


# for files or directories
if MyFile.exists():
    print("this directory or file exists!")
else:
    print("this directory or file does not exist!") 