# comment 
#* *TODO 
#! warning 
#? test code 
#// ignore

import streamlit as st
from cryptography.fernet import Fernet
import json
import string
import engine
import time
import qrcode
from dotenv import load_dotenv
import os

load_dotenv()

Dna_key = os.getenv('DNA_KEY')

st.set_page_config(
    page_title="Dnakey",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="expanded"
)

class DnaScript:

    def __init__(self):
        # Instantiate DNAEngine upon object creation
        self.engine = engine.DNAEngine()
        self.symbols = list(string.punctuation)
        self.lett, self.hash_text, self.prompt_list = [], [], []
        self.NEWLEVEL = [[],[],[],[],[]]
        self.wp = 0

    def dna_main(self, data, prompt):
        self.prompt = prompt
        self.data = data
        # Call check_symbols to check if the symbols in the prompt are valid
        self.check_symbols()
        # Iterate through each character in the prompt string
        for letter in prompt:
            # Check if the current position in the DNA sequence
            # is greater than or equal to the length of the corresponding DNA sequence in the dna_brain data structure
            if self.wp >= len(self.data["dna_brain"][letter]):
                # If so, add the remaining characters in the prompt string to a list and check_level to check the level
                self.lett.extend(prompt)
                self.check_level()
                # Call new_level to reset join_new and start a new level
                self.new_level()
            # Try to append the corresponding DNA symbol for the current character to a list called hash_text
            try:
                self.hash_text.append(
                    self.data["dna_brain"][letter][self.wp][letter])
                self.wp += 1
            # If the index is out of range, return 0
            except IndexError:
                return 0
        self.result_prompt()

    def check_symbols(self):
        for symbol in self.prompt:
            if symbol in self.symbols:
                st.error(f"\n'{symbol}' Dnakey does not accept symbols! 🙁")
                time.sleep(0.5)
                st.info("If you don't know Dnakey accepts max 11 characters for now + supports numbers [0, 9] and no symbols!", icon="ℹ️")
                quit()

    def result_prompt(self):  # //sourcery skip: extract-method
        jhash = ''.join(self.hash_text)
        hash_length = len(self.hash_text)
        condition = ["Weak🙁", "#ffa347"] if hash_length < 4 else ["Medium😎", "#3cb371"]
        st.code(f"'TOKEN':['{jhash}', '{condition[0]}']\n"
                "//Note: You don't have to save this token just remember your key!", 
                language="javascript")
        self.qr_code(jhash, condition[1])
        self.hash_text.clear()
    
    def check_memory(self):
        st.error("\nDATA OUT OF MEMORY!")
        st.error("\nERROR: Sorry, you entered more than 11 letters/digits!")
        quit()

    def new_level(self):
        joined_lists = [''.join(sublist) for sublist in self.NEWLEVEL]
        to_be_copied = ''.join(self.hash_text) + ''.join(joined_lists)
        condition = ["Strong😮", "#ec002b"]
        st.code(f"'TOKEN':['{to_be_copied}', '{condition[0]}']\n"
                "//Note: You don't have to save this token just remember your key!", 
                language="javascript")
        self.qr_code(to_be_copied, condition[1])
        # Clear some lists
        self.hash_text.clear()
        self.lett.clear()
        for sublist in self.NEWLEVEL:
            sublist.clear()

    def check_level(self):
        # Loop through hash_text and every time you pass 6/7/8/9/10, add the words in the levels (1 to 5)
        for level in self.hash_text:
            if len(self.lett) > 6:
                self.NEWLEVEL[0].append(level[:1])

            if len(self.lett) > 7:
                self.NEWLEVEL[1].append(level[1:2])

            if len(self.lett) > 8:
                self.NEWLEVEL[2].append(level[2:3])

            if len(self.lett) > 9:
                self.NEWLEVEL[3].append(level[3:4])

            if len(self.lett) > 10:
                self.NEWLEVEL[4].append(level[4:5])

            # If the length of hash_text exceeds 11, call check memory function
            if len(self.lett) >= 12:
                self.check_memory()

    def qr_code(self, data_qr, color):
        self.file_name = "qr_code.png"
        qr_data_text = f"-TOKEN: {data_qr}"
        self.color = color
        self.generate_qr_code(qr_data_text, self.file_name, self.color)
        st.subheader("DnaKey QR Code", help="You can scan this QR code to see your token in the phone faster!")
        st.image(image=self.file_name)
        with st.empty():
            for seconds in range(5, -1, -1):
                with st.spinner(f"Clear QR code in: {seconds}s..."):
                        time.sleep(1)
            st.success("Your QR code has been deleted from the database!")
        # Check if the image file exists
        if os.path.exists(self.file_name):
            # Delete the image file
            os.remove(self.file_name)
            print(f"Deleted the image file: {self.file_name}")
        else:
            print(f"The image file does not exist: {self.file_name}")

        exit()

    def generate_qr_code(self, data, file_name, color):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, 
                           box_size=5, border=7)
        qr.add_data(data)
        qr.make(fit=True)
        self.qr_img = qr.make_image(fill_color=color, back_color="#3c3c3c")
        self.qr_img.save(file_name)

class MenuStart:
    def __init__(self):
        # Calling the time and date to keep you updated
        self.wn = 0
        self.space = " "
        
    def menu_start(self):
        st.title("DnaKey!")
        with st.sidebar:
            st.title("Settings")
            self.brain_name = st.text_input("Create New Brain!", placeholder="Example: Emails...")
            if st.button("Create it", key=0) and self.brain_name != "":
                self.check_brain_data()
                with st.spinner("Creating the brain please wait..."):
                    time.sleep(2)
                st.balloons()
                st.success("The new brain created successfully!")

            self.uploaded_file = st.file_uploader("Upload your dnakey brain!",
                                                  help="Required a txt file only!")
            if self.uploaded_file:
                if self.uploaded_file.name.endswith('.txt'):
                    with st.spinner("Verifying the file, please wait..."):
                           time.sleep(2)
                    st.success("The file data is live...")
                else:
                    with st.spinner("Verifying the file, please wait..."):
                        time.sleep(2)
                    st.error("Invalid file format. Please upload a txt file.")

        # Making a while loop to keep asking the user to input something
        self.menu_prompt = st.text_input("Enter Your Key:", max_chars=11, 
                                        help="Note: Dnakey accepts max 11 characters for now + supports numbers [0, 9]!", 
                                        placeholder="Example: Blue / Cat...")
        if st.button("Decode Text", key=1):
            if self.uploaded_file is None:
                st.error("Please upload your file or create new one!")
            try: 
                self.decode_data()
            except Exception:
                st.error("This is not a dnakey brain!")
                time.sleep(0.5)
                st.info("If you don't know you can create a 'dnakey' brain in the sidebar in your left!", icon="ℹ️")
            if self.menu_prompt == "":
                st.error("Please enter your key or create new one!")

        st.text("About DnaKey:")
        with open("info.txt", "r") as f:
                info = f.read()
        st.code(info, language="javascript")

    def decode_data(self):
        # Split the words found in the menu_prompt
        self.m_p = self.menu_prompt.split()
        # Make a while loop to iterate through all the words in the split list
        while self.wn < len(self.m_p):
            if self.m_p:
                self.first_word = self.m_p[self.wn]
                self.data = self.brain_data()
                self.data_user = self.data["dna_brain"]["data_user"]
                st.code("'user_data':{"
                            f"'for_my':'{self.data_user}',"
                            f"'your_key':'{self.first_word}'""}",
                            language="javascript")
                # Pass the word to the dna_main function
                DnaScript().dna_main(self.data, self.first_word)
            self.wn += 1

    def data_qr_note(self):
        return f"for_my: {self.data_user} | your_key: {self.first_word}"

    def brain_data(self):
        if self.uploaded_file is not None:
            # Create a Fernet object with the secret key
            secret_key = Dna_key.encode('latin-1')
            fernet = Fernet(secret_key)
            # To read file as bytes:
            bytes_data = self.uploaded_file
            # st.write(bytes_data)
            st.write(bytes_data)
            # Read the encrypted data from the file
            encrypted_data = self.uploaded_file.read()
            # Decrypt the encrypted data
            decrypted_data = fernet.decrypt(encrypted_data)
            # Convert the decrypted data back to a JSON object
            decrypted_string = decrypted_data.decode()
            self.data = json.loads(decrypted_string)
            return self.data
        
    def check_brain_data(self):
        new_brain = DnaScript().engine
        brain_contents = new_brain.write_dna_brain_to_file(self.brain_name)
        st.download_button(
            label='Download data as txt',
            data=brain_contents,
            file_name=f'dnakey_{self.brain_name}.txt'
        )

if __name__ == '__main__':
    # Start the script
    MenuStart().menu_start()
