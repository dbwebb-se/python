"""
Custom test collecter, builder and runner used for examining students.
"""
import sys
import unittest
from examiner.exceptions import ContanctError
from examiner.exam_test_result import ExamTestResult
from examiner.exam_test_case import ExamTestCase
from examiner.cli_parser import parse
from examiner.helper_functions import get_testfiles, import_module


PASS = 1
NOT_PASS = 0
ARGS = parse()


def get_testcases(path_and_name):
    """
    Add all TestCases to a list and return.
    """
    testcases = []
    testMethodPrefix = "Test"
    path, name = path_and_name
    module = import_module(path, name)
    for attrname in dir(module):
        if not attrname.startswith(testMethodPrefix):
            continue
        testClass = getattr(module, attrname)
        # Should use isinstance. But it return False, don't know why.
        if testClass.__base__ is ExamTestCase:
            testcases.append(testClass)
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
            suite.addTest(unittest.makeSuite(case))
    return suite



def run_testcases(suite):
    """
    Run testsuit.
    """
    runner = unittest.TextTestRunner(resultclass=ExamTestResult, verbosity=2)

    try:
        results = runner.run(suite)
    except Exception as e:
        raise ContanctError() from e

    return results



def exit_with_result(results):
    """
    Exit with status code based on if tests passed or not
    """
    sys.exit(not results.wasSuccessful())



def main():
    """
    Start point of program.
    """
    suite = build_testsuite()
    results = run_testcases(suite)
    exit_with_result(results)



if __name__ == "__main__":
    main()
