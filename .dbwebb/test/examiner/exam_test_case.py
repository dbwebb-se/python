"""
Overriding TestCase for exam tool.
"""
import re
import unittest
import importlib
from examiner.exceptions import TestFuncNameError, TestClassNameError
from examiner.fail_message import FailMessage
import examiner.helper_functions as hf

class ExamTestCase(unittest.TestCase):
    """
    Override methods to help customize outputs of testcases.
    """

    ASSIGNMENT_REGEX = r"\.Test[0-9]?([A-Z].+)\)"
    TEST_NAME_REGEX = r"test(_[a-z])?_(\w+)"
    USER_TAGS = []
    SHOW_TAGS = False

    link_to_assignment = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assignment = ""
        self.test_name = ""
        self._set_test_name_and_assignment()
        self.fail_msg = FailMessage(self._testMethodDoc)


    def __setattr__(self, name, value):
        """
        This is done so that we can send values to fail_msg and set in this instance.
        Mostly done for arguments and muli_arguments. Also work for norepr but there we return
        becaus it's value is only used in fail_msg.
        """
        if name == 'norepr':
            self.fail_msg.norepr = value
            return
        if name == '_argument':
            self.fail_msg.arguments = repr(value)
        if name == '_multi_arguments':
            self.fail_msg.arguments = ", ".join([repr(arg) for arg in value])
        super().__setattr__(name, value)



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



    def assert_setup(self, first, second, what_msgs):
        """
        Things to be done in each assert method
        """
        self.fail_msg.set_answers(first, second)
        if what_msgs:
            self.fail_msg.what_msgs_from_assert = what_msgs
        else:
            # if previous assert changed and didn't fail, we need this to reset
            # otherwise the previous change will be used
            self.fail_msg.what_msgs_from_assert = []




    def assertEqual(self, first, second, msg=None):
        """
        Check if first is equal to second. Save correct and student answer as to variables.
        First comes from student
        """
        self.assert_setup(first, second, msg)
        super().assertEqual(first, second, msg)



    def assertIn(self, member, container, msg=None):
        """
        Check if value in container.  Save correct and student answer as to variables.
        Container comes from student
        """
        self.assert_setup(container, member, msg)
        super().assertIn(member, container, msg)



    def assertFalse(self, expr, msg=None):
        """
        Check that the expression is False.
        Save correct and student answer as to variables.
        """
        self.assert_setup(expr, False, msg)
        super().assertFalse(expr, msg)



    def assertTrue(self, expr, msg=None):
        """
        Check that the expression is true.
        Save correct and student answer as to variables.
        """
        self.assert_setup(expr, True, msg)
        super().assertTrue(expr, msg)



    def assertNotIn(self, member, container, msg=None):
        """
        Check that the expression is true.
        Save correct and student answer as to variables.
        """
        self.assert_setup(container, member, msg)
        super().assertNotIn(member, container, msg)

    def assertModule(self, module, module_path=None, msg=None):
        """
        Check that module can be imported.
        Save correct and student answer as to variables.
        """
        self.assert_setup(module_path, module, msg)
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
        self.assert_setup(obj, attr, msg)
        try:
            getattr(obj, attr)
        except AttributeError as e:
            msg = self._formatMessage(msg, f"attribute {attr} not found in object {obj}")
            raise self.failureException(msg) from e



    def assertRaises(self, expected_exception, *args, msg=None, **kwargs): # pylint: disable=arguments-differ
        """
        assertRaises is a context and therefore we need to return it
        """
        self.assert_setup("", expected_exception, msg)
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
        self.assert_setup(first, second, msg)
        super().assertCountEqual(first, second, msg)



    def assertOrder(self, order, container, msg=None):
        """
        Check that in index of elements in order are lowest to highest in container.
        Save correct and student answer as to variables.
        """
        self.assert_setup(container, order, msg)

        try:
            for i in range(len(order)-1):
                if not container.index(order[i]) < container.index(order[i+1]):
                    raise ValueError
        except ValueError as e:
            msg = self._formatMessage(msg, f"Index of elemnts in {order} don't appear in correct order in {container}")
            raise self.failureException(msg) from e
