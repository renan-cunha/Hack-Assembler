import re


def remove_whitespaces(string: str) -> str:
    return string.replace(" ", "")


def remove_comments(string: str) -> str:
    return re.sub(r"//.*", "", string)


def remove_blank_lines(string: str) -> str:
    while True:
        new_string = string.replace("\n\n", "\n")
        if new_string == string:
            break
        string = new_string

    return new_string.lstrip("\n")


def clean_code(string: str) -> str:
    string = remove_whitespaces(string)
    string = remove_comments(string)
    string = remove_blank_lines(string)
    return string
