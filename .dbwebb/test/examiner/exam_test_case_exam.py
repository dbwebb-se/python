"""
Overriding TestCase for exam tool.
"""
from examiner.exam_test_case import ExamTestCase

class ExamTestCaseExam(ExamTestCase):
    """
    Custom class for examination.
    Can set points for assignments and a threshold for passing.
    """

    points_for_pass = -1
    points_worth = 0
