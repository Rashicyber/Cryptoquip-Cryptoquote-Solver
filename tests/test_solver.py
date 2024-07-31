# test_solver.py

import unittest
from solver import decrypt, create_key_from_mapping

class TestSubstitutionCipherSolver(unittest.TestCase):
    def test_decrypt(self):
        cipher_text = "Gsrh rh z hvxivg"
        key_mapping = "zyxwvutsrqponmlkjihgfedcba"
        key = create_key_from_mapping(key_mapping)
        decrypted_message = decrypt(cipher_text, key)
        self.assertEqual(decrypted_message, "This is a secret")

if __name__ == "__main__":
    unittest.main()
