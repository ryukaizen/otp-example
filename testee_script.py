# MODIFIED VERSION FOR TEST CASES

import os
import random
import re
import smtplib
import string 
import sys

from dotenv import load_dotenv
from email.message import EmailMessage

def validate_email(receiver_email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'   
    if (re.fullmatch(regex, receiver_email)): # Validates email address using regular expression  
        print("[*] No error found in email!")
        return receiver_email
    else:
        raise AssertionError("[x] Invalid email address!")

def get_otp_len(otp_len):
    if otp_len < 4 or otp_len > 8:
        raise AssertionError("\n[x] OTP length should be between 4 to 8.\n\tPlease enter again.")
    else:
        return otp_len

def get_otp_type(otp_type):
    if otp_type < 1 or otp_type > 7:
        raise AssertionError("\n[x] Invalid OTP type selected.")          
    else:
        return otp_type
    
def generate_otp(otp_len, otp_type):
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

    return otp

def send_otp(otp, receiver_email):

    load_dotenv() # Loads the .env file

    # Initialization of environment variables 
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    SENDER_EMAIL_PASS = os.getenv('SENDER_EMAIL_PASS')
    EMAIL_OTP_SUBJECT = os.getenv('EMAIL_OTP_SUBJECT')
    EMAIL_SERVER_HOST = os.getenv('EMAIL_SERVER_HOST')
    EMAIL_SERVER_PORT = os.getenv('EMAIL_SERVER_PORT')

    server = smtplib.SMTP(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT) # Create a session
    server.starttls() # Starts TLS for security
    server.login(SENDER_EMAIL, SENDER_EMAIL_PASS) # SMTP server authentication

    msg = EmailMessage() 
    msg.set_content(f"Your one-time password is: {otp}\n\nHave a good day haha!")
    msg['Subject'] = EMAIL_OTP_SUBJECT # The subject field of your email
    msg['From'] = SENDER_EMAIL 
    msg['To'] = receiver_email

    server.send_message(msg) # Send the email
    print("\n[!] OTP sent! Check your inbox for the OTP!")
    server.quit() # Terminate SMTP session

def verify_otp(otp):
    while True:
        otp_input = input("\n[*] Enter the received OTP: ")
        if otp_input == otp:
            print("\n[*] OTP verified successfully!")
            break
        else:
            print("\n[x] Invalid OTP. Please re-enter it again.")
            continue