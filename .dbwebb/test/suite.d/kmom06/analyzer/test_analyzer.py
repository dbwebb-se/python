#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from io import StringIO
import os
import sys
from unittest.mock import patch
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


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





class Test2Counters(ExamTestCase):
    """
    Meny options for counting
    """
    @classmethod
    def setUpClass(cls):
        # Otherwise the .txt files will not be found
        os.chdir(REPO_PATH)


    @tags("count", "lines")
    def test_b_lines(self):
        """
        Testar att anropa menyval 'lines' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["lines", "", "q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("17", str_data)



    @tags("count", "words")
    def test_c_words(self):
        """
        Testar att anropa menyval 'words' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["words", "", "q"]

        with patch('builtins.input', side_effect=self._multi_arguments):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("199", str_data)



    @tags("count", "letters")
    def test_d_letters(self):
        """
        Testar att anropa menyval 'letters' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["letters", "", "q"]
        self.norepr = True
        with patch('builtins.input', side_effect=self._multi_arguments):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()
                self.assertIn("907", str_data)



class Test3Frequencies(ExamTestCase):
    """
    Meny options for frequency
    """

    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                main.main()
                for val in correct:
                    str_data = fake_out.getvalue()
                    self.assertIn(val, str_data)


    @tags("freq", "word_frequency")
    def test_a_word_frequency(self):
        """
        Testar att anropa menyval 'word_frequency' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["word_frequency", "", "q"]
        self.check_print_contain(self._multi_arguments, [
            "the: 12 | 6.0%",
            "to: 8 | 4.0%",
            "and: 7 | 3.5%",
            "of: 6 | 3.0%",
            "street: 5 | 2.5%",
            "him: 5 | 2.5%",
            "he: 5 | 2.5%",
        ])




    @tags("freq", "letter_frequency")
    def test_b_letter_frequency(self):
        """
        Testar att anropa menyval 'letter_frequency' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["letter_frequency", "", "q"]
        self.check_print_contain(self._multi_arguments, [
            "e: 108 | 11.9%",
            "t: 91 | 10.0%",
            "o: 77 | 8.5%",
            "h: 67 | 7.4%",
            "n: 66 | 7.3%",
            "i: 64 | 7.1%",
            "a: 64 | 7.1%",
        ])




class Test4All(ExamTestCase):
    """
    Meny options for frequency
    """

    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                main.main()
                for val in correct:
                    str_data = fake_out.getvalue()
                    self.assertIn(val, str_data)

    @tags("all")
    def test_a_all(self):
        """
        Testar att anropa menyval 'all' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["all", "", "q"]

        self.check_print_contain(self._multi_arguments, [
            "17",
            "199",
            "907",
            "the: 12 | 6.0%",
            "to: 8 | 4.0%",
            "and: 7 | 3.5%",
            "of: 6 | 3.0%",
            "street: 5 | 2.5%",
            "him: 5 | 2.5%",
            "he: 5 | 2.5%",
            "e: 108 | 11.9%",
            "t: 91 | 10.0%",
            "o: 77 | 8.5%",
            "h: 67 | 7.4%",
            "n: 66 | 7.3%",
            "i: 64 | 7.1%",
            "a: 64 | 7.1%",
        ])



class Test4Change(ExamTestCase):
    """
    Meny options for frequency
    """

    @tags("change")
    def test_a_change(self):
        """
        Testar att anropa menyval 'all' i main.py.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["change", "lorum.txt", "", "all", "", "q"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main.main()
                str_data = fake_out.getvalue()

                self.assertIn("23", str_data)
                self.assertIn("3", str_data)
                self.assertIn("140", str_data)

                self.assertIn("dolor: 2 | 8.0%", str_data)
                self.assertIn("vivamus: 1 | 4.0%", str_data)
                self.assertIn("vitae: 1 | 4.0%", str_data)
                self.assertIn("varius: 1 | 4.0%", str_data)
                self.assertIn("urna: 1 | 4.0%", str_data)
                self.assertIn("sit: 1 | 4.0%", str_data)
                self.assertIn("pellentesque: 1 | 4.0%", str_data)

                self.assertIn("i: 18 | 12.9%", str_data)
                self.assertIn("e: 16 | 11.4%", str_data)
                self.assertIn("u: 12 | 8.6%", str_data)
                self.assertIn("a: 12 | 8.6%", str_data)
                self.assertIn("t: 10 | 7.1%", str_data)
                self.assertIn("l: 10 | 7.1%", str_data)
                self.assertIn("s: 9 | 6.4%", str_data)



if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
