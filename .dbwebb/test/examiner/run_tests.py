"""
Custom test collecter, builder and runner used for examining students.
"""
import io
import unittest
from collections import OrderedDict
from exceptions import ContanctError
from exam_test_result import ExamTestResult
from exam_test_case import ExamTestCase
from cli_parser import parse
from helper_functions import get_testfiles, import_module


PASS = 1
NOT_PASS = 0
ARGS = parse()


def get_testcases(assignments, path_and_name):
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
            # remove "TestX"
            assignments[str(attrname)[5:]] = {
                "pass": NOT_PASS,
            }
    return testcases



def build_testsuite(assignments):
    """
    Create TestSuit with testcases.
    """

    suite = unittest.TestSuite()
    for path_and_name in get_testfiles(ARGS.what, ARGS.extra_assignments):
        testcases = get_testcases(assignments, path_and_name)

        for case in testcases:
            case.USER_TAGS = ARGS.tags
            suite.addTest(unittest.makeSuite(case))
    return suite



def run_testcases(suite):
    """
    Run testsuit.
    """
    buf = io.StringIO()
    runner = unittest.TextTestRunner(resultclass=ExamTestResult, verbosity=2, stream=buf)
    # i think this is used to see print()'s
    # runner = unittest.TextTestRunner(resultclass=ExamTestResult, verbosity=2)

    try:
        assignments_results = runner.run(suite).assignments_results
    except Exception as e:
        raise ContanctError() from e

    return buf.getvalue(), assignments_results



def check_pass_fail(assignments, result):
    """
    Mark assignments as Passed if they succeded.
    """
    for assignment, outcome in result.items():
        if outcome["started"] == outcome["success"]:
            assignments[assignment]["pass"] = PASS



def format_output(output, assignments):
    """
    Print and format test run and which assignments pass/fail.
    """
    result = " ".join([str(res["pass"]) for res in assignments.values()])
    print(result)
    print(output)



def main():
    """
    Start point of program.
    """
    assignments = OrderedDict() # OrderedDict used for backwards compability
    suite = build_testsuite(assignments)
    output, assignments_results = run_testcases(suite)
    check_pass_fail(assignments, assignments_results)
    format_output(output, assignments)



if __name__ == "__main__":
    main()
