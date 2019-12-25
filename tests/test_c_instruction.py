import pytest
from src.c_instruction import get_dest, get_comp


get_dest_data = [
    ("MD=D+1", "MD"),
    ("D+1",  "null"),
    ("D;JMP",  "null"),
]

@pytest.mark.parametrize("input,expected", get_dest_data)
def test_get_dest(input, expected):
    assert get_dest(input) == expected


get_comp_data = [
    ("MD=D+1", "D+1"),
    ("D+1",  "D+1"),
    ("D;JMP",  "D"),
    ("MD=D+1;JMP", "D+1"),
]

@pytest.mark.parametrize("input,expected", get_comp_data)
def test_get_comp(input, expected):
    assert get_comp(input) == expected
