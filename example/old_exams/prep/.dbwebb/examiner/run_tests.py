"""
Custom test collecter, builder and runner used for examining students.
"""
import io
import unittest
from collections import OrderedDict
import test_exam
from examiner.exam_test_result import ExamTestResult
from examiner.exam_test_case import ExamTestCase
from examiner.exceptions import ContanctError



PASS = 1
NOT_PASS = 0



def get_testcases(assignments):
    """
    Add all TestCases to a list and return.
    """
    testcases = []
    testMethodPrefix = "Test"

    for attrname in dir(test_exam):
        if not attrname.startswith(testMethodPrefix):
            continue
        testClass = getattr(test_exam, attrname)
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
    testcases = get_testcases(assignments)
    suite = unittest.TestSuite()
    for case in testcases:
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
