#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import re
import os
import sys
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
main = import_module(REPO_PATH, 'main')
marvin2 = import_module(REPO_PATH, 'marvin2')



class Test3Marvin2Extra(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    link_to_assignment = "https://dbwebb.se/uppgift/din-egen-chattbot-marvin-steg-2-v4#extra"

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)


    def check_print_contain(self, inp, correct, func):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                func()
                str_data = fake_out.getvalue()
                for val in correct:
                    self.assertIn(val, str_data)

    @tags("b1")
    def test_has_strings_menu(self):
        """
        Testar att anropa menyval b2 via main funktionen i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande sträng finns med i utskriften:
        {correct}
        Fick följande:
        {student}
        """
        self._multi_arguments = ["b1", "anagram", "ana", "agr", "am", "", "q"]
        self.check_print_contain(self._multi_arguments, ["Match"], main.main)



    @tags("b1")
    def test_has_strings_func(self):
        """
        Testar att anropa has_strings i marvin2.py.
        Använder följande som argument:
        {arguments}
        Förväntar att följande sträng returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._multi_arguments = ["Palindrom", "par", "ind", "rom" ]
        self.assertEqual(
            marvin2.has_strings(*self._multi_arguments),
            "No match" 
        )



if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
