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


    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions
        """
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue()
                self.assertIn(correct, str_data)


    @tags("1")
    def test_a_module_exist(self):
        """
        Test that correct module exist for assignment 1.
        |G|Förväntar att följande modul finns men hittades inte:|/RE|
        {arguments}
        """
        self._argument = "analyze_functions"
        self.assertIsNotNone(util.find_spec(self._argument))


    @tags("1")
    def test_b_vocals(self):
        """
        Testar "v" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True

        inp = ["v", " ", "q"]
        self.check_print_contain(inp, "270")

    @tags("1")
    def test_c_dots(self):
        """
        Testar "p" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True

        inp = ["p", " ", "q"]
        self.check_print_contain(inp, "18")

    @tags("1")
    def test_d_uppers(self):
        """
        Testar "u" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True

        inp = ["u", " ", "q"]
        self.check_print_contain(inp, "20")

    @tags("1")
    def test_e_wrong_command(self):
        """
        Testar utskrift vid felaktigt kommando.
        Använde {arguments} som kommando.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True
        self._argument = "Gobble gobble"
        inp = [self._argument, " ", "q"]
        self.check_print_contain(inp, "Not an option!")


class Test2Assignment2(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_worth = 10

    @tags("2")
    def test_a_sorted_list(self):
        """
        Testar med en sorterad lista.
        Använde följande som argument: {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Följande returnerades:
        {student}
        """
        self._argument = [0, 1, 2, 4, 5]
        self.assertEqual(exam.list_median(self._argument[:]), 2)

    @tags("2")
    def test_b_unsorted_list(self):
        """
        Testar med osorterad lista.
        Använde följande som argument: {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Följande returnerades:
        {student}
        """
        self._argument = [5, 1, 0, 2, 4]
        self.assertEqual(exam.list_median(self._argument[:]), 2)

        self._argument = [2, 1, 4, 5, 3, 2]
        self.assertEqual(exam.list_median(self._argument[:]), 2.5)


    @tags("2")
    def test_d_not_imported_module(self):
        """
        Kollar att du inte har använt dig av importerad modul för att lösa uppgiften.
        |R|Hittade modulen:|/RE|
        statistics
        """
        # Check that module is not used for solving Assignment
        finder = ModuleFinder()
        finder.run_script(REPO_PATH + "/" + exam.__name__ + ".py")
        self.assertNotIn("statistics", finder.modules.keys())

class Test3Assignment3(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_worth = 10

    @tags("3")
    def test_a_empty_list(self):
        """
        Testar med en tom list, [], som argument.
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        self._argument = []
        self.assertEqual(exam.find_duplicates(self._argument[:]), [])
        
    @tags("3")
    def test_b_no_duplicates(self):
        """
        Testar med en lista som inte har några dubletter.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        self._argument = ["hej", "hopp"]
        self.assertEqual(exam.find_duplicates(self._argument[:]), [])

    @tags("3")
    def test_c_duplicates(self):
        """
        Testar med en lista som har ett dubletter par.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        self._argument = ["hej", "hopp", "hej"]
        self.assertEqual(exam.find_duplicates(self._argument[:]), ["hej"])

        self._argument = ["oj", "hej", "oj", "hopp", "hej"]
        self.assertEqual(exam.find_duplicates(self._argument[:]), ["hej", "oj"])

    @tags("3")
    def test_e_case_insensitive_duplicates(self):
        """
        Testar med en lista som har dubletter och är case-insensitive.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        self._argument = ["hej", "Hej"]
        self.assertEqual(exam.find_duplicates(self._argument[:]), ["hej"])

class Test4Assignment4(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """ 
    points_worth = 10

    @tags("4")
    def test_a_one_of_each(self):
        """
        Testar med en lista som har ett element av varje datatype.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        self._argument = [1, "hej", ["3", "4", "5"]]
        self.assertEqual(exam.types(self._argument[:]), "The square of 1 is 1. The secret word is hej. The list contains 3, 4, 5.")
        self._argumen = [1, "hej", ["3", "4", "5", "hej", "haha"]]
        self.assertEqual(exam.types(self._argumen[:]),
                         "The square of 1 is 1. The secret word is hej. The list contains 3, 4, 5, hej, haha.")

    @tags("4")
    def test_b_only_integers(self):
        """
        Testar med en lista som bara har heltal.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        self._argument = [12]
        self.assertEqual(exam.types(self._argument[:]), "The square of 12 is 144.")
        self._argument = [2, 5, 8]
        self.assertEqual(exam.types(self._argument[:]), "The square of 2 is 4. The square of 5 is 25. The square of 8 is 64.")

    @tags("4")
    def test_c_empty_list(self):
        """
        Testar med en tom lista, [], som argument.
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        self._argument = []
        self.assertEqual(exam.types(self._argument[:]), "")


class Test5Assignment5(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """ 
    points_worth = 10

    @tags("5")
    def test_a_valid(self):
        """
        Testar med korrekta addresser.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        match = ["abc@dbwebb.com", ".@dbwebb.com", "ab_c@dbwebb.com", "ab-c@dbwebb.com",
                 "aa.b-c@dbwebb.com", "aa.b-c@dbw.ebb.com", "a23c@dbwebb.com", "abc@dbwebb.co3", "abc@dbwebb.se"]
        for case in match:
            self._argument = case
            self.assertTrue(exam.validate_email(self._argument))

    @tags("5")
    def test_b_invalid(self):
        """
        Testar med icke korrekta addresser.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        not_match = ["abcdbwebb.com", "@dbwebb.com", "abc@asf..com", "abc@.com",
                     "ab c@dbwebb.com",
                     "ab:c@dbwebb.com", "ab!c@dbwebb.com", "aåc@dbwebb.com",
                     "abcdbwebb.c", "ab-c@dbwebbcom", "aa.b-c@dbwebb.coms",
                     "Awac@dbwebb.com", "aa.b-c@dbwebb.coms", "aa.b-c@db@webb.com"]

        for case in not_match:
            self._argument = case
            self.assertFalse(exam.validate_email(self._argument))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=ExamTestResultExam, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
