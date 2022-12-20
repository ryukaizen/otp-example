# -------------------------------------------------------------------------------
# This is my college assignment. I'm not responsible for any misuse of this code.
#                       - Akash (github.com/ryukaizen)
# -------------------------------------------------------------------------------

# With functional decomposition using OOP concepts

import os
import random
import re
import smtplib
import string
import sys

from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv() # Load the .env file
msg = EmailMessage() # Create message object

# Initialization of environment variables 
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SENDER_EMAIL_PASS = os.getenv('SENDER_EMAIL_PASS')
EMAIL_OTP_SUBJECT = os.getenv('EMAIL_OTP_SUBJECT')
EMAIL_SERVER_HOST = os.getenv('EMAIL_SERVER_HOST')
EMAIL_SERVER_PORT = os.getenv('EMAIL_SERVER_PORT')

class OTP:
    def __init__(self):
        try:
            self.server = smtplib.SMTP(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT) # Create a session
            self.server.starttls() # Starts TLS for security
            self.server.login(SENDER_EMAIL, SENDER_EMAIL_PASS) # SMTP server authentication
        except Exception as e:
            print("Error occured while connecting to the server: ", e)
            sys.exit(1)
        else:
            print(f"""\n\033[48;5;202m---------------------[ OTP GENERATOR ]---------------------\033[0m""" + 
                "\n\033[1;97m[!] Connection to e-mail server established successfully!\n" + 
                "\t\tHost: {}\n\t\tPort: {}\033[0m".format(EMAIL_SERVER_HOST, EMAIL_SERVER_PORT) +
                "\n\033[30;48;5;34m-----------------------------------------------------------\033[0m\n")
        
        self.receiver_email = self.get_receiver_email() # Gets the receiver's email
        self.otp_len = self.get_otp_len() # Gets the length of the OTP
        self.otp_type = self.get_otp_type() # Gets the type of the OTP
        self.otp_code = self.generate_otp(self.otp_len, self.otp_type) # Generates the OTP
        self.send_otp(self.otp_code, self.receiver_email) # Sends the OTP to the receiver's email
        self.verify_otp(self.otp_code) # Verifies the OTP
    
    # There are many better ways to do this, but I was low on time
    def generate_otp(self, otp_len, otp_type): 
        self.otp_code = ""
        if otp_type == 1:
            for i in range(otp_len):
                self.otp_code += random.choice(string.digits)            
        elif otp_type == 2:
            for i in range(otp_len):
                self.otp_code += random.choice(random.choice(string.digits) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase))      
        elif otp_type == 3:
            for i in range(otp_len):
                self.otp_code += random.choice(random.choice(string.digits) + random.choice(string.ascii_uppercase)) 
        elif otp_type == 4:
            for i in range(otp_len):
                self.otp_code += random.choice(random.choice(string.digits) + random.choice(string.ascii_lowercase)) 
        elif otp_type == 5:
            for i in range(otp_len):
                self.otp_code += random.choice(random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)) 
        elif otp_type == 6:
            for i in range(otp_len):
                self.otp_code += random.choice(string.ascii_uppercase)
        elif otp_type == 7:
            for i in range(otp_len):
                self.otp_code += random.choice(string.ascii_lowercase)
        return self.otp_code 
    
    def get_receiver_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'   
        while True:
            try:
                receiver_email = input("\n[*] Enter receiver's email address: ")
                if not (re.fullmatch(regex, receiver_email)): # Validates email address using regular expression
                    print("[x] Invalid email address! Try again.")
                    continue
            except ValueError:
                print("\n[x] Please enter a valid email address.")    
                continue
            else:
                return receiver_email
    
    def get_otp_len(self):
        while True:
            try:
                self.otp_len = int(input("\n\n[*] Enter OTP length (no. of digits). Minimum 4, maximum 8: "))         
                if self.otp_len < 4 or self.otp_len > 8:
                    print("\n[x] OTP length should be between 4 to 8.\n\tPlease enter again.")
                    continue
            except ValueError: # To handle empty input
                print("\n[x] Please enter the OTP length (no. of digits) in numbers. Minimum 4, maximum 8")    
                continue
            else:   
                return self.otp_len

    def get_otp_type(self):
        while True:
            try:
                self.otp_type = int(input(   
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
                if self.otp_type < 1 or self.otp_type > 7:
                    print("\n[x] Invalid option selected.")
                    continue
            except ValueError: 
                print("\n[x] Please enter valid option no.")    
                continue
            else:
                return self.otp_type
    
    def send_otp(self, otp_code, receiver_email):
        input("\n[!] All ready! Press enter to send the OTP.")
        msg.set_content(f"Your one-time password is: {otp_code}\n\nHave a good day haha!") # The body of your email
        msg['Subject'] = EMAIL_OTP_SUBJECT # The subject field of your email
        msg['From'] = SENDER_EMAIL # The sender's email address
        msg['To'] = receiver_email # The recipient's email address
        try:
            self.server.send_message(msg) # Send the email
        except Exception as e:
            print("Error occured: ", e)
            sys.exit(1) # Exit on exception
        else:
            print("\n[!] OTP sent! Check your inbox for the OTP!")
            
    def verify_otp(self, otp_code):
        while True:
            try:
                self.otp_input = input("\n[*] To verify, enter the OTP you've received: ")
            except ValueError:
                print("\n\n[x] Please enter your OTP.")
                continue
            else:
                if self.otp_input == otp_code:
                    print("\n[*] OTP verified successfully!")
                    break
                else:
                    print("\n[x] Invalid OTP. Please re-enter it again.")
                    continue

if __name__ == "__main__":
    OTPClass = OTP()
    input("\n\n[*] Press enter to exit.")
    OTPClass.server.quit() # Terminate SMTP session
    sys.exit(0)