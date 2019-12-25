from src.clean_program import clean_code
from src.c_instruction import convert_c
from src.a_instruction import convert_a, is_a_instruction
import sys


if __name__ == "__main__":
    args = sys.argv
    machine_file_name = args[1]
    binary_file_name = args[2]
    with open(machine_file_name, "r") as machine_file:
        machine_string = machine_file.read()
    machine_string = clean_code(machine_string)
    machine_lines = machine_string.split("\n")

    with open(binary_file_name, "w") as binary_file:
        for line in machine_lines:
            if is_a_instruction(line):
                binary_line = convert_a(line)
            else:
                binary_line = convert_c(line)
            binary_file.write(binary_line+"\n")




