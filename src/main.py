from PIL import Image
import os

def convert(filepath, filename, filetype, converttype, exportlocation):
    location = "../Exports" if not exportlocation else exportlocation
    os.makedirs(location, exist_ok=True)

    with Image.open(os.path.join(filepath, f"{filename}.{filetype}")) as img:
        save_path = os.path.join(location, f'{filename}.{converttype}')

        img.save(save_path, format=converttype.upper())

        print(f'FILE SAVED TO {save_path}')

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$Hello welcome to Shrek64 FileConversion$$$")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

filepath = input("Please specify the path to the file you would like to convert ONLY THE DIRECTORY OF THE FILE (example: C:\photos\catphotos): ")
filename = input("Please enter the name of the file NOT INCLUDING THE TYPE JUST THE NAME (example: picture1, thebeach, catphoto): ")
filetype = input("Please enter the filetype of the file WITHOUT A . (example: png, jpg, jpeg): ")
converttype = input("Please enter the filetype you would like to convert to WITHOUT A . (example: png, jpg, jpeg): ")
exportlocation = input("OPTIONAL: Please enter a path to a folder to save this file: ")

convert(filepath, filename, filetype, converttype, exportlocation)

print("Program finished")
