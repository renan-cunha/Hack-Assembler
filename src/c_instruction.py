from typing import Dict


def get_dest(string: str) -> str:
    equal_index = string.find("=")
    if equal_index == -1:
        return "null"
    else:
        return string[:equal_index]


def get_comp(string: str) -> str:
    equal_index = string.find("=")
    jump_index = string.find(";")
    cond1 = equal_index != -1
    cond2 = jump_index != -1
    if not cond1 and not cond2:
        return string
    elif not cond1 and cond2:
        return string[:jump_index]
    elif cond1 and not cond2:
        return string[equal_index+1:]
    else:
        return string[equal_index+1:jump_index]

#def get_c_instruction_fields(string: str) -> Dict[str, str]:
