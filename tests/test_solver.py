# test_solver.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
