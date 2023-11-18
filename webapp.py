import streamlit as st
# add a module to run external python scripts
import os


st.title("Maigret web version")
nicknameInput = st.text_input("Enter nickame", "…")
if(st.button("Start")):
    nickname = nicknameInput.title()
    # Run the script Maigret.py with the parameter read from the nicknameInput field
    result=os.popen("github.com/hameedsayed8900/username/blob/main/maigret.py "+nickname).read()
    # Print the result (this may take a few minutes)
    st.text(result)
