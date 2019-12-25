import pytest
from src.a_instruction import convert_a, is_a_instruction


check_a = [
    ("@21", True),
    ("@0", True),
    ("0", False),
    ("D=M;JMP", False),
    ("D;", False),
    ("D=M;", False),
]

@pytest.mark.parametrize("input,expected", check_a)
def test_check_a(input, expected):
    assert is_a_instruction(input) == expected


convert_a_data = [
    ("@21", "0000000000010101"),
    ("@0",  "0000000000000000"),
    ("@1",  "0000000000000001"),
]

@pytest.mark.parametrize("input,expected", convert_a_data)
def test_convert_a(input, expected):
    assert convert_a(input) == expected
