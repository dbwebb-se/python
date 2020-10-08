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
from examiner.exam_test_case import ExamTestCase
from examiner.exam_test_result import ExamTestResult

proj_path = os.path.dirname(os.path.realpath(__file__ + "/.."))
if proj_path not in sys.path:
    sys.path.insert(0, proj_path)
#pylint: disable=wrong-import-position
import exam
#pylint: enable=wrong-import-position
#pylint: disable=attribute-defined-outside-init, line-too-long

class Test1Assignment1(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    def test_a_module_exist(self):
        """
        |G|Förväntar att följande modul finns men hittades inte:|/RE|
        {arguments}
        """
        self._argument = "analyze_functions"
        self.assertIsNotNone(util.find_spec(self._argument))

    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions
        """
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.analyze_text()
                str_data = fake_out.getvalue()
                self.assertIn(correct, str_data)

    def test_b_space_command(self):
        """
        Testar "s" och "space" kommandot
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        # inp = ["s", "spaces", "l", "letters", "c", "specials", "Gobble gobble", "q"]
        self._argument = ["s", " ", "q"]
        self.check_print_contain(self._argument, "206")
        self._argument = ["spaces", " ", "q"]
        self.check_print_contain(self._argument, "206")

    # self.assertEqual(list_data, ["206", "206", "721", "721", "17", "17", "Not an option!"])
    def test_c_letters_command(self):
        """
        Testar "l" och "letters" kommandot
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        # inp = [l", "letters", "c", "specials", "Gobble gobble", "q"]
        self._argument = ["l", " ", "q"]
        self.check_print_contain(self._argument, "721")
        self._argument = ["letters", " ", "q"]
        self.check_print_contain(self._argument, "721")

    def test_d_specials_command(self):
        """
        Testar "c" och "specials" kommandot
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        # inp = [c", "specials", "Gobble gobble", "q"]
        self._argument = ["c", " ", "q"]
        self.check_print_contain(self._argument, "17")
        self._argument = ["specials", " ", "q"]
        self.check_print_contain(self._argument, "17")

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


class Test2Assignment2(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    def test_a_valid_numbers(self):
        """
        Testar med korrekta nummer.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        match = ["070-354 78 00", "072-354 02 11", "073-456 12 99", "076-686 78 01", "079-244 07 80"]
        for case in match:
            self._argument = case
            self.assertTrue(exam.validate_mobile(self._argument))

    def test_b_invalid_numbers(self):
        """
        Testar med icke-korrekta nummer.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        not_match = ["xxx-xxx xx xx", "072-354 02 111", "075-456 12 99",
                     "0734561299", "076456 12 99", "073-4561299", "073-456 12 9a"]
        for case in not_match:
            self._argument = case
            self.assertFalse(exam.validate_mobile(self._argument))


class Test3Assignment3(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    def test_a_valid_numbers(self):
        """
        Testar med korrekta nummer.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """

        match = [
            "38520000023237",
            "4024007149639212",
            "5493046493842344",
            "6011989109950095",
        ]
        for case in match:
            self._argument = case
            self.assertTrue(exam.verify_credit_card(self._argument))

    def test_b_invalid_numbers(self):
        """
        Testar med korrekta nummer.
        Använde följande som argument:
        {arguments}
        Förväntar sig att följande returneras:
        {correct}
        Fick:
        {student}
        """
        not_match = ["38520000023236", "371727588736132", "3717275887361314", "601198910995009", "385200000232347"]

        for case in not_match:
            self._argument = case
            self.assertFalse(exam.verify_credit_card(self._argument))


class Test4Assignment4(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    def test_a_no_buplicates(self):
        """
        Testar med listor som inte har dubletter.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        empty = []
        self._multi_arguments = [empty, empty]
        self.assertEqual(exam.find_difference(empty, empty), empty)

        no_dups = ["hej", "hopp"]
        self._multi_arguments = [no_dups, empty]
        self.assertEqual(exam.find_difference(no_dups, empty), no_dups)

        dups = ["hej", "hopp", "hej"]
        self._multi_arguments = [dups, empty]
        self.assertEqual(exam.find_difference(dups, empty), ["hej", "hopp"])

    def test_b_buplicates(self):
        """
        Testar med listor som har dubletter.
        Använder följande som argument:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        mult_dups = ["oj", "hej", "elefant", "oj", "hopp", "hej"]
        mult_dups2 = ["Elefant", "oj", "hopp", "hej"]
        self._multi_arguments = [mult_dups, mult_dups2]
        self.assertEqual(exam.find_difference(mult_dups, mult_dups2), [])

        mult_dups = ["kossa", "gris", "elefant", "tiger", "åsna", "apa"]
        mult_dups2 = ["Elefant", "orm", "apa", "katt", "åsna"]
        self._multi_arguments = [mult_dups, mult_dups2]
        self.assertEqual(
            exam.find_difference(mult_dups, mult_dups2),
            ["gris", "katt", "kossa", "orm", "tiger"]
        )


class Test5Assignment5(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.

    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    def test_a_module_exist(self):
        """
        |G|Förväntar att följande modul finns men hittades inte:|/RE|
        {arguments}
        """
        self._argument = "date_time_functions"
        self.assertIsNotNone(util.find_spec(self._argument))

    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions
        """
        with patch('builtins.input', side_effect=inp):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                exam.validate_date_time()
                str_data = fake_out.getvalue()
                self.assertIn(correct, str_data)

    def test_b_date_command(self):
        """
        Testar "d" och "date" kommandot
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        # inp = [t", "time", "Gobble gobble", "q"]
        self._argument = ["d", " ", "q"]
        self.check_print_contain(self._argument, "2018-10-30")
        self._argument = ["date", " ", "q"]
        self.check_print_contain(self._argument, "2018-10-30")

    def test_c_time_command(self):
        """
        Testar "t" och "time" kommandot
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        # inp = [t", "time", "Gobble gobble", "q"]
        self._argument = ["t", " ", "q"]
        self.check_print_contain(self._argument, "08:00, 21:03, 12:15, 13:15, 16:30, 18:30, 21:04, 21:03")
        self._argument = ["time", " ", "q"]
        self.check_print_contain(self._argument, "08:00, 21:03, 12:15, 13:15, 16:30, 18:30, 21:04, 21:03")

    def test_d_invalid_command(self):
        """
        Testar felaktigt kommando.
        Använde {arguments} som kommando.
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self._argument = "Gobble gobble"
        inp = [self._argument, " ", "q"]
        self.check_print_contain(inp, "Not an option!")


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)

