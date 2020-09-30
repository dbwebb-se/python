"""
COntain functions for modifying strings
"""
def case_switch(letter):
    """
    Change uppers to lowers and lowers to uppers
    """
    if letter.isupper():
        return letter.lower()
    return letter.upper()
