import os 
import shutil 

mapping = { 
 ".jpg": "Images",
    ".png": "Images",

    ".pdf": "PDFs",

    ".mp4": "Videos",

    ".docx": "Documents",
    ".doc": "Documents"


}



def create_folder(folder):
     if not os.path.exists(folder):
          os.mkdir(folder)
          print(f"{folder} created")


files = os.listdir()

for file in files :
 if os.path.isfile(file):
     
     name , ext = os.path.splitext(file)

     if ext in mapping:
          
          folder = mapping[ext] 
           
          create_folder(folder)

          shutil.move(file,folder)
          
          print(f"{file} -> {folder}")
