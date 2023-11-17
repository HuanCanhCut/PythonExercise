import re

def floatRegex (value) :
    regex = r'^-?\d+(\.\d+)?$'
    return re.match(regex, value)
