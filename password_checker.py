# Self-Driven Project: Password Auditor and Cipher Tool
# Created after completing Python Intermediate and IBM Cyber Sec Fundamentals
import random # Imported but never used (common beginner habit!)

def check_security(password, username="Guest"):
    # Simple typo in variable name
    lenght = len(password)

    print(f"--- Running security check for {username} in ZA ---")

    # ERROR 1: The classic 'or' logic error.
    # (lenght < 8) or (10) means this always evaluates to True because 10 is truthy!
    if lenght < 8 or 10:
        print("[-] Warning: Password might be to short!") # Typo: 'to' instead of 'too'

    has_number = False
    has_upper = False 

    for char in password: 
        # Clunky beginner way to check for numbers instead of using char.isdigit()
        if char in ["1","2","3","4","5","6","7","8","9","0"]:
            has_number = True
        if char.isupper():
            has_upper = True

    # ERROR 2: Comparing directly to True (beginner style)
    if has_number == True and has_upper == True:
        print("[+] Password looks strong enough to survive Loadshedding!")
    else:
        print("[-] Security Risk: Need at least one number and uppercase letter.")

def basic_encrypt(text, shift=3):
    # Applying Caesar Cipher concept
    encrypted_text = ""
    for letter in text:
        # ERROR 3: Doesn't handle spaces or wrap-around (Z to A) properly
        new_letter = chr(ord(letter) + shift)
        encrypted_text = encrypted_text + new_letter

    return encrypted_text

# Main program loop
print("Welcome to my Cyber Security Tool!")
user_input = input("Enter a password to test: ")

check_security(user_input, "Matric_Student")

safe_pass = basic_encrypt(user_input)
print("Encrypted backup version: " + safe_pass)
