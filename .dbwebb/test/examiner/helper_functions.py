"""
pass
"""
import re
import hashlib
import os
from functools import wraps
from unittest import SkipTest
import importlib.util as importer
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
    "BR": Style.BRIGHT,
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
            return ", ".join([repr(arg) for arg in getattr(test, "_multi_arguments")])
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



def check_for_tags(*tag_args, msg="Inkluderar inte någon av de givna taggarna"):
    """
    Compares the user tags and the test_case tags to see which tests
    should be be ran.
    """
    def skip_function():
        """
        replaces test_cases so they are skipped
        """
        raise SkipTest(msg)

    def decorator(f):
        """Decorator for overwriting test_case functions"""

        @wraps(f)
        def wrapper(self, *args, **kwargs):
            """Wrapper"""
            user_tags = set(self.USER_TAGS)
            if user_tags:
                test_case_tags = set(tag_args)
                if not user_tags.intersection(test_case_tags):
                    return skip_function()
            return f(self, *args, **kwargs)
        wrapper.__wrapped__ = f # used to assert that method has been decorated
        return wrapper
    return decorator



def find_test_folders(root):
    """
    Recursively looks for folder names matching test_folder
    starting from where the script is called and returns the paths.
    """
    test_dirs = [root]

    for path, dirs, _files in os.walk(root):
        for dir_ in dirs:
            if dir_ != "__pycache__":
                test_dirs.append(os.path.join(path, dir_))
    return test_dirs



def get_testfiles(root=None, extra_assignments=False):
    """
    Gets a list of tuples (path and the testfiles basename) for all
    test_folders.
    """
    base_test_pattern = r"test_(\w)*.py"
    extra_test_pattern = r"extra_test_(\w)*.py"

    test_folders = find_test_folders(root)
    tests = []
    for dir_ in test_folders:
        pattern = extra_test_pattern if extra_assignments else base_test_pattern
        tests.extend([(dir_, file[:-3]) for file in os.listdir(dir_) if re.match(pattern, file)])

    return tests



def import_module(proj_path, module_name):
    """
    Loads a module from the given path and name.
    If obligatory_functions is missing Raise exception.
    """
    spec = importer.spec_from_file_location(
        module_name, f"{proj_path}/{module_name}.py"
    )
    module = importer.module_from_spec(spec)

    spec.loader.exec_module(module)
    return module



def find_path_to_assignment(test_file_location):
    """
    Takes a testfiles location and calculates the path to the assignment,
    given that it has .dbwebb has the same structure as the me folder.
    """
    FILE_DIR_LIST = test_file_location.split("/")
    FILE_DIR_LEN = len(FILE_DIR_LIST) - 1
    FOLDERS_TO_BACK = FILE_DIR_LEN - FILE_DIR_LIST.index('suite.d')
    COURSE_REPO_ROOT = '../' * (FOLDERS_TO_BACK + 3)
    KMOM_AND_ASSIGNENT = "/".join(FILE_DIR_LIST[-(FOLDERS_TO_BACK):])
    return f"{test_file_location}/{COURSE_REPO_ROOT}me/{KMOM_AND_ASSIGNENT}"
