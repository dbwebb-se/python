"""
Overriding TestCase for exam tool.
"""
import re
import unittest
import importlib
from examiner.exceptions import TestFuncNameError, TestClassNameError
import examiner.helper_functions as hf

class ExamTestCase(unittest.TestCase):
    """
    Override methods to help customize outputs of testcases.
    """

    ASSIGNMENT_REGEX = r"\.Test[0-9]?([A-Z].+)\)"
    TEST_NAME_REGEX = r"test(_[a-z])?_(\w+)"
    USER_TAGS = []

    link_to_assignment = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assignment = ""
        self.test_name = ""
        self.student_answer = ""
        self.correct_answer = ""
        self.norepr = False
        self._set_test_name_and_assignment()



    def _set_test_name_and_assignment(self):
        """
        Extract Assignment from TestCase name.
        Extract test name from test function name.
        Format testname and assignment text and assign to test object.
        """
        test_string = str(self)
        try:
            self.assignment = re.search(self.ASSIGNMENT_REGEX, test_string).group(1)
        except AttributeError as e:
            raise TestClassNameError(
                "Class name for TestCase should follow the structure 'Test[<number>]<words>'. Got '" + test_string + "'"
            ) from e

        try:
            self.test_name = re.search(self.TEST_NAME_REGEX, test_string).group(2).replace("_", " ")
        except AttributeError as e:
            raise TestFuncNameError(
                "Test function name should follow the structure 'test[_<letter>]_<name>' Got '" + test_string + "'"
            ) from e


    def set_answers(self, student_answer, correct_answer):
        """
        Set students answer and correct answer as members.
        """
        self.student_answer = repr(student_answer)
        self.correct_answer = repr(correct_answer)
        if self.norepr:
            if isinstance(student_answer, str):
                self.student_answer = hf.clean_str(student_answer)
            else:
                self.student_answer = str(student_answer)



    def assertEqual(self, first, second, msg=None):
        """
        Check if first is equal to second. Save correct and student answer as to variables.
        First comes from student
        """
        self.set_answers(first, second)
        super().assertEqual(first, second, msg)



    def assertIn(self, member, container, msg=None):
        """
        Check if value in container.  Save correct and student answer as to variables.
        Container comes from student
        """
        self.set_answers(container, member)
        super().assertIn(member, container, msg)



    def assertFalse(self, expr, msg=None):
        """
        Check that the expression is False.
        Save correct and student answer as to variables.
        """
        self.set_answers(expr, False)
        super().assertFalse(expr, msg)



    def assertTrue(self, expr, msg=None):
        """
        Check that the expression is true.
        Save correct and student answer as to variables.
        """
        self.set_answers(expr, True)
        super().assertTrue(expr, msg)



    def assertNotIn(self, member, container, msg=None):
        """
        Check that the expression is true.
        Save correct and student answer as to variables.
        """
        self.set_answers(container, member)
        super().assertNotIn(member, container, msg)

    def assertModule(self, module, module_path=None, msg=None):
        """
        Check that module can be imported.
        Save correct and student answer as to variables.
        """
        self.set_answers(module_path, module)
        if module_path is None:
            if importlib.util.find_spec(module) is None:
                msg = self._formatMessage(msg, f"{module} not as standard import")
                raise self.failureException(msg)
        else:
            try:
                hf.import_module(module_path, module)
            except FileNotFoundError as e:
                msg = self._formatMessage(msg, f"{module} not found in path {module_path}")
                raise self.failureException(msg) from e



    def assertAttribute(self, obj, attr, msg=None):
        """
        Check that object has attribute.
        Save correct and student answer as to variables.
        """
        self.set_answers(obj, attr)
        try:
            getattr(obj, attr)
        except AttributeError as e:
            msg = self._formatMessage(msg, f"attribute {attr} not found in object {obj}")
            raise self.failureException(msg) from e



    def assertRaises(self, expected_exception, *args, **kwargs):
        """
        assertRaises is a context and therefore we need to return it
        """
        self.set_answers("", expected_exception)
        return super().assertRaises(expected_exception, *args, **kwargs)



    def assertCountEqual(self, first, second, msg=None):
        """Asserts that two iterables have the same elements, the same number of
        times, without regard to order.
            self.assertEqual(Counter(list(first)),
                             Counter(list(second)))
         Example:
            - [0, 1, 1] and [1, 0, 1] compare equal.
            - [0, 0, 1] and [0, 1] compare unequal.
        """
        self.set_answers(first, second)
        super().assertCountEqual(first, second, msg)



    def assertOrder(self, order, container, msg=None):
        """
        Check that in index of elements in order are lowest to highest in container.
        Save correct and student answer as to variables.
        """
        self.set_answers(container, order)

        try:
            for i in range(len(order)-1):
                if not container.index(order[i]) < container.index(order[i+1]):
                    raise ValueError
        except ValueError as e:
            msg = self._formatMessage(msg, f"Index of elemnts in {order} don't appear in correct order in {container}")
            raise self.failureException(msg) from e
