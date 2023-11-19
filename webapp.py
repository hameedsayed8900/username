import streamlit as st
import os
import sys

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

    # Add the directory containing the cloned repository to the Python path
    sys.path.append(os.getcwd())

    # Set execute permissions on the Maigret.py script
    os.system(f"chmod +x {script_path}")

    # Import main from the maigret module
    from maigret import main

    # Run the main function with the parameter read from the nicknameInput field
    result = main(nickname)

    # Print the result (this may take a few minutes)
    st.text(result)
