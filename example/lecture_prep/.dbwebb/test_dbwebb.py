#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from unittest.mock import patch
from importlib import util
from io import StringIO
import os
import sys

proj_path = os.path.dirname(os.path.realpath(__file__ + "/.."))
if proj_path not in sys.path:
    sys.path.insert(0, proj_path)
#pylint: disable=wrong-import-position
import exam
#pylint: enable=wrong-import-position

class TestFunc(unittest.TestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """


    def test_a_module(self):
        """
        Test that module and functions exist
        """
        self.assertIsNotNone(util.find_spec("exam"))
        self.assertTrue(hasattr(exam, "analyze_text"))
        self.assertTrue(hasattr(exam, "verify_hex"))

    def test_b_analyze_text(self):
        """
        Test assignment 1
        """
        self.assertIsNotNone(util.find_spec("analyze_functions"))

        inp = ["s", "g", "h", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                self.assertEqual(list_data, ["6", "5", "5", "21", "8", "1", "Not an option!"])

    def test_c_verify_hex(self):
        """
        Test assignment 2
        """
        self.assertTrue(exam.verify_hex("#fff"))
        self.assertTrue(exam.verify_hex("#fff000"))
        self.assertTrue(exam.verify_hex("#0f0f0f"))

        self.assertFalse(exam.verify_hex("#ffff"))
        self.assertFalse(exam.verify_hex("#FFF"))
        self.assertFalse(exam.verify_hex("fff"))
        self.assertFalse(exam.verify_hex("#0F0F0F"))
        self.assertFalse(exam.verify_hex("#fff000f"))
        self.assertFalse(exam.verify_hex("#orange"))



if __name__ == '__main__':
    unittest.main(verbosity=2)
