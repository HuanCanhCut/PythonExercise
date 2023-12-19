import re 

def isInteger (value):
    regex = r'^[0-9]+$'
    return re.fullmatch(regex, value)

def isEmail (value):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(regex, value)