# OTP-Example

A Python script to demonstrate basic OTP (One-time password) generation, verification and delivery of emails using the Simple Mail Transfer Protocol (SMTP) library.

## To run:
Preferably, use Python 3.10.8 or higher.

Run the commands from below into your shell.
```bash
  git clone https://github.com/Ryukaizen/otp-example.git
  cd otp-example
  cp .env.example .env
  pip install -r requirements.txt
```

Add the environment variables to `.env` file. Then run:

```bash
  python main.py
```
    
## Environment variables

Rename the `.env.example` file to `.env` first.

To run this script, you will need to add the following environment variables to your .env file:

`SENDER_EMAIL = your_email_address@xyz.com`

`SENDER_EMAIL_PASS = password`

Default variables:

`EMAIL_OTP_SUBJECT = "Your OTP for OTP-Example:"`

`EMAIL_SERVER_HOST = smtp.gmail.com`

`EMAIL_SERVER_PORT = 587`


#### For Gmail users:
Make sure to enable IMAP in Gmail settings. 

Then follow these steps: 
1. Activate two-step verification of the corresponding Gmail account. 
2. Create an app password. 
3. Replace the password with the generated app password (a sixteen-digit password).

### Note:
This is just my college assignment for Software Engineering subject. I'm in no way responsible for whatever you do with it.