import streamlit as st

# Initialize session state
if "remove_element" not in st.session_state:
    st.session_state.remove_element = False

# Function to remove element
def remove_element():
    st.session_state.remove_element = True

# Create a placeholder
placeholder = st.empty()

if not st.session_state.remove_element:
    with placeholder:
        st.write("This element will be removed.")
        st.button("Remove Element", on_click=remove_element)
else:
    placeholder.empty()  # Clears the element
