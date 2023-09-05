"""
Create a method for each type of common error.
Use common_errors to connect the method to an exception type.
"""
from examiner.cli_parser import parse
from examiner.helper_functions import COLORS

ARGS = parse()

def check_if_common_error(exc_name, tb_exc, _):
    """
    Call all methods connected to an exception type.
    Return str from method if returned.
    Para _ should be "msg" if we find a use for it. Is "_" to pass validation
    """
    common_errors = {
        "StopIteration": [
            wrong_nr_of_input_calls,
        ],
        "AssertionError": [
            assertion_traceback,
        ],
    }
    try:
        methods = common_errors[exc_name]
    except KeyError:
        return ""
    for method in methods:
        res = method(tb_exc)
        if res:
            return COLORS["BL"]+COLORS["BR"]+res+COLORS["RE"]
    return ""



def wrong_nr_of_input_calls(tb_exc):
    """
    Check if the exception match where the student make to many input() calls.
    """
    help_msg = (
        "(Tips! Det är vanligt att få detta felet om man gör fler "
        "anrop till funktionen input() än vad det står i uppgiften.)"
    )
    tb_str = "\n".join(list(tb_exc.format()))
    if "input(" in tb_str:
        if "mock_call" in tb_str:
            if "result = next(effect)" in tb_str:
                return help_msg
    return ""



def assertion_traceback(tb_exc):
    """
    Catch errors if --trace flag is set
    """
    if ARGS.trace_assertion_error:
        traceback = "\n".join(list(tb_exc.format()))

        return COLORS["M"] + "\n" + traceback + COLORS["RE"]
    return ""
