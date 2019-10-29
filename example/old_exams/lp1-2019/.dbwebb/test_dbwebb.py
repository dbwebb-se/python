#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from unittest.mock import patch
from importlib import util
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
        self.assertTrue(hasattr(exam, "find_replace"))
        self.assertTrue(hasattr(exam, "count_animals"))
        self.assertTrue(hasattr(exam, "validate_isbn"))
        self.assertTrue(hasattr(exam, "decide_winners"))
        self.assertTrue(hasattr(exam, "validate_bookings"))

    def test_b_find_replace(self):
        """
        Test assignment 1
        """
        # self.assertIsNotNone(util.find_spec("analyze_functions"))

        inp = ["is", "ko"]
        with patch('builtins.input', side_effect=inp):
            exam.find_replace()
            with open("output.txt") as fh:
                text = fh.read()
            self.assertIn("Beautiful ko better than ugly.\n", text)
            self.assertIn("Explicit ko better than implicit.\n", text)
            self.assertIn("Simple ko better than complex.\n", text)
            self.assertIn("Complex Is better than complicated.", text)
            self.assertIn("Flat ko better than nested.", text)
            self.assertIn("Sparse Is better than dense.", text)

        inp = ["ugly", "ko"]
        with patch('builtins.input', side_effect=inp):
            exam.find_replace()
            with open("output.txt") as fh:
                text = fh.read()
            self.assertIn("Beautiful is better than ko.\nExplicit is better than implicit.", text)

        inp = ["Errors", "cake"]
        with patch('builtins.input', side_effect=inp):
            exam.find_replace()
            with open("output.txt") as fh:
                text = fh.read()
            self.assertIn("\ncake should never pass silently.\nUnless explicitly silenced.", text)
        
        inp = ["in", "ko"]
        with patch('builtins.input', side_effect=inp):
            exam.find_replace()
            with open("output.txt") as fh:
                output = fh.readlines()
            
            with open("manifesto.txt") as fh:
                manifesto = fh.readlines()
            for index, line in enumerate(output):
                self.assertEqual(line, manifesto[index])
    
    def test_c_count_animals(self):
        """
        Test assignment 2
        """
        self.assertEqual(exam.count_animals({
            "ko": ["Mamma Mu", "Kalvin"],
            "gris": "Babe",
        }), "1 gris: Babe\n2 ko: Kalvin, Mamma Mu")

        self.assertEqual(exam.count_animals({
            "ko": ["Mamma Mu", "Kalvin"],
            "gris": "Babe",
            "tupp": "Jussi",
            "höna": ["Juhani", "Aapo", "Tuomas", "Simeoni", "Timo", "Lauri", "Eero"]
        }), "1 gris: Babe\n7 höna: Aapo, Eero, Juhani, Lauri, Simeoni, Timo, Tuomas\n\
2 ko: Kalvin, Mamma Mu\n1 tupp: Jussi")

    def test_d_validate_isbn(self):
        """
        Test assignment 3
        """
    
        self.assertTrue(exam.validate_isbn("9781861972712"))
        self.assertTrue(exam.validate_isbn("9781617294136"))
        self.assertFalse(exam.validate_isbn("9781681972712"))
        self.assertFalse(exam.validate_isbn("97816819727102"))
        self.assertFalse(exam.validate_isbn("ISBN13-97816819727102"))
        self.assertFalse(exam.validate_isbn("9781861973712"))
        self.assertFalse(exam.validate_isbn("9R81861973712"))
    


    def test_e_decide_winners(self):
        """
        Test assignment 4
        """
        self.assertEqual(exam.decide_winners([]), [])
        self.assertEqual(exam.decide_winners([["11-2", "5-11", "6-11"], ["11-3", "11-5"]]), ['player2', 'player1'])
        self.assertEqual(exam.decide_winners([["11-3", "7-11", "9-11"], ["11-0", "11-5"],
                                              ["1-11", "2-11", "13-11", "11- 13"]]), ['player2', 'player1', 'player2'])
        


    def test_f_validate_bookings(self):
        """
        Test assignment 5
        """
        #pylint: disable=line-too-long
    
        self.assertTrue(exam.validate_bookings([{"date": "2019-10-28", "time": "10-12", "course": "DV1531"}, {"date": "2019-10-28", "time": "9-10", "course": "PA1439"}]))
        self.assertTrue(exam.validate_bookings([{"date": "2019-10-28", "time": "8-13", "course": "DV1531"}, {"date": "2019-10-31", "time": "8-12", "course": "PA1439"}]))
        self.assertTrue(exam.validate_bookings([{"date": "2019-10-28", "time": "8-13", "course": "DV1531"}, {"date": "2019-10-31", "time": "8-12", "course": "PA1439"}, {"date": "2019-10-29", "time": "12-15", "course": "DV1531"}, {"date": "2019-10-30", "time": "8-15", "course": "DV1531"}]))
        self.assertFalse(exam.validate_bookings([{"date": "2019-10-28", "time": "8-13", "course": "DV1531"}, {"date": "2019-10-28", "time": "10-12", "course": "PA1439"}]))
        self.assertFalse(exam.validate_bookings([{"date": "2019-10-28", "time": "10-12", "course": "DV1531"}, {"date": "2019-10-28", "time": "8-13", "course": "PA1439"}]))
        self.assertFalse(exam.validate_bookings([{"date": "2019-10-28", "time": "10-12", "course": "DV1531"}, {"date": "2019-10-28", "time": "8-13", "course": "PA1439"}]))
        #pylint: enable=line-too-long

if __name__ == '__main__':
    unittest.main(verbosity=2)
