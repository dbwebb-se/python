"""
Custom unittest.TextTestResult class. Is used to customize the output from unittests.
"""
import sys
import traceback
from unittest.result import failfast
from unittest.runner import TextTestResult
from examiner import common_errors
from examiner import helper_functions as hf
try:
    from examiner.colorama import init, Fore, Back, Style
except ImportError:
    from colorama import init, Fore, Back, Style

init(strip=False)

STDOUT_LINE = '\nStdout:\n%s'
STDERR_LINE = '\nStderr:\n%s'



class ExamTestResult(TextTestResult):
    """
    Implementation of TextTestResult to use MyTestResult to create custom output for tests.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assignments_results = {}



    def _exc_info_to_string(self, err, test):
        """
        Converts a sys.exc_info()-style tuple of values into a string.
        Creates custom msg for assertErrors, for the students.
        Code is copied from baseclass and then changed/added to.
        """
        exctype, value, tb = err
        # Skip test runner traceback levels
        while tb and self._is_relevant_tb_level(tb):
            tb = tb.tb_next

        #----------------------
        # here starts the interesting code, which we changed. If test failed
        # because of wrong answer from student
        tb_e = traceback.TracebackException(
            exctype, value, tb, limit=None, capture_locals=self.tb_locals)
        help_msg = common_errors.check_if_common_error(exctype.__name__, tb_e, value)

        if exctype is test.failureException:
            function_args = hf.get_function_args(test)

            msgLines = hf.create_fail_msg(
                function_args,
                test
            )
        else:
            msgLines = list(tb_e.format())

        if help_msg:
            msgLines.append(help_msg)
        #---------------------

        if self.buffer:
            # Dont care about this code
            output = sys.stdout.getvalue()
            error = sys.stderr.getvalue()
            if output:
                if not output.endswith('\n'):
                    output += '\n'
                msgLines.append(STDOUT_LINE % output)
            if error:
                if not error.endswith('\n'):
                    error += '\n'
                msgLines.append(STDERR_LINE % error)
        return ''.join(msgLines)



    def printErrors(self):
        """
        Overridden and is called from unittest framework
        """
        if self.dots or self.showAll:
            self.stream.writeln()
        if self.errors:
            self.printErrorListWithExplenation("Error", self.errors, "Your code crasched!", True)
        if self.failures:
            self.printErrorListWithExplenation("Fail", self.failures, "Your code produced wrong result!")



    def printErrorLines(self, error):
        """
        Print error and fails traceback
        """
        for line in error:
            self.stream.writeln("    |" + line)
        self.stream.writeln("    "  + Style.BRIGHT + self.separator2 + Style.RESET_ALL)



    def printErrorListWithExplenation(self, flavour, errors, explenation, is_errors=False):
        """
        Print errors grouped by assignment (TestCase object)
        """
        already_printed_assignments = {}

        self.stream.writeln(self.separator1)
        self.stream.writeln("{} section: {}".format(flavour.upper(), explenation))
        self.stream.writeln(self.separator1)
        for test, err in errors:
            if not test.assignment in already_printed_assignments:
                self.stream.writeln("{}{}s for {}{}".format(
                    Back.MAGENTA +Style.BRIGHT+ Fore.WHITE,
                    flavour,
                    test.assignment,
                    Style.RESET_ALL
                ))
                already_printed_assignments[test.assignment] = {}

            err_as_list = err.strip().split("\n")
            if is_errors:
                hex_dig = hf.list_to_hash(err_as_list[-3:])
                if hex_dig in already_printed_assignments[test.assignment]:
                    self.printErrorLines(["Hiding same error as above!"])
                else:
                    self.printErrorLines(err_as_list)
                    already_printed_assignments[test.assignment][hex_dig] = True
            else:
                self.printErrorLines(err_as_list)



    def startTestBase(self):
        """
        Base version of startTest, from unittest.TestResult.
        Super() calls the class inbetween this one and TestResult.
        """
        self.testsRun += 1
        self._mirrorOutput = False
        self._setupStdout()



    def startTest(self, test):
        """
        Summary print at beginning of output.
        Group output by Assignment.
        Counts number of tests run for each assignment.
        """
        if not test.assignment in self.assignments_results:
            self.assignments_results[test.assignment] = {
                "started": 0,
                "success": 0,
            }
            self.stream.write(f"{test.assignment} {test.link_to_assignment}\n")

        self.assignments_results[test.assignment]["started"] += 1

        self.startTestBase()

        MAX_TEST_FUNCNAME_LEN = 40
        TEST_INDENT = 4

        indent = " " * TEST_INDENT
        whitespace = "." * (MAX_TEST_FUNCNAME_LEN - len(test.test_name))
        self.stream.write(indent + test.test_name + whitespace)
        self.stream.write("... ")
        self.stream.flush()



    @failfast
    def addError(self, test, err):
        """Called when an error has occurred. 'err' is a tuple of values as
        returned by sys.exc_info().
        """
        if hf.error_is_missing_assignment_function(err):
            self.stream.writeln("Assignment Not Implemented")
            return
        self.errors.append((test, self._exc_info_to_string(err, test)))
        self._mirrorOutput = True
        self.stream.writeln("ERROR")



    def addSuccess(self, test):
        """
        Counts number of successfull run test for each assignment
        """
        super().addSuccess(test)
        self.assignments_results[test.assignment]["success"] += 1



    def exit_with_result(self):
        """
        Exit with status code based on if tests passed or not
        """
        sys.exit(not self.wasSuccessful())
