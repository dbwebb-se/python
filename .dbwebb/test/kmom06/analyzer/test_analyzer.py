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
from unittest import TextTestRunner
from exam_test_case import ExamTestCase
from exam_test_result import ExamTestResult
from helper_functions import import_module
from helper_functions import find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
main = import_module(REPO_PATH, "main")


class Test1Files(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    @classmethod
    def setUpClass(cls):
        # Otherwise the .txt files will not be found
        os.chdir(REPO_PATH)

    def test_a_modules_exist(self):
        """
        Testar att din kod är uppdelad i rätt moduler.
        |G|Förväntar att följande modul finns men hittades inte:|/RE|
        {arguments}
        
        """
        self._argument = "main"
        self.assertIsNotNone(util.find_spec(self._argument))
        self._argument = "menu"
        self.assertIsNotNone(util.find_spec(self._argument))
        self._argument = "analyzer"
        self.assertIsNotNone(util.find_spec(self._argument))

class Test2Counters(ExamTestCase):
    """
    Meny options for counting
    """
    def test_b_lines(self):
        """
        Testar "lines" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True
        with patch('builtins.input', side_effect=["lines", "", "q"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("17", str_data)

    def test_c_words(self):
        """
        Testar "words" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True
        with patch('builtins.input', side_effect=["words", "", "q"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("199", str_data)



    def test_d_letters(self):
        """
        Testar "letters" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True
        with patch('builtins.input', side_effect=["letters", "", "q"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("907", str_data)



class Test3Frequencies(ExamTestCase):
    """
    Meny options for frequency
    """
    def test_a_word_frequency(self):
        """
        Testar "word_frequency" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """ 
        self.norepr = True
        with patch('builtins.input', side_effect=["word_frequency", "", "q"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("the", str_data)
                self.assertIn("6.0%", str_data)
                self.assertIn("to", str_data)
                self.assertIn("4.0%", str_data)
                self.assertIn("and", str_data)
                self.assertIn("3.5%", str_data)
                self.assertIn("of", str_data)
                self.assertIn("3.0%", str_data)
                self.assertIn("street", str_data)
                self.assertIn("2.5%", str_data)
                self.assertIn("him", str_data)
                self.assertIn("2.5%", str_data)
                self.assertIn("he", str_data)
                self.assertIn("2.5%", str_data)



    def test_b_letter_frequency(self):
        """
        Testar "letter_frequency" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """ 
        self.norepr = True
        with patch('builtins.input', side_effect=["letter_frequency", "", "q"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("e", str_data)
                self.assertIn("11.9%", str_data)
                self.assertIn("t", str_data)
                self.assertIn("10.0%", str_data)
                self.assertIn("o", str_data)
                self.assertIn("8.5%", str_data)
                self.assertIn("h", str_data)
                self.assertIn("7.4%", str_data)
                self.assertIn("n", str_data)
                self.assertIn("7.3%", str_data)
                self.assertIn("i", str_data)
                self.assertIn("7.1%", str_data)
                self.assertIn("a", str_data)
                self.assertIn("7.1%", str_data)



class Test4All(ExamTestCase):
    """
    Meny options for frequency
    """

    def test_a_all(self):
        """
        Testar "all" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """ 
        self.norepr = True
        with patch('builtins.input', side_effect=["all", "", "q"]):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("17", str_data)
                self.assertIn("199", str_data)
                self.assertIn("907", str_data)
                self.assertIn("the", str_data)
                self.assertIn("6.0%", str_data)
                self.assertIn("he", str_data)
                self.assertIn("2.5%", str_data)
                self.assertIn("e", str_data)
                self.assertIn("11.9%", str_data)
                self.assertIn("i", str_data)
                self.assertIn("7.1%", str_data)



if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
