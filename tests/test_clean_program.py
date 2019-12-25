import pytest
from src.clean_program import remove_whitespaces
from src.clean_program import remove_comments
from src.clean_program import clean_code
import os


white_space_data = [
    ("hello world", "helloworld"),
    (" helloworld", "helloworld"),
    ("helloworld", "helloworld"),
    ("helloworld ", "helloworld"),
    ("  hello      world ", "helloworld"),
    ("  hello\n      world ", "hello\nworld"),
    ("  hello\n      world ", "hello\nworld"),
]

@pytest.mark.parametrize("input,expected", white_space_data)
def test_remove_whitespaces(input, expected):
    assert remove_whitespaces(input) == expected

comment_data = [
    ("helloworld//", "helloworld"),
    ("helloworld// frfeegege", "helloworld"),
    ("helloworld//fwefwefewfwe", "helloworld"),
    ("//fwefwefwefwef", ""),
    ("//fwefewfewfe\nhelloworld", "\nhelloworld"),
    ("helloworld\n//uehuhewuhfuhew", "helloworld\n"),
]

@pytest.mark.parametrize("input,expected", comment_data)
def test_remove_comments(input, expected):
    assert remove_comments(input) == expected


def test_clean_program():
    file_name = "Fill.asm"
    file_path = os.path.join(__file__, "..", file_name)
    file_path = os.path.abspath(file_path)
    with open(file_path, "r") as file:
        string = file.read()
    file_name = "CleanFill.asm"
    file_path = os.path.join(__file__, "..", file_name)
    file_path = os.path.abspath(file_path)
    with open(file_path, "r") as file:
        clean_string = file.read()
    output = clean_code(string)
    print(f"output {output[-1]}")
    print(f"results {clean_string[-1]}")
    assert output == clean_string
