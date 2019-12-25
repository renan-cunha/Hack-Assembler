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


