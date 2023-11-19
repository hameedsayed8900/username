import streamlit as st
import os

st.title("Maigret web version")

nicknameInput = st.text_input("Enter nickname", "...")

if st.button("Start"):
    nickname = nicknameInput.title()

    # Specify the name of the script in the GitHub repository
    script_name = "maigret.py"

    # Clone the repository to the current working directory
    os.system("git clone https://github.com/hameedsayed8900/username.git")

    # Dynamically set the script path based on the current working directory
    script_path = os.path.join(os.getcwd(), script_name)

    # Set execute permissions on the Maigret.py script
    os.system(f"chmod +x {script_path}")

    # Run the script maigret.py with the parameter read from the nicknameInput field
    result = os.popen(f"{script_path} {nickname}").read()

    # Print the result (this may take a few minutes)
    st.text(result)
