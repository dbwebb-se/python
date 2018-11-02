"""
Module for analyze datetime functions
"""



def validate_date_string(index, text):
    """
    Validate dates in text
    """
    spaces = text[index-5] + text[index+6]
    if spaces in ("  ", " .", " ,"):
        year = int(text[index-4:index])
        if year > -1:
            month = int(text[index+1:index+3])
            if 0 < month < 13 and text[index+3] == "-":
                day = int(text[index+4:index+6])
                if 0 < day < 32:
                    return text[index-4:index+6]
    return False



def find_dates():
    """
    FInd valid dates
    """
    text = read_file()
    valid = []
    for i, c in enumerate(text):
        # Find "-" which we use identifier for possible dates
        if c == "-":
            try:
                date = validate_date_string(i, text)
                if date:
                    valid.append(date)
            except ValueError:
                continue
    print(", ".join(valid))

    return True



def validate_time_string(index, text):
    """
    Validate substring for times
    """
    spaces = text[index-3] + text[index+3]
    if spaces in ("  ", " ,", " ."):
        hour = int(text[index-2:index])
        if -1 < hour < 24:
            minute = int(text[index+1:index+3])
            if -1 < minute < 60:
                return text[index-2:index+3]
    return False



def find_times():
    """
    Find valid times
    """
    text = read_file()
    valid = []
    for i, c in enumerate(text):
        # Find ":" which we use identifier for possible times
        if c == ":":
            try:
                time = validate_time_string(i, text)
                if time:
                    valid.append(time)
            except ValueError:
                continue
    print(", ".join(valid))



def read_file():
    """
    Read file
    """
    with open("value-of-time.txt", "r") as fh:
        return fh.read()



if __name__ == "__main__":
    find_dates()
    find_times()
