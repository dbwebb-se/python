"""
Custom test collecter, builder and runner used for examining students.
"""
import unittest
import re
from examiner.exceptions import ContactError
from examiner.exam_test_result import ExamTestResult
from examiner.exam_test_result_exam import ExamTestResultExam
from examiner import ExamTestCaseExam
from examiner.cli_parser import parse
from examiner.helper_functions import get_testfiles, import_module
from examiner import sentry


PASS = 1
NOT_PASS = 0
ARGS = parse()
RESULT_CLASS = ExamTestResult

def get_testsuites_from_file(path_and_name):
    """
    Create TestSuite with testcases from a file
    """
    path, name = path_and_name
    module = import_module(path, name)

    tl = unittest.TestLoader()

    testsuite = tl.loadTestsFromModule(module)
    return testsuite


def build_testsuite():
    """
    Create TestSuit with testcases.
    """
    global RESULT_CLASS
    all_suites = unittest.TestSuite()

    for path_and_name in get_testfiles(ARGS.what, ARGS.extra_assignments):
        filesuites = get_testsuites_from_file(path_and_name)

        for suite in filesuites:
            for case in suite:
                case.USER_TAGS = ARGS.tags
                case.SHOW_TAGS = ARGS.show_tags
                #  under nog vara en bugg. har inte testa om det funkar med Exam tester då vi använder det längre
                if issubclass(type(case), ExamTestCaseExam):
                    RESULT_CLASS = ExamTestResultExam
            all_suites.addTest(suite)
    return all_suites



def run_testcases(suite):
    """
    Run testsuit.
    """
    runner = unittest.TextTestRunner(resultclass=RESULT_CLASS, verbosity=2, failfast=ARGS.failfast, descriptions=False)

    try:
        results = runner.run(suite)
    except Exception as e:
        raise ContactError() from e

    return results



def main():
    """
    Start point of program.
    """
    sentry.activate_sentry(
        ARGS.sentry_url,
        ARGS.sentry_release,
        ARGS.sentry_sample_rate,
        ARGS.sentry_user,
        re.findall(r"kmom\d\d", ARGS.what)[0]
    )
    suite = build_testsuite()
    results = run_testcases(suite)
    results.exit_with_result()



if __name__ == "__main__":
    main()
