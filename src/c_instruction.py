from typing import Tuple

dest_table = {"null": "000",
              "M": "001",
              "D": "010",
              "MD": "011",
              "A": "100",
              "AM": "101",
              "AD": "110",
              "AMD": "111"}

jump_table = {"null": "000",
              "JGT": "001",
              "JEQ": "010",
              "JGE": "011",
              "JLT": "100",
              "JNE": "101",
              "JLE": "110",
              "JMP": "111"}

comp_table = {"0": "0101010",
              "1": "0111111",
              "-1": "01110101",
              "D": "0001100",
              "A": "0110000",
              "!D": "0001101",
              "!A": "0110001",
              "-D": "0001111",
              "-A": "0110011",
              "D+1": "0011111",
              "A+1": "0110111",
              "D-1": "0001110",
              "A-1": "0110010",
              "D+A": "0000010",
              "D-A": "0010011",
              "A-D": "0000111",
              "D&A": "0000000",
              "D|A": "0010101",
              "M": "1110000",
              "!M": "1110001",
              "-M": "1110011",
              "M+1": "1110111",
              "M-1": "1110010",
              "D+M": "1000010",
              "D-M": "1010011",
              "M-D": "1000111",
              "D&M": "1000000",
              "D|M": "1010101"}


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


def get_jump(string: str) -> str:
    jump_index = string.find(";")
    if jump_index == -1:
        return "null"
    else:
        return string[jump_index+1:]


def get_c_instruction_fields(string: str) -> Tuple[str, str, str]:
    dest = get_dest(string)
    comp = get_comp(string)
    jump = get_jump(string)
    return dest, comp, jump


def convert_c(string: str) -> str:
    dest, comp, jump = get_c_instruction_fields(string)
    dest = dest_table[dest]
    comp = comp_table[comp]
    jump = dest_table[jump]
    return "111" + comp + dest + jump
