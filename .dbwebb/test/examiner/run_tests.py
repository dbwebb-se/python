"""
Custom test collecter, builder and runner used for examining students.
"""
import unittest
from examiner.exceptions import ContactError
from examiner.exam_test_result import ExamTestResult
from examiner.exam_test_result_exam import ExamTestResultExam
from examiner.exam_test_case import ExamTestCase
from examiner import ExamTestCaseExam
from examiner.cli_parser import parse
from examiner.helper_functions import get_testfiles, import_module


PASS = 1
NOT_PASS = 0
ARGS = parse()
RESULT_CLASS = ExamTestResult

def get_testcases(path_and_name):
    """
    Add all TestCases to a list and return.
    """
    global RESULT_CLASS
    testcases = []
    testMethodPrefix = "Test"
    path, name = path_and_name
    module = import_module(path, name)
    for attrname in dir(module):
        if not attrname.startswith(testMethodPrefix):
            continue
        testClass = getattr(module, attrname)
        if issubclass(testClass, ExamTestCase):
            testcases.append(testClass)
        else:
            raise TypeError(f"Test case is not subclass of ExamTestCase. It has class {type(testClass)}")

    if issubclass(testClass, ExamTestCaseExam):
        RESULT_CLASS = ExamTestResultExam

    return testcases



def build_testsuite():
    """
    Create TestSuit with testcases.
    """
    suite = unittest.TestSuite()
    for path_and_name in get_testfiles(ARGS.what, ARGS.extra_assignments):
        testcases = get_testcases(path_and_name)

        for case in testcases:
            case.USER_TAGS = ARGS.tags
            case.SHOW_TAGS = ARGS.show_tags
            suite.addTest(unittest.makeSuite(case))
    return suite



def run_testcases(suite):
    """
    Run testsuit.
    """
    runner = unittest.TextTestRunner(resultclass=RESULT_CLASS, verbosity=2, failfast=ARGS.failfast)

    try:
        results = runner.run(suite)
    except Exception as e:
        raise ContactError() from e

    return results



def main():
    """
    Start point of program.
    """
    suite = build_testsuite()
    results = run_testcases(suite)
    results.exit_with_result()



if __name__ == "__main__":
    main()
