import streamlit as st
import os

st.title("Maigret web version")

nicknameInput = st.text_input("Enter nickname", "…")

if st.button("Start"):
    nickname = nicknameInput.title()
    
    # Specify the path to your Maigret.py script in the GitHub repository
    script_path = "https://raw.githubusercontent.com/hameedsayed8900/username/main/Maigret.py"
    
    # Clone the repository to a temporary directory
    os.system(f"git clone https://github.com/hameedsayed8900/username.git /tmp/maigret_repo")
    
    # Run the script Maigret.py with the parameter read from the nicknameInput field
    result = os.popen(f"python /tmp/maigret_repo/Maigret.py {nickname}").read()
    
    # Print the result (this may take a few minutes)
    st.text(result)
