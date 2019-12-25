
pre_defined_symbols = {"SCREEN": "16384",
                       "KBD": "24576",
                       "SP": "0",
                       "LCL": "1",
                       "ARG": "2",
                       "THIS": "3",
                       "THAT": "4"}


def is_a_instruction(string: str) -> bool:
    if string.startswith("@"):
        return True
    return False


def convert_a(string: str) -> str:
    string = string[1:]
    if not string.isdigit():
        if string[0] == "R":
            string = string[1:]
        else:
            string = pre_defined_symbols[string]
    decimal_number = int(string)
    bin_number = bin(decimal_number)
    bin_str = str(bin_number)[2:]
    size = 15
    zeros = "0"*(size-len(bin_str))
    bin_str = zeros+bin_str
    return "0" + bin_str