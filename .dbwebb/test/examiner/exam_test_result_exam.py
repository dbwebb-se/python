"""
Custom unittest.TextTestResult class. Is used to customize the output from unittests.
"""
import sys
from examiner.exam_test_result import ExamTestResult
try:
    from examiner.colorama import init, Fore, Back, Style
except ImportError:
    from colorama import init, Fore, Back, Style

init(strip=False)



class ExamTestResultExam(ExamTestResult):
    """
    Implementation of TextTestResult to use MyTestResult to create custom output for tests.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points_for_pass = -1
        self.nr_of_points = 0



    def startTest(self, test):
        """
        Get points needed for passing and how many points each assignment is worth.
        """
        super().startTest(test)
        self.assignments_results[test.assignment]["points"] = test.points_worth
        if self.points_for_pass != -1 and self.points_for_pass != test.points_for_pass and test.points_for_pass > -1:
            raise ValueError(
                "There are multiple values for 'points_for_pass' in the test cases."
                "\nThere can only a value for it in one of the test case for all tests."
            )
        if test.points_for_pass > -1:
            self.points_for_pass = test.points_for_pass



    def stopTestRun(self):
        """
        Called once after all tests are executed.
        Calculate how many points was achieved.
        """
        for values in self.assignments_results.values():
            if values["started"] == values["success"]:
                self.nr_of_points += values["points"]
                values["passed"] = True
            else:
                values["passed"] = False



    def wasSuccessful(self):
        """
        Base successfulness on points instead of if all tests are passed.
        """
        return self.nr_of_points >= self.points_for_pass



    def exit_with_result(self):
        """
        Exit with summary text, where we show if they have enough points for passing.
        """
        for assignment, values in self.assignments_results.items():
            self.stream.writeln(
                f"{assignment} - {'solved' if values['passed'] else 'not solved'}"
            )

        if self.wasSuccessful():
            text = (
                Back.GREEN + Style.BRIGHT + Fore.WHITE+\
                f"Passed{Style.RESET_ALL} - You have achieved {self.nr_of_points} points."
                " This places you above the limit for a passing score."
                f" The limit for passing is {self.points_for_pass} points."
            )
        else:
            text = (
                Back.RED + Style.BRIGHT + Fore.WHITE+\
                f"Not passed{Style.RESET_ALL} - You have achieved {self.nr_of_points} points. "
                " This places you below the limit for a passing score."
                f" The limit for passing is {self.points_for_pass} points."
            )

        self.stream.writeln(text)
        sys.exit(not self.wasSuccessful())
