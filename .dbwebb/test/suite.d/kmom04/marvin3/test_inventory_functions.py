#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from io import StringIO
import os
import sys
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
backpack = import_module(REPO_PATH, 'inventory')



class Test2InventoryFunctions(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)



    @tags("inv")
    def test_inventory(self):
        """
        Testar att anropa "inventory" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments  = [["java", "c#"]]


        with patch("sys.stdout", new=StringIO()) as fake_out:
            backpack.inventory(*self._multi_arguments)
            str_data = fake_out.getvalue()

        for val in self._multi_arguments[0]:
            self.assertIn(val, str_data)

        self.assertIn("2", str_data)



    @tags("inv")
    def test_inventory_again(self):
        """
        Testar att anropa "inventory" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = [["python", "golang", "php"]]


        with patch("sys.stdout", new=StringIO()) as fake_out:
            backpack.inventory(*self._multi_arguments)
            str_data = fake_out.getvalue()

        for val in self._multi_arguments[0]:
            self.assertIn(val, str_data)
        self.assertIn("3", str_data)



    @tags("pick")
    def test_pick_with_no_index(self):
        """
        Testar att lägga till ett värde utan att ange ett index, via "pick" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """

        bag = ["snow", "sand"]
        self._multi_arguments = [bag.copy(), "grass"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.pick(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, ["snow", "sand", "grass"])
        self.assertIn(self._multi_arguments[1], str_data)
        self.assertNotIn("Error", str_data)



    @tags("pick")
    def test_pick_at_the_beginning(self):
        """
        Testar att lägga till ett nytt värdet i början av listan, via "pick" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["dog", "cat", "bird", "worm"]

        self._multi_arguments = [bag.copy(), "snake", "0"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.pick(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, ["snake", "dog", "cat", "bird", "worm"])
        self.assertIn(self._multi_arguments[1], str_data)
        self.assertIn(self._multi_arguments[2], str_data)
        self.assertNotIn("Error", str_data)




    @tags("pick")
    def test_pick_in_the_middle(self):
        """
        Testar att lägga till ett nytt värdet i mitten av listan, via "pick" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["dog", "cat", "bird", "worm"]

        self._multi_arguments = [bag.copy(), "snake", "2"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.pick(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, ["dog", "cat", "snake", "bird", "worm"])
        self.assertIn(self._multi_arguments[1], str_data)
        self.assertIn(self._multi_arguments[2], str_data)
        self.assertNotIn("Error", str_data)


    @tags("drop")
    def test_drop_last_element(self):
        """
        Testar att ta bort listans sista värde, via "drop" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["dog", "cat", "bird", "worm"]

        self._multi_arguments = [bag.copy(), "worm"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.drop(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, ["dog", "cat", "bird"])
        self.assertIn(self._multi_arguments[1], str_data)
        self.assertNotIn("Error", str_data)


    @tags("drop")
    def test_drop_first_element(self):
        """
        Testar att kasta bort listans första värde, via "drop" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["dog", "cat", "bird", "worm"]

        self._multi_arguments = [bag.copy(), "dog"]

        with patch("sys.stdout", new=StringIO()) as _:
            new_bag = backpack.drop(bag, *self._multi_arguments[1:])

        self.assertEqual(new_bag, ["cat", "bird", "worm"])



    @tags("drop")
    def test_drop_middle_element(self):
        """
        Testar att kasta bort listans mittersta värde, via "drop" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["dog", "cat", "horse", "bird", "worm"]

        self._multi_arguments = [bag.copy(), "horse"]

        with patch("sys.stdout", new=StringIO()) as _:
            new_bag = backpack.drop(bag, *self._multi_arguments[1:])


        self.assertEqual(new_bag, ["dog", "cat", "bird", "worm"])




    @tags("swap")
    def test_swap_first_and_last(self):
        """
        Testar att byta plats på på listans första och sista värde, via "swap" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["windows", "mac", "linux"]

        self._multi_arguments = [bag.copy(), "windows", "linux"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.swap(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()


        self.assertEqual(new_bag, ["linux", "mac", "windows"])
        self.assertIn(self._multi_arguments[1], str_data)
        self.assertIn(self._multi_arguments[2], str_data)
        self.assertNotIn("Error", str_data)




    @tags("swap")
    def test_swap_items_with_same_name(self):
        """
        Testar att byta plats på de identiska namn, via "swap" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["windows", "mac", "mac", "linux"]

        self._multi_arguments = [bag.copy(), "mac", "mac"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.swap(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, bag)
        self.assertIn("Error", str_data)




    @tags("swap")
    def test_swap_middle_elements(self):
        """
        Testar att byta plats på de två mittersta värden i listan, via "swap" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["windows", "other", "mac", "linux"]

        self._multi_arguments = [bag.copy(), "other", "mac"]

        with patch("sys.stdout", new=StringIO()) as _:
            new_bag = backpack.swap(bag, *self._multi_arguments[1:])

        self.assertEqual(new_bag, ["windows", "mac", "other", "linux"])



    @tags("error", "pick")
    def test_error_on_pick_high_index(self):
        """
        Testar att lägga till ett värde när användaren anger ett för högt index, via "pick" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["alone"]
        self._multi_arguments = [bag.copy(), "more", "2"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.pick(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, self._multi_arguments[0])
        self.assertIn("Error", str_data)
        self.assertIn(str(self._multi_arguments[2]), str_data)



    @tags("error", "drop")
    def test_error_on_drop_empty_bag(self):
        """
        Testar drop kommandot på ett ike existerande värde, via "drop" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = []
        self._multi_arguments = [bag.copy(), "bread"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.drop(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, self._multi_arguments[0])
        self.assertIn("Error", str_data)
        self.assertIn(self._multi_arguments[1], str_data)


    
    @tags("error", "drop")
    def test_error_on_drop_with_items(self):
        """
        Testar drop kommandot på en tom lista, via "drop" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["butter", "cheese"]
        self._multi_arguments = [bag.copy(), "bread"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.drop(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()

        self.assertEqual(new_bag, self._multi_arguments[0])
        self.assertIn("Error", str_data)
        self.assertIn(self._multi_arguments[1], str_data)



    @tags("error", "swap")
    def test_error_on_swap_empty_bag(self):
        """
        Testar "swap" funktionen på en tom lista.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = []
        self._multi_arguments = [bag.copy(), "bread", "butter"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.swap(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()


        self.assertEqual(new_bag, self._multi_arguments[0])
        self.assertIn("Error", str_data)
        self.assertIn(self._multi_arguments[1], str_data)
        self.assertIn(self._multi_arguments[2], str_data)



    @tags("error", "swap")
    def test_error_on_swap(self):
        """
        Testar att byta plats på ett existerande och icke existerande värde, via "swap" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["butter", "cheese"]
        self._multi_arguments = [bag.copy(), "bread", "butter"]

        with patch("sys.stdout", new=StringIO()) as fake_out:
            new_bag = backpack.swap(bag, *self._multi_arguments[1:])
            str_data = fake_out.getvalue()


        self.assertEqual(new_bag, self._multi_arguments[0])
        self.assertIn(self._multi_arguments[1], str_data)



    @tags("error", "swap")
    def test_error_on_swap_same_name(self):
        """
        Testar att byta plats på två likadana värden som bara existerar en gång, via "swap" funktionen.
        Använder följande som argument:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        bag = ["butter", "cheese"]
        self._multi_arguments = [bag.copy(), "butter", "butter"]

        with patch("sys.stdout", new=StringIO()) as _:
            new_bag = backpack.swap(bag, *self._multi_arguments[1:])

        self.assertEqual(new_bag, self._multi_arguments[0])




if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
