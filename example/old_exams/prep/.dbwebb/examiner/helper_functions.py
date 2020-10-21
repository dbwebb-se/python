"""
pass
"""
import re
import hashlib
try:
    from examiner.colorama import init, Fore, Back, Style
except ImportError:
    from colorama import init, Fore, Back, Style

init(strip=False)


COLOR_REGEX_START = r"\|(\w)\|"
COLOR_REGEX_STOP = r"\|/(\w)\|"
COLORS = {
    "G": Fore.GREEN,
    "B": Fore.BLACK,
    "R": Fore.RED,
    "Y": Fore.YELLOW,
    "BL": Fore.BLUE,
    "M": Fore.MAGENTA,
    "C": Fore.CYAN,
    "W": Fore.WHITE,
    "RE": Fore.RESET,
}


def list_to_hash(error):
    """
    hash a list
    """
    hash_obj = hashlib.sha1(bytes("".join(error), "utf-8"))
    return hash_obj.hexdigest()



def clean_str(string):
    """
    Remove cluther form students answer string.
    """
    return string.replace(chr(27) + "[2J" + chr(27) + "[;H", "")


def get_color_indexes(msg_list):
    """
    Return index of lines with {correct} (green) and {student} (red).
    """
    indexes = {}
    for i, line in enumerate(msg_list):
        if "{correct}" in line:
            indexes["green"] = i - 1
        elif "{student}" in line:
            indexes["red"] = i - 1

    return indexes



def inject_answer_colors(msg_list):
    """
    Insert red and green color if "correct" and "student" is present in doscring.
    """
    indexes = get_color_indexes(msg_list)
    if "green" in indexes:
        i = indexes["green"]
        msg_list[i] = (
            Back.BLACK + Fore.GREEN + Style.BRIGHT
            + msg_list[i]
            + Style.RESET_ALL
        )
    if "red" in indexes:
        i = indexes["red"]
        msg_list[i] = (
            Back.BLACK + Fore.RED + Style.BRIGHT
            + msg_list[i]
            + Style.RESET_ALL
        )

    return msg_list



def inject_regex_colors(msg):
    """
    Use regex to find |<color letter>| and replace with colors.
    """
    color_start = re.findall(COLOR_REGEX_START, msg)
    for color in color_start:
        msg = msg.replace("|{}|".format(color), COLORS[color]+ Style.BRIGHT)
    msg = msg.replace("|/RE|", COLORS["RE"])
    return msg



def create_fail_msg(function_args, test):
    """
    Create formated fail msg using docstring from test function
    """
    #pylint: disable=protected-access
    if test._testMethodDoc is None:
        raise AttributeError(
            "Test is missing docstring."
            " Docstring is needed to explainin the test when Something goes wrong."
        )
    docstring = re.sub("\n +", "\n", test._testMethodDoc)

    msg_list = docstring.split("\n")
    inject_answer_colors(msg_list)
    msg = "\n".join(msg_list)
    msg = inject_regex_colors(msg)

    return [msg.format(
        arguments=function_args,
        correct=test.correct_answer,
        student=test.student_answer
    )]
    #pylint: enable=protected-access



def get_function_args(test):
    """
    Use repr() on arguments used for the students defined function.
    If no arguments is used, return None.
    """
    try:
        return repr(getattr(test, "_argument"))
    except AttributeError:
        try:
            return ", ".join([repr(arg) for arg in getattr(test, "_mult_arguments")])
        except AttributeError:
            return None



def error_is_missing_assignment_function(error):
    """
    Returns True if the error is missing function for an assignment in the
    students code.
    """
    _, value, tb = error
    if "module 'exam' has no attribute" in str(value):
        while tb.tb_next:
            tb = tb.tb_next
        filename = tb.tb_frame.f_code.co_filename.split("/")[-1]
        if filename == "test_exam.py":
            return True
    return False
