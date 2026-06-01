import os 
import shutil 
from tkinter import Tk,filedialog

class FileOrganizer:

    def __init__(self):
     self.mapping = {

   ".jpg": "Images",
            ".png": "Images",
            ".pdf": "PDFs",
            ".mp4": "Videos",
            ".docx": "Documents",
            ".doc": "Documents"

    }
     
    def create_folder(self,destination_path):

        if not os.path.exists(destination_path):
           os.mkdir(destination_path)
           print(f"{destination_path} created")

    def organize_files(self, target_path):
       
       files = os.listdir(target_path)

       for file in files:
           
           if os.path.isfile(os.path.join(target_path, file)):
              
              name,ext = os.path.splitext(file)

              if ext in self.mapping:
                 
                 category_folder = self.mapping[ext]

                 destination_path = os.path.join( target_path , category_folder)

                 self.create_folder(destination_path)

                 source_path = os.path.join(selected_folder,file)


                 try:
                    shutil.move(source_path,destination_path)
                    print(f"{file} moved to {destination_path}")
                
                 except Exception as e:
                    print(f"Error moving {file}:{e}")





root = Tk()

root.withdraw()    



selected_folder = filedialog.askdirectory()

organizer = FileOrganizer()



organizer.organize_files(selected_folder)































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
