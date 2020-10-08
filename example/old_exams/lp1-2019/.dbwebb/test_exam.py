#!/usr/bin/env python3
"""
Contains testcases for the individual examination.
"""
import unittest
import os
import sys
from unittest.mock import patch
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

    def test_a_find_replace_middle(self):
        """
        Testar att byta ut ett ord mitt i strängen.
        Använde följande som input: 
        {arguments}
        Förväntar att följande finns i filen:
        {correct}
        Letade i följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["is", "ko"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            exam.find_replace()
            with open("output.txt") as fh:
                text = fh.read()
            self.assertIn("Beautiful ko better than ugly.\n", text)
            self.assertIn("Explicit ko better than implicit.\n", text)
            self.assertIn("Simple ko better than complex.\n", text)
            self.assertIn("Complex Is better than complicated.", text)
            self.assertIn("Flat ko better than nested.", text)
            self.assertIn("Sparse Is better than dense.", text)

    def test_b_find_replace_end(self):
        """
        Testar att byta ut sista ordet på en rad.
        Använde följande som input: 
        {arguments}
        Förväntar att följande finns i filen:
        {correct}
        Letade i följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["ugly", "ko"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            exam.find_replace()
            with open("output.txt") as fh:
                text = fh.read()
            self.assertIn("Beautiful is better than ko.\nExplicit is better than implicit.", text)

    def test_c_find_replace_first(self):
        """
        Testar att byta ut första ordet på en rad.
        Använde följande som input: 
        {arguments}
        Förväntar att följande finns i filen:
        {correct}
        Letade i följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["Errors", "cake"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            exam.find_replace()
            with open("output.txt") as fh:
                text = fh.read()
            self.assertIn("\ncake should never pass silently.\nUnless explicitly silenced.", text)

    def test_d_find_replace_no_match(self):
        """
        Testar att byta ut ord som inte finns, för att kolla att manifesto.txt kopieras till output.txt.
        Använde följande som input: 
        {arguments}
        Förväntar att följande rad finns i filen:
        {correct}
        Hittade följande rad istället:
        {student}
        """
        self._multi_arguments = ["in", "ko"]
        with patch('builtins.input', side_effect=self._multi_arguments):
            exam.find_replace()
            with open("output.txt") as fh:
                output = fh.readlines()
            with open("manifesto.txt") as fh:
                manifesto = fh.readlines()
            for index, line in enumerate(output):
                self.assertEqual(line, manifesto[index])

class Test2Assignment2(ExamTestCase):
    """
    Assignment 2.
    """
    def test_a_count_animals(self):
        """
        Testar olika stora dictionaries.
        Följande användes som argument till funktionen:
        {arguments}
        Förväntar att följande sträng returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._argument = {
            "ko": ["Mamma Mu", "Kalvin"],
            "gris": "Babe",
        }
        self.assertEqual(exam.count_animals(self._argument), "1 gris: Babe\n2 ko: Kalvin, Mamma Mu")

        self._argument = {
            "ko": ["Mamma Mu", "Kalvin"],
            "gris": "Babe",
            "tupp": "Jussi",
            "höna": ["Juhani", "Aapo", "Tuomas", "Simeoni", "Timo", "Lauri", "Eero"]
        }
        self.assertEqual(exam.count_animals(self._argument), "1 gris: Babe\n7 höna: Aapo, Eero, Juhani, Lauri, Simeoni, Timo, Tuomas\n2 ko: Kalvin, Mamma Mu\n1 tupp: Jussi")

class Test3Assignment3(ExamTestCase):
    """
    Each assignment has 3 testcase with multiple asserts.
    """
    def test_a_valid_isbn(self):
        """
        Test Testar olika korrekta isbn nummer.
        Följande användes som argument till funktionen:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument = "9781861972712"
        self.assertTrue(exam.validate_isbn(self._argument))
        self._argument = "9781617294136"
        self.assertTrue(exam.validate_isbn(self._argument))

    def test_b_invalid_sum_isbn_(self):
        """
        Test icke-korrekta isbn där summan blir fel.
        Följande användes som argument till funktionen:
        {arguments}
        Förväntar att följande returneras:
        {correct}
        Fick istället:
        {student}
        """
        self._argument = "9781681972712"
        self.assertFalse(exam.validate_isbn(self._argument))
        self._argument = "97816819727102"
        self.assertFalse(exam.validate_isbn(self._argument))
        self._argument = "9781861973712"
        self.assertFalse(exam.validate_isbn(self._argument))

    def test_c_invalid_chars_isbn_(self):
        """
        Testar icke-korrekta isbn där bokstäver ingår.
        Följande användes som argument till funktionen:
        {arguments}
        Testet förväntar sig att följande returneras: 
        {correct}
        Följande värde returnerades istället:
        {student}
        """
        self._argument = "ISBN13-97816819727102"
        self.assertFalse(exam.validate_isbn(self._argument))
        self._argument = "9R81861973712"
        self.assertFalse(exam.validate_isbn(self._argument))



class Test4Assignment4(ExamTestCase):
    """
    Each assignment has 4 testcase with multiple asserts.
    """

    def test_a_empty_list(self):
        """
        Testar med tom lista
        Följande användes som argument till funktionen:
        {arguments}
        Testet förväntar sig att följande lista returneras:
        {correct}
        Följande lista returnerades istället:
        {student}
        """
        self._argument = []
        self.assertEqual(exam.decide_winners(self._argument), [])

    def test_b_two_matches(self):
        """
        Testar med två matcher.
        Följande användes som argument till funktionen:
        {arguments}
        Testet förväntar sig att följande lista returneras:
        {correct}
        Följande lista returnerades istället:
        {student}
        """
        self._argument = [["11-2", "5-11", "6-11"], ["11-3", "11-5"]]
        self.assertEqual(exam.decide_winners(self._argument), ['player2', 'player1'])

    def test_c_more_matches(self):
        """
        Testar med flera matcher.
        Följande användes som argument till funktionen:
        {arguments}
        Testet förväntar sig att följande lista returneras:
        {correct}
        Följande lista returnerades istället:
        {student}
        """
        self._argument = [
            ["11-3", "7-11", "9-11"],
            ["11-0", "11-5"],
            ["1-11", "2-11", "13-11", "11- 13"]
        ]
        self.assertEqual(exam.decide_winners(self._argument), ['player2', 'player1', 'player2'])


class Test5Assignment5(ExamTestCase):
    """
    Each assignment has 5 testcase with multiple asserts.
    """
    def test_a_valid_bookings(self):
        """
        Testar med giltiga bokningar.
        Följande användes som argument till funktionen:
        {arguments}
        Testet förväntar sig att följande returneras:
        {correct}
        Din funktion returnerade istället:
        {student}
        """
        #pylint: disable=line-too-long
        self._argument = [{"date": "2019-10-28", "time": "10-12", "course": "DV1531"}, {"date": "2019-10-28", "time": "9-10", "course": "PA1439"}]
        self.assertTrue(exam.validate_bookings(self._argument))
        self._argument = [{"date": "2019-10-28", "time": "8-13", "course": "DV1531"}, {"date": "2019-10-31", "time": "8-12", "course": "PA1439"}]
        self.assertTrue(exam.validate_bookings(self._argument))
        self._argument = [{"date": "2019-10-28", "time": "8-13", "course": "DV1531"}, {"date": "2019-10-31", "time": "8-12", "course": "PA1439"}, {"date": "2019-10-29", "time": "12-15", "course": "DV1531"}, {"date": "2019-10-30", "time": "8-15", "course": "DV1531"}]
        self.assertTrue(exam.validate_bookings(self._argument))
        #pylint: enable=line-too-long

    def test_b_invalid_bookings(self):
        """
        Testar med icke-giltiga bokningar.
        Följande användes som argument till funktionen:
        {arguments}
        Testet förväntar sig att följande returneras:
        {correct}
        Din funktion returnerade istället:
        {student}
        """
        #pylint: disable=line-too-long
        self._argument = [{"date": "2019-10-28", "time": "8-13", "course": "DV1531"}, {"date": "2019-10-28", "time": "10-12", "course": "PA1439"}]
        self.assertFalse(exam.validate_bookings(self._argument))
        self._argument = [{"date": "2019-10-28", "time": "10-12", "course": "DV1531"}, {"date": "2019-10-28", "time": "8-13", "course": "PA1439"}]
        self.assertFalse(exam.validate_bookings(self._argument))
        #pylint: enable=line-too-long

if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
