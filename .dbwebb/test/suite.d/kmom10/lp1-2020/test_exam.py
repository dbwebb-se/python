#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
from importlib import util
from io import StringIO
import os
import sys
from unittest.mock import patch
from unittest import TextTestRunner
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

    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions
        """
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue()
                for v in correct:
                    self.assertIn(v, str_data)

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)



    @tags("1")
    def test_a_module_exist(self):
        """
        Testar att rätt modul är skapad.
        |G|Förväntar att följande modul finns men hittades inte:|/RE|
        {arguments}
        """
        self._argument = "analyze_functions"
        self.assertIsNotNone(util.find_spec(self._argument))



    @tags("1")
    def test_b_year(self):
        """
        Testar "year" kommandot.
        Använde följande som input:
        {arguments}
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["year", "1897"] 
        self.check_print_contain(self._multi_arguments, ["Bataille de neige:1468", "Boulevard des Italiens:18"])

        self._multi_arguments = ["year", "1892"] 
        self.check_print_contain(self._multi_arguments, ["Le clown et ses chiens:199", "Pauvre Pierrot:1365", "Un bon bock:121"])

        self._multi_arguments = ["year", "1893"] 
        self.check_print_contain(self._multi_arguments, ["Blacksmith Scene:2149"])

    @tags("1")
    def test_c_title(self):
        """
        Testar "title" kommandot.
        Förväntar sig att följande finns i utskriften:
        {correct}
        Fick utskriften:
        {student}
        """
        self.norepr = True

        inp = ["title"]
        self.check_print_contain(
            inp,
            [
                "Baby's Dinner:5.9",
                "Leaving the Factory:6.9",
                "The Arrival of a Train:7.4",
                "The Photographical Congress Arrives in Lyon:5.7",
                "The Waterer Watered:7.1",
                "Blacksmith Scene:5.1",
                "The Sea:5.7",
                "The Messers. Lumière at Cards:5.7",
                "Cordeliers' Square in Lyon:5.6",
                "Fishing for Goldfish:5.1",
                "Jumping the Blanket:5.5",
                "Trick Riding:5.6",
                "Watering the Flowers:5.6",
                "Sea Bathing:4.7"
            ]
        )


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
        self.check_print_contain(self._argument, ["Not an option!"])



class Test2Assignment2(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_worth = 10

    @tags("2")
    def test_a_addition(self):
        """
        Testar listor med "+" operatorn.
        Använde följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._multi_arguments = [[15, 12, 13, 14], "+"]
        self.assertEqual(exam.reversed_sum([15, 12, 13, 14], "+"), 108)

        self._multi_arguments = [[25, 12], "+"]
        self.assertEqual(exam.reversed_sum([25, 12], "+"), 64)

        self._multi_arguments = [[25], "+"]
        self.assertEqual(exam.reversed_sum([25], "+"), 52)

    @tags("2")
    def test_b_addition_lose_zero(self):
        """
        Testar listor med "+" operatorn där listan innehåller tal som slutar på 0 och ska bli av med 0 i omvandlingsprocessen.
        Använde följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._multi_arguments = [[10, 12, 13, 14], "+"]
        self.assertEqual(exam.reversed_sum([10, 12, 13, 14], "+"), 58)

    @tags("2")
    def test_c_subtraction(self):
        """
        Testar listor med "-" operatorn.
        Använde följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._multi_arguments = [[15, 12, 13, 14], "-"]
        self.assertEqual(exam.reversed_sum([15, 12, 13, 14], "-"), -6)

        self._multi_arguments = [[10, 12, 13, 14], "-"]
        self.assertEqual(exam.reversed_sum([10, 12, 13, 14], "-"), -56)

        self._multi_arguments = [[25, 12], "-"]
        self.assertEqual(exam.reversed_sum([25, 12], "-"), 40)

        self._multi_arguments = [[25], "-"]
        self.assertEqual(exam.reversed_sum([25], "-"), 52)



class Test3Assignment3(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_worth = 10

    @tags("3")
    def test_a_repeating_letter(self):
        """
        Testar med sträng där det finns två av varje bokstav.
        Använder följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._argument = "abcab"
        self.assertEqual(
            exam.repeating_letter_distance(self._argument), 
            {'a': 3, 'b': 3}
        )

        self._argument = "abccba"
        self.assertEqual(
            exam.repeating_letter_distance(self._argument), 
            {'a': 5, 'b': 3, 'c': 1}
        )

        self._argument = "kismkmiwlwosolpp"
        self.assertEqual(
            exam.repeating_letter_distance(self._argument), 
            {'k': 4, 'i': 5, 's': 9, 'm': 2, 'w': 2, 'l': 5, 'o': 2, 'p': 1}
        )


    @tags("3")
    def test_b_missing_repeating_letter(self):
        """
        Testar med sträng där det saknas bokstaväver.
        Använder följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._argument = "abcba"
        self.assertEqual(
            exam.repeating_letter_distance(self._argument), 
            {'a': 4, 'b': 2}
        )

        self._argument = "abca"
        self.assertEqual(
            exam.repeating_letter_distance(self._argument), 
            {'a': 3}
        )

        self._argument = "kiskmwolwolpp"
        self.assertEqual(
            exam.repeating_letter_distance(self._argument), 
            {'k': 3, 'w': 3, 'o': 3, 'l': 3, 'p': 1}
        )



class Test4Assignment4(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_worth = 10

    @tags("4")
    def test_a_default_argument(self):
        """
        Testar utan att skicka in argument till default parametern.
        Använder följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._multi_arguments = ["A third class of historians-the so-called Historians of culture.", 10]
        self.assertEqual(exam.find_word(*self._multi_arguments), "historians")

        self._multi_arguments = ["A third class! of historians-the so-called Historians of culture.", 6]
        self.assertEqual(exam.find_word(*self._multi_arguments), "called")

        self._multi_arguments = ["A third class! of historians-the so-called Historians of culture.", 2]
        self.assertEqual(exam.find_word(*self._multi_arguments), "of")

        self._multi_arguments = ["'A' third class of; historians-the so-called Historians of culture.", 3]
        self.assertEqual(exam.find_word(*self._multi_arguments), "the")

        self._multi_arguments = ["A third class of; historians-the so /called Historians of culture?", 7]
        self.assertEqual(exam.find_word(*self._multi_arguments), "culture")


    @tags("4")
    def test_b_integer_optional_parameter(self):
        """
        Testar med heltal som argument till den optionella parametern.
        Använder följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._multi_arguments = ["A third class of historians-the so-called Historians of culture-", 10, 2]
        self.assertEqual(exam.find_word(*self._multi_arguments), "Historians")

        self._multi_arguments = ["A third class! of historians-the so-called Historians of culture-", 2, 2]
        self.assertEqual(exam.find_word(*self._multi_arguments), "so")

        self._multi_arguments = ["A third class! of historians-the so-called Historians of culture-", 2, 3]
        self.assertEqual(exam.find_word(*self._multi_arguments), "of")


    @tags("4")
    def test_c_string_optional_parameter(self):
        """
        Testar med sträng som argument till den optionella parametern.
        Använder följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._multi_arguments = ["A third class of historians-the so-called Historians of culture-", 10, "Hist"]
        self.assertEqual(exam.find_word(*self._multi_arguments), "Historians")

        self._multi_arguments = ["A third class of historians-the so-called Historians of culture-", 5, "thi"]
        self.assertEqual(exam.find_word(*self._multi_arguments), "third")

        self._multi_arguments = ["A third class! of historians-the so-called Historians Of culture-", 2, "O"]
        self.assertEqual(exam.find_word(*self._multi_arguments), "Of")

        self._multi_arguments = ["A third class! of historians-the so-called Historians Of culture-", 2, "o"]
        self.assertEqual(exam.find_word(*self._multi_arguments), "of")



class Test5Assignment5(ExamTestCaseExam):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """
    points_worth = 10

    @tags("5")
    def test_a_list_with_integers(self):
        """
        Testar med listor som innehåller heltal.
        Använder följande som input
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student} 
        """
        self._argument = [4, 6, 2, 2, 6, 4, 4, 4, 6]
        self.assertEqual(exam.frequency_sort(self._argument), [4, 4, 4, 4, 6, 6, 6, 2, 2])


        self._argument = [44, 6, 21, 21, 6, 44, 44, 44, 6]
        self.assertEqual(exam.frequency_sort(self._argument), [44, 44, 44, 44, 6, 6, 6, 21, 21])



if __name__ == '__main__':
    runner = unittest.TextTestRunner(resultclass=ExamTestResultExam, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
