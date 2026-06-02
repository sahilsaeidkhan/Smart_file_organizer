import os 
import shutil 
from tkinter import Tk,filedialog

class FileOrganizer:

    def __init__(self):
     self.mapping = {
        
  # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    # Documents
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",

    # PDFs
    ".pdf": "PDFs",

    # Spreadsheets
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",

    # Presentations
    ".ppt": "Presentations",
    ".pptx": "Presentations",

    # Videos
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    # Code
    ".py": "Code",
    ".java": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code",
    ".cpp": "Code",
    ".c": "Code",
       ".md": "Documents",

    # Java compiled files
    ".class": "Code",

    # Subtitle files
    ".vtt": "Subtitles",

    # Executables
    ".exe": "Applications",
    ".msi": "Applications",

    # Encrypted files
    ".enc": "Encrypted",

    # Logs
    ".log": "Logs"


    }
     
    def create_folder(self,destination_path):

        if not os.path.exists(destination_path):
           os.mkdir(destination_path)
           print(f"{destination_path} created")

    def organize_files(self, target_path):
       stats = {}
       moved_files = []

       files = os.listdir(target_path)

       for file in files:
           
           if os.path.isfile(os.path.join(target_path, file)):
              
              name,ext = os.path.splitext(file)

              if ext in self.mapping:
                 
                 category_folder = self.mapping[ext]

                 destination_path = os.path.join( target_path , category_folder)

                 self.create_folder(destination_path)

                 source_path = os.path.join(target_path,file)


                 try:
                    shutil.move(source_path,destination_path)

                    if category_folder not in stats:
                       stats[category_folder] = 1
                    else:
                       stats[category_folder] +=1

                    moved_files.append(f"{file}>{category_folder}")

                    print(f"{file} moved to {destination_path}")

                 except Exception as e:
                    print(f"Error moving {file}:{e}")
       return moved_files , stats 




# root = Tk()

# root.withdraw()    



# selected_folder = filedialog.askdirectory()

# organizer = FileOrganizer()



# organizer.organize_files(selected_folder)































# Practicing 


# class Student:
#     def __init__(self,name,age):
#           self.name = name
#           self.age = age 

#     def show(self):
#          print(f"Name : {self.name}")
#          print(f"Age : { self.age}")


# s1 = Student("Krishna",100)
# s1.show()
