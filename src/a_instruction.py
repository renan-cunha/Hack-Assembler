

def is_a_instruction(string: str) -> bool:
    if string.startswith("@"):
        return True
    return False


def convert_a(string: str) -> str:
    decimal_number = int(string[1:])
    bin_number = bin(decimal_number)
    bin_str = str(bin_number)[2:]
    size = 15
    zeros = "0"*(size-len(bin_str))
    bin_str = zeros+bin_str
    return "0" + bin_str


