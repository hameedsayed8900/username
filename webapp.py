import streamlit as st
import os

st.title("Maigret web version")

nicknameInput = st.text_input("Enter nickname", "...")

if st.button("Start"):
    nickname = nicknameInput.title()

    # Specify the path to your Maigret.py script in the GitHub repository
    script_path = "/tmp/maigret_repo/maigret.py"

    # Clone the repository to a temporary directory
    os.system(f"git clone https://github.com/hameedsayed8900/username.git /tmp/maigret_repo")

    # Set execute permissions on the Maigret.py script
    os.system(f"chmod +x {script_path}")

    # Run the script Maigret.py with the parameter read from the nicknameInput field
    result = os.popen(f"{script_path} {nickname}").read()

    # Print the result (this may take a few minutes)
    st.text(result)
