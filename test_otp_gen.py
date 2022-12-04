import unittest
import smtplib
import testee_script

class TestOTP(unittest.TestCase):
    def testcase1(self):
        # Variable Input
        print("----------------------------------[Test case #1 - Variable Input]-----------------------------------")
        
        # Get receiver's email
        # receiver_email = "exampleemail@gmail.com" # Pass
        receiver_email = input("\n[*] Enter receiver's email address: ")
        valid_receiver_email = testee_script.validate_email(receiver_email)

        # Get OTP length
        # otp_len = 4 # Pass
        otp_len = int(input("\n\n[*] Enter OTP length (no. of digits). Minimum 4, maximum 8: "))
        valid_otp_len = testee_script.get_otp_len(otp_len)  

        # Get OTP type
        # otp_type = 2 # Pass
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
        valid_otp_type = testee_script.get_otp_type(otp_type)

        # Generate the OTP
        otp = testee_script.generate_otp(valid_otp_len, valid_otp_type)

        # Send the OTP
        testee_script.send_otp(otp, valid_receiver_email)

        # Verify the OTP
        testee_script.verify_otp(otp)

    def testcase2(self):
        # Email Validation
        print("----------------------------------[Test case #2 - Email Validation]-----------------------------------")
        
        # receiver_email = input("\n[*] Enter receiver's email address: ")
        receiver_email = "exampleemail@gmail.com" # Pass
        receiver_email = "exampleemail.com" # Fail

        valid_receiver_email = testee_script.validate_email(receiver_email)

    def testcase3(self):
        # OTP Length
        print("----------------------------------[Test case #3 - OTP Length]-----------------------------------")

        # otp_len = int(input("\n\n[*] Enter OTP length (no. of digits). Minimum 4, maximum 8: "))
        otp_len = 3 # Fail
        # Or 
        # otp_len = 9 # Fail
        # otp_len = 4 # Pass
        valid_otp_len = testee_script.get_otp_len(otp_len)  

    def testcase4(self):
        # OTP Type
        print("----------------------------------[Test case #4 - OTP Type]-----------------------------------")

        # Get OTP type
        # otp_type = int(input(   
        #             "\n[!] Select OTP type from below" +
        #             "\n\n-- [1] Numbers only" +
        #             "\n-- [2] Alphanumeric (alternating caps)" +
        #             "\n-- [3] Uppercase alphanumeric" +
        #             "\n-- [4] Lowercase alphanumeric" +
        #             "\n-- [5] Alphabets only (alternating caps)" +
        #             "\n-- [6] Uppercase alphabets only" +
        #             "\n-- [7] Lowercase alphabets only" +
        #             "\n\n[*] Enter your choice: "
        # ))
        otp_type = 8 # Fail
        valid_otp_type = testee_script.get_otp_type(otp_type)
        print("------------------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    unittest.main()