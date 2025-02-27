import streamlit as  st
import os


def checkfile_exist(file):
    file_name = file.name
    file_path = os.path.join('./uploaded_data', file_name)
    do_embedding = None
    if os.path.exists(file_path):        
        exist_warning_placeholder = st.empty()
        exist_warning_placeholder.warning(f"File {file_name} already exists", icon="⚠️")

        radio_placeholder = st.empty()
        with radio_placeholder: 
            overwrite = st.radio("Do you want to overwrite the file?\n\nThis will cause re-embedding and will taketime.", ("Yes", "No"), index=None, key='radio')
            if overwrite == "Yes":
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                st.success(f"File {file.name} has been saved successfully!", icon="✅")
                do_embedding = "YES"

            elif overwrite == 'No':
                st.info("File upload was canceled.", icon="ℹ️")
                do_embedding = "NO"

            if overwrite:
                del st.session_state['radio']
                exist_warning_placeholder.empty()

    else:
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
            do_embedding = "YES"

    return file_path, do_embedding