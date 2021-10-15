"""
Custom exceptions
"""
try:
    from examiner.colorama import init, Fore, Back, Style
except ImportError:
    from colorama import init, Fore, Back, Style
init(strip=False)

class ExamException(Exception):
    """
    Base exception for custom exception
    """



class TestFuncNameError(ExamException):
    """
    Error for when test function name is wrong
    """



class TestClassNameError(ExamException):
    """
    Error for when test class name is wrong
    """



class ContactError(ExamException):
    """
    Custom error. Used when there is an error in the test code and the
    student should contact the person responsible for the exam.
    """
    DEFAULT_MSG = (
        Style.BRIGHT + Back.BLACK + Fore.RED + "\n*********\n"
        "Något gick fel i rättningsprogrammet. "
        "Kontakta Ansvarig med ovanstående felmeddelandet!"
        "\n*********" + Style.RESET_ALL
    )

    def __init__(self, message=DEFAULT_MSG):
        self.message = message
        super().__init__(self.message)
