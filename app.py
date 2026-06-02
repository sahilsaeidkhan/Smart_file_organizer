import streamlit as st
from organizer_oop import FileOrganizer

if "selected_folder" not in st.session_state:
   st.session_state.selected_folder = None


st.title("Smart File Organizer")

st.write("Organize your files automatically into folders.")

if st.button("Select Folder"):
    
    from tkinter import Tk, filedialog

    root = Tk() # starts tkinter
    root.withdraw() # without this an empty window appears

    selected_folder = filedialog.askdirectory()

    st.session_state.selected_folder = selected_folder

    st.write(selected_folder)

if st.button("Organize Files"):
 
 if st.session_state.selected_folder:

    organizer = FileOrganizer()


    moved_files , stats = organizer.organize_files(st.session_state.selected_folder)

    st.success("Files Organized Successfully")
    st.write("Total files moved",len(moved_files))
    st.write("Statistics")
    for key,value in stats.items():
       st.write(f"{key}:{value}")
    


 else:
    st.warning("Please select a folder first")






