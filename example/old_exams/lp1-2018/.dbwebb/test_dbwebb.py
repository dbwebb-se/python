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
        self.assertTrue(hasattr(exam, "validate_mobile"))
        self.assertTrue(hasattr(exam, "verify_credit_card"))
        self.assertTrue(hasattr(exam, "find_difference"))
        self.assertTrue(hasattr(exam, "validate_date_time"))

    def test_b_analyze_text(self):
        """
        Test assignment 1
        """
        self.assertNotEqual(exam.analyze_text.__doc__.strip(), "Assignment 1")
        self.assertIsNotNone(util.find_spec("analyze_functions"))
        inp = ["s", "spaces", "l", "letters", "c", "specials", "Gobble gobble", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                code = exam.analyze_text()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                self.assertEqual(list_data, ["206", "206", "721", "721", "17", "17", "Not an option!"])
                self.assertTrue(code)

    def test_c_validate_mobile(self):
        """
        Test assignment 2
        """
        self.assertNotEqual(exam.validate_mobile.__doc__.strip(), "Assignment 2")
        match = ["070-354 78 00", "072-354 02 11", "073-456 12 99", "076-686 78 01", "079-244 07 80"]
        not_match = ["xxx-xxx xx xx", "072-354 02 111", "075-456 12 99",
                     "0734561299", "076456 12 99", "073-4561299", "073-456 12 9a"]

        for case in match:
            self.assertTrue(exam.validate_mobile(case))

        for case in not_match:
            self.assertFalse(exam.validate_mobile(case))

    def test_d_verify_credit_card(self):
        """
        Test assignment 3
        """
        self.assertNotEqual(exam.verify_credit_card.__doc__.strip(), "Assignment 3")

        match = [
            "38520000023237",
            "4024007149639212",
            "5493046493842344",
            "6011989109950095",
        ]
        not_match = ["38520000023236", "371727588736132", "3717275887361314", "601198910995009", "385200000232347"]

        for case in match:
            self.assertTrue(exam.verify_credit_card(case))

        for case in not_match:
            self.assertFalse(exam.verify_credit_card(case))


    def test_e_find_difference(self):
        """
        Test assignment 4
        """
        self.assertNotEqual(exam.find_difference.__doc__.strip(), "Assignment 4")
        empty = []
        self.assertEqual(exam.find_difference(empty, empty), [])
        no_dups = ["hej", "hopp"]
        self.assertEqual(exam.find_difference(no_dups, empty), no_dups)
        dups = ["hej", "hopp", "hej"]
        self.assertEqual(exam.find_difference(dups, empty), ["hej", "hopp"])

        mult_dups = ["oj", "hej", "elefant", "oj", "hopp", "hej"]
        mult_dups2 = ["Elefant", "oj", "hopp", "hej"]
        self.assertEqual(exam.find_difference(mult_dups, mult_dups2), empty)
        mult_dups = ["kossa", "gris", "elefant", "tiger", "åsna", "apa"]
        mult_dups2 = ["Elefant", "orm", "apa", "katt", "åsna"]
        self.assertEqual(
            exam.find_difference(mult_dups, mult_dups2),
            ["gris", "katt", "kossa", "orm", "tiger"]
        )


    def test_f_validate_date_time(self):
        """
        Test assignment 5
        """
        self.assertNotEqual(exam.validate_date_time.__doc__.strip(), "Assignment 5")
        self.assertIsNotNone(util.find_spec("date_time_functions"))

        inp = ["d", "date", "t", "time", "Gobble gobble", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                code = exam.validate_date_time()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                self.assertEqual(list_data, [
                    "2018-10-30",
                    "2018-10-30",
                    "08:00, 21:03, 12:15, 13:15, 16:30, 18:30, 21:04, 21:03",
                    "08:00, 21:03, 12:15, 13:15, 16:30, 18:30, 21:04, 21:03",
                    "Not an option!",
                ])
                self.assertTrue(code)

if __name__ == '__main__':
    unittest.main(verbosity=2)
