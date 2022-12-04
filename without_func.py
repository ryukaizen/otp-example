# Without functional decomposition

import os
import random
import re
import smtplib
import string
import sys

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
    server.login(SENDER_EMAIL, SENDER_EMAIL_PASS) # SMTP server authentication
except Exception as e:
    print("Error occured while connecting to the server: ", e)
    sys.exit(1)
else:
    print(f"""\n\033[48;5;202m---------------------[ OTP GENERATOR ]---------------------\033[0m""" + 
            "\n\033[1;97m[!] Connection to e-mail server established successfully!\n" + 
            "\t\tHost: {}\n\t\tPort: {}\033[0m".format(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT) +
            "\n\033[30;48;5;34m-----------------------------------------------------------\033[0m\n")

while True:
    try:
        otp_len = int(input("\n\n[*] Enter OTP length (no. of digits). Minimum 4, maximum 8: "))         
        if otp_len < 4 or otp_len > 8:
            print("\n[x] OTP length should be between 4 to 8.\n\tPlease enter again.")
            continue
    except ValueError: # To handle empty input
            print("\n[x] Please enter the OTP length (no. of digits) in numbers. Minimum 4, maximum 8")    
            continue
    else:   
        break

while True:
    try:
        otp_type = int(input(   
                "\n[!] Select OTP type from below" +
                "\n\n-- [1] Numbers only" +
                "\n-- [2] Alphanumeric (alternating caps)" +
                "\n-- [3] Uppercase alphanumeric" +
                "\n-- [4] Lowercase alphanumeric" +
                "\n-- [5] Alphabets only (alternating caps)" +
                "\n-- [6] Uppercase alphabets only" +
                "\n-- [7] Lowercase alphabets only" +
                "\n\n[*] Enter your choice: "
        ))
    
        if otp_type < 1 or otp_type > 7:
            print("\n[x] Invalid option selected.")
            continue
    except ValueError: 
        print("\n[x] Please enter valid option no.")    
        continue
    else:
        break
        
otp = ""

if otp_type == 1:
    for i in range(otp_len):
        otp += random.choice(string.digits)            
elif otp_type == 2:
    for i in range(otp_len):
        otp += random.choice(random.choice(string.digits) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase))      
elif otp_type == 3:
    for i in range(otp_len):
        otp += random.choice(random.choice(string.digits) + random.choice(string.ascii_uppercase)) 
elif otp_type == 4:
    for i in range(otp_len):
        otp += random.choice(random.choice(string.digits) + random.choice(string.ascii_lowercase)) 
elif otp_type == 5:
    for i in range(otp_len):
        otp += random.choice(random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)) 
elif otp_type == 6:
    for i in range(otp_len):
        otp += random.choice(string.ascii_uppercase)
elif otp_type == 7:
    for i in range(otp_len):
        otp += random.choice(string.ascii_lowercase)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'   

while True:
    try:
        receiver_email = input("\n[*] Enter receiver's email address: ")
    except ValueError:
        print("\n[x] Please enter a valid email address.")    
        continue
    else:
        if (re.fullmatch(regex, receiver_email)): # Validates email address using regular expression
            input("\n[!] All ready! Press enter to send the OTP.")
            msg.set_content(f"Your one-time password is: {otp}\n\nHave a good day haha!")
            msg['Subject'] = EMAIL_OTP_SUBJECT # The subject field of your email
            msg['From'] = SENDER_EMAIL 
            msg['To'] = receiver_email

            try:
                server.send_message(msg) # Send the email
            except Exception as e:
                print("Error occured: ", e)
                sys.exit(1) # Exit on exception
            else:
                print("\n[!] OTP sent! Check your inbox for the OTP!")
                break         
        else:
            print("[x] Invalid email address! Try again.")
            continue
        
while True:
    try:
        otp_input = input("\n[*] To verify, enter the OTP you've received: ")
    except ValueError:
        print("\n\n[x] Please enter your OTP.")
        continue
    else:
        if otp_input == otp:
            print("\n[*] OTP verified successfully!")
            break
        else:
            print("\n[x] Invalid OTP. Please re-enter it again.")
            continue

input("\n\n[*] Press enter to exit.")
server.quit() # Terminate SMTP session
sys.exit(0)