# -------------------------------------------------------------------------------
# This is my college assignment. I'm not responsible for any misuse of this code.
#                       - Akash (github.com/ryukaizen)
# -------------------------------------------------------------------------------

# Possible examples of test cases 

import unittest
import string

from main import OTP 

class TestOTP(unittest.TestCase):
    
    # Test cases for email validation:
    def test_valid_email(self):
        self.assertEqual(OTP.get_receiver_email("test@example.com"), "test@example.com")
    
    # Test cases for generated OTPs:
    # Test the generation of an OTP of length 8, containing only digits:
    def test_generate_otp_only_digits(self):
        otp_len = 8
        otp_type = 1
        otp_code = OTP.generate_otp(self, otp_len, otp_type)
        print("[1] Numbers only: ", otp_code)
        
        # Check if the generated OTP is a string of 8 digits
        assert len(otp_code) == 8
        assert all(c in string.digits for c in otp_code)
    
    # Test the generation of an OTP of length 8, containing digits, uppercase letters, and lowercase letters:
    def test_generate_otp_digits_uppercase_lowercase(self):
        otp_len = 8
        otp_type = 2
        otp_code = OTP.generate_otp(self, otp_len, otp_type)
        print("[2] Alphanumeric: ", otp_code)

        # Check if the generated OTP is a string of 8 characters containing at least one digit, 
        # at least one uppercase letter, and at least one lowercase letter
        assert len(otp_code) == 8
        assert any(c in string.digits for c in otp_code)
        assert any(c in string.ascii_uppercase for c in otp_code)
        assert any(c in string.ascii_lowercase for c in otp_code)
        
    # Test the generation of an OTP of length 8, containing digits and uppercase letters:
    def test_generate_otp_digits_uppercase(self):
        otp_len = 8
        otp_type = 3
        otp_code = OTP.generate_otp(self, otp_len, otp_type)
        print("[3] Uppercase alphanumeric: ", otp_code)
        
        # Check if the generated OTP is a string of 8 characters containing at least one digit 
        # and at least one uppercase letter
        assert len(otp_code) == 8
        assert any(c in string.digits for c in otp_code)
        assert any(c in string.ascii_uppercase for c in otp_code)
    
    # Test the generation of an OTP of length 8, containing digits, lowercase letters:
    def test_generate_otp_digits_lowercase(self):
        otp_len = 8
        otp_type = 4
        otp_code = OTP.generate_otp(self, otp_len, otp_type)
        print("[4] Lowercase alphanumeric: ", otp_code)
        
        # Check if the generated OTP is a string of 8 characters containing at least one digit, 
        # at least one lowercase letter
        assert len(otp_code) == 8
        assert any(c in string.digits for c in otp_code)
        assert any(c in string.ascii_lowercase for c in otp_code)
        
    # Test the generation of an OTP of length 8, containing uppercase letters, and lowercase letters:
    def test_generate_otp_uppercase_lowercase(self):
        otp_len = 8
        otp_type = 5
        otp_code = OTP.generate_otp(self, otp_len, otp_type)
        print("[5] Alphabets only: ", otp_code)
        
        # Check if the generated OTP is a string of 8 characters containing at least one uppercase letter, 
        # and at least one lowercase letter
        assert len(otp_code) == 8
        assert any(c in string.ascii_uppercase for c in otp_code)
        assert any(c in string.ascii_lowercase for c in otp_code)
        
    # Test the generation of an OTP of length 8, containing only uppercase letters:
    def test_generate_otp_uppercase(self):
        otp_len = 8
        otp_type = 6
        otp_code = OTP.generate_otp(self, otp_len, otp_type)
        print("[6] Uppercase only: ", otp_code)

        # Check if the generated OTP is a string of 8 uppercase letters
        assert len(otp_code) == 8
        assert all(c in string.ascii_uppercase for c in otp_code)

    # Test the generation of an OTP of length 8, containing only lowercase letters:
    def test_generate_otp_lowercase(self):
        otp_len = 8
        otp_type = 7
        otp_code = OTP.generate_otp(self, otp_len, otp_type)
        print("[7] Lowercase only: ", otp_code)
        
        # Check if the generated OTP is a string of 8 lowercase letters
        assert len(otp_code) == 8
        assert all(c in string.ascii_lowercase for c in otp_code)
        
    # Test case to verify generated otp
    def test_verify_otp_valid(self):
        generated_otp_code = OTP.generate_otp(self, 8, 2)
        to_verify = generated_otp_code
        # to_verify = 12345
        print("Generated OTP for verification: ", generated_otp_code)
        print("Input OTP for verification: ", to_verify)
        self.assertEqual(generated_otp_code, to_verify, "Invalid OTP!")

if __name__ == '__main__':
    unittest.main()