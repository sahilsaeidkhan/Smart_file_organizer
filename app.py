import streamlit as st

st.title("Smart File Organizer")

st.write("My First Streamlit Project")

folder_path = st.text_input(

    "Enter Folder Path"
)

st.write(folder_path)