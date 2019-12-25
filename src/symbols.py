def is_label(string: str) -> bool:
    if string[0] == "(":
        return True
    return False


def get_label(string: str) -> str:
    return string[1:-1]
