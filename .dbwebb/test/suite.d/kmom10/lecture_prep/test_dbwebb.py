#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from importlib import util
from io import StringIO
import os
import sys
from modulefinder import ModuleFinder
from unittest.mock import patch
from examiner import ExamTestCaseExam, ExamTestResultExam, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
exam = import_module(REPO_PATH, "exam")

class Test1Assignment1(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_for_pass = 20
    points_worth = 20

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)



    def test_a_module(self):
        """
        Test that correct module exist for assignment 1.
        |G|Förväntar att följande modul finns men hittades inte:|/RE|
        {arguments}
        """
        self._argument = "exam"
        self.assertIsNotNone(util.find_spec("exam"))

        self._argument = "analyze_text"
        self.assertTrue(hasattr(exam, "analyze_text"))

        self._argument = "verify_hex"
        self.assertTrue(hasattr(exam, "verify_hex"))


    @tags("1")
    def test_b_sentences(self):
        """
        Testar "s" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True

        inp = ["s", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                for v in ["6", "5", "5"]:
                    self.assertIn(v, list_data)



    @tags("1")
    def test_c_gods(self):
        """
        Testar "g" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True

        inp = ["g", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                for v in ["21", "8", "1"]:
                    self.assertIn(v, list_data)



    @tags("1")
    def test_c_gods(self):
        """
        Testar skriva in "h" för att få not an option.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True

        inp = ["h", "q"]
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue().strip("\n")
                list_data = str_data.split("\n")
                self.assertIn("Not an option!", list_data)



class Test2Assignment2(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_worth = 10


    @tags("2")
    def test_a_correct_codes(self):
        """
        Testar med koder som är giltiga.
        Använder följande som argument:
        {arguments}
        Förväntar sig att följande returneras från funktionen:
        {correct}
        Fick utskriften:
        {student}
        """
        self._argument = "#fff"
        self.assertTrue(exam.verify_hex("#fff"))
        self._argument = "#fff000"
        self.assertTrue(exam.verify_hex("#fff000"))
        self._argument = "#0f0f0f"
        self.assertTrue(exam.verify_hex("#0f0f0f"))



    @tags("2")
    def test_b_incorrect_codes(self):
        """
        Testar med koder som är inte är giltiga.
        Använder följande som argument:
        {arguments}
        Förväntar sig att följande returneras från funktionen:
        {correct}
        Fick utskriften:
        {student}
        """

        self._argument = "#0f0f0f0"
        self.assertFalse(exam.verify_hex("0f0f0f0"))
        self._argument = "#ffff"
        self.assertFalse(exam.verify_hex("#ffff"))
        self._argument = "#FFF"
        self.assertFalse(exam.verify_hex("#FFF"))
        self._argument = "#fff"
        self.assertFalse(exam.verify_hex("fff"))
        self._argument = "#0F0F0F"
        self.assertFalse(exam.verify_hex("#0F0F0F"))
        self._argument = "#fff000f"
        self.assertFalse(exam.verify_hex("#fff000f"))
        self._argument = "#orange"
        self.assertFalse(exam.verify_hex("#orange"))



if __name__ == '__main__':
    unittest.main(verbosity=2)
