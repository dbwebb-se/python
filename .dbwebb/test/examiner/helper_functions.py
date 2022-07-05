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
    from examiner.colorama import init, Fore, Style
except ImportError:
    from colorama import init, Fore, Style

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



def check_for_tags(*tag_args, default_msg="Does not include any of the given tags"):
    """
    Compares the user tags and the test_case tags to see which tests
    should be be ran.
    """
    def skip_function(msg=default_msg):
        """
        replaces test_cases so they are skipped
        """
        raise SkipTest(msg)

    def decorator(f):
        """Decorator for overwriting test_case functions"""

        @wraps(f)
        def wrapper(self, *args, **kwargs):
            """Wrapper"""
            test_case_tags = set(tag_args)

            if self.SHOW_TAGS:
                return skip_function(f"has the tags: {', '.join(sorted(test_case_tags))}")

            user_tags = set(self.USER_TAGS)
            if user_tags:
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
