try:
    file = open("filename.FILEFORMAT")

except FileNotFoundError:
    print("this file does not exist!")
else:
    print("this file exists!")
