# So the first thing is i have to understand the process then break the processs what should be at first what next like that...
# and i have feel the code to do that i need to open my heart for love and that felling will chnage everything like that ok .....


# so now the first part is begiing like this :-
#  1> Load Encrypytion Key 
#  2> Add a Pass Word
# 3> save to file
# 4> decryption
# 5> View Pass
# 6> Show it wit random colors  


# Now the separation is almost ready we need to create a mental flow chart so imagine it foe final time with heart ful of emotion tol make it real and  meaningfull...

# Now the logic part we need to make to flow our emotion into life :-
# like  For encryption needs Fernet
# Save everything in json file
# Every breaked part or chunk i just wrote all of them are are just different function
# like this [def add_pass ():]

# Now th last part i have to debug the code mentally to understand what could go wrong
# everything that i can think could go wrong is how that thing will make it stonger and make my code more stronger for next project 
# and thats how i will make my logic stronger than everest and depth more than mariana trench..
# And the belief i can do this will only tell me what could go wrong and that is the thing i nneed to make strong an stronger for next project......

from cryptography.fernet import Fernet
import os
import random
from cryptography.fernet import Fernet
from getpass import getpass  
KEY_FILE = "key.key"

def write_key(path = KEY_FILE):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    return key

def load_key(path = KEY_FILE):
    if not os.path.exists(path):
        print("No key found! Generating a new keei it safe...")
        return write_key(path)
    with open(path, "rb") as f:
        return f.read()
    
KEY = load_key()
FERNET = Fernet(KEY)

            


import json
DATA_FILE = "passwords.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        return{}
    with open(DATA_FILE, "r", encoding = "utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Data file corupted. Starting fresh.")
            return {} 


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def add_password():
    data = load_data()
    account = input("Account name (e.g.,  gmail, github): ").strip()
    if not account:
        print("Account name cannot be empty")
        return
    username = input("Username/email (optional):").strip()
    password = input("Password: ").strip()

    encrypted_password = FERNET.encrypt(password.encode()).decode()
    

    data[account] = {
            "username": username,
            "password": encrypted_password
        }

    save_data(data)
    print(f"Account {account} saved succesfully (encrypted for now)")



ANSI_COLORS = [
    '\u001b[31m', # red
    '\u001b[32m', # green
    '\u001b[33m', # yellow
    '\u001b[34m', # blue
    '\u001b[35m', # magenta
    '\u001b[36m', # cyan
    '\u001b[37m', # white
    '\u001b[90m', # bright black (gray)
    '\u001b[91m', # bright red
    '\u001b[92m', # bright green
    '\u001b[93m', # bright yellow
    '\u001b[94m', # bright blue
    '\u001b[95m', # bright magenta
    '\u001b[96m', # bright cyan
]
ANSI_RESET = '\u001b[0m'

def colored_random(text: str) -> str:
    parts = []
    for ch in text:
        if ch.isspace():
            parts.append(ch)
        else:
            parts.append(f"{random.choice(ANSI_COLORS)}{ch}{ANSI_RESET}")
    return ''.join(parts)

def view_passwords():
    data = load_data()
    if not data:
        print("NO passwords stored yet.")
        return
    print("\n🔒 Stored accounts:")
    for account, info in data.items():
        username = info.get("username", "")
        enc_password = info.get("password", "")
        try:
            password = FERNET.decrypt(enc_password.encode()).decode()
        except:
            password = "<decryption error>"
        print("-------")
        print("Account:", account)
        if username:
            print("User:", username)
        print("Password:", colored_random(password))
        print("---")



def main_loop():
    print("Welcome, Fury! This is your password manager. Type 'help' for commands.")
    while True:
        mode = input("\nChoose: [add/view/quit/help]: ").strip().lower()
        if mode in ("q", "quit", "exit"):
            print("Goodbye! Keep your key.key safe!")
            break
        elif mode == "add":
            add_password()
        elif mode == "view":
            view_passwords()
        elif mode == "help":
            print("\nCommands:\n  add  - Add a new account\n  view - View all accounts\n  quit - Exit program")
        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    
    print("Key loaded. key.key exists:", os.path.exists(KEY_FILE))
    print("Key preview (First 8 bytes hex ):", KEY[:8].hex())
    main_loop()






