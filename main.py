# This is my college assignment. (Which I'm handing in late :/)
# I'm not so fluent in Python (Typescript is my primary language), so the code may seem (very) poor & has many wrong things.
# Of course, I'm aware that there are many better ways to do this. But anyways, take it with the grain of salt.
# - Akash (github.com/Ryukaizen)

import os
import random
import re
import smtplib
import string, sys

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv() # Loads the .env file

# Initialization of environment variables 
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_EMAIL_PASS = os.getenv('SENDER_EMAIL_PASS')
EMAIL_OTP_SUBJECT = os.getenv('EMAIL_OTP_SUBJECT')
EMAIL_SERVER_HOST = os.getenv('EMAIL_SERVER_HOST')
EMAIL_SERVER_PORT = os.getenv('EMAIL_SERVER_PORT')

msg = EmailMessage() # Create message object

try: 
    server = smtplib.SMTP(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT) # Create a session
    server.starttls() # Starts TLS for security
except Exception as e:
    print("Error occured while connecting to the server: ", e)
    sys.exit(1)
else: 
    print(f"""\n\033[48;5;202m---------------------[ OTP GENERATOR ]---------------------\033[0m""" + 
    "\n\033[1;97m[!] Connection to e-mail server established successfully!\n" + 
    "\t\tHost: {}\n\t\tPort: {}\033[0m".format(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT) +
    "\n\033[30;48;5;34m-----------------------------------------------------------\033[0m\n")

def generate_otp():
    otp = ""

    # OTP length
    otp_len = int(input("\n\n[*] Enter OTP length (no. of digits). Minimum 4, maximum 8: "))         
    if otp_len == 0:
        print("\n[x] Please enter the OTP length (no. of digits) in numbers. Minimum 4, maximum 8")    
        generate_otp()
    elif otp_len < 4:
        print("\n[x] Minimum OTP length is 4 digits. \n\tPlease enter again.")
        generate_otp()
    elif otp_len > 8:
        print("\n[x] Maximum OTP length is 8 digits. \n\tPlease enter again.")
        generate_otp()
    
    # OTP type
    while True:
        otp_type = input(   
            "\n[!] Select OTP type from below" +
            "\n\n-- [1] Numbers only" +
            "\n-- [2] Alphanumeric (alternating caps)" +
            "\n-- [3] Uppercase alphanumeric" +
            "\n-- [4] Lowercase alphanumeric" +
            "\n-- [5] Alphabets only (alternating caps)" +
            "\n-- [6] Uppercase alphabets only" +
            "\n-- [7] Lowercase alphabets only" +
            "\n\n[*] Enter your choice: "
        )

        if otp_type == "1":
            for i in range(otp_len):
                otp += random.choice(string.digits)            
        elif otp_type == "2":
            for i in range(otp_len):
                otp += random.choice(random.choice(string.digits) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase))      
        elif otp_type == "3":
            for i in range(otp_len):
                otp += random.choice(random.choice(string.digits) + random.choice(string.ascii_uppercase)) 
        elif otp_type == "4":
            for i in range(otp_len):
                otp += random.choice(random.choice(string.digits) + random.choice(string.ascii_lowercase)) 
        elif otp_type == "5":
            for i in range(otp_len):
                otp += random.choice(random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)) 
        elif otp_type == "6":
            for i in range(otp_len):
                otp += random.choice(string.ascii_uppercase)
        elif otp_type == "7":
            for i in range(otp_len):
                otp += random.choice(string.ascii_lowercase)
        else:
            print("\n[x] Invalid option selected.")
            continue

        send_otp(otp)
        break
                
def send_otp(otp):
    receiver_email = input("\n[*] Enter receiver's email address: ")
    
    msg.set_content(f"Your one-time password is: {otp}\n\nHave a good day haha!")
    msg['Subject'] = EMAIL_OTP_SUBJECT
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'   
    
    if (re.fullmatch(regex, receiver_email)): # Validates email address using regular expression
        input("\n[!] All ready! Press enter to send the OTP.")
        try:
            server.send_message(msg) # Send the email
        except Exception as e:
            print("Error occured: ", e, "\n\n[*] Press enter to try again.")
            send_otp(otp, SENDER_EMAIL)
        else:
            print("\n[!] OTP sent! Check your inbox for the OTP!")
            verify_otp(otp)
    else:
        print("[x] Invalid email address! Try again.")
        send_otp(otp)
            
def verify_otp(otp):
    otp_input = input("\n[*] To verify, enter the OTP you've received: ")
    
    if otp_input == otp:
        print("\n[*] OTP verified successfully!")
        input("\n\n[*] Press enter to exit.")
        server.quit()
        sys.exit(0)
    else:
        print("\n[x] Invalid OTP. Please re-enter it again.\n[x] Or regenerate the OTP by running this program again.")
        verify_otp(otp) 

def main():   
    try:
        server.login(SENDER_EMAIL, SENDER_EMAIL_PASS)
    except Exception as e:
        print("[x] Error occured while logging in: ", e)
        input("\n\n[!] Check the e-mail ID or password provided in .env file!")
        sys.exit(1)
    else:
        print("[!] Login successful!")

    generate_otp()

if __name__ == "__main__":
    main()