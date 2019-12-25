from typing import Dict


def get_dest(string: str) -> str:
    equal_index = string.find("=")
    if equal_index == -1:
        return "null"
    else:
        return string[:equal_index]

#def get_c_instruction_fields(string: str) -> Dict[str, str]:
