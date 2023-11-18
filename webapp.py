import streamlit as st
import os

# Clone the repository
os.system("git clone https://github.com/hameedsayed8900/username.git")

# Set the working directory to the cloned repository
os.chdir("your-repo")

st.title("Maigret web version")
nicknameInput = st.text_input("Enter nickname", "…")
if(st.button("Start")):
    nickname = nicknameInput.title()
    # Run the script Maigret.py with the parameter read from the nicknameInput field
    result = os.popen("maigret.py " + nickname).read()
    # Print the result (this may take a few minutes)
    st.text(result)
