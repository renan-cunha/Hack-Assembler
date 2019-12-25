import pytest
from src.c_instruction import get_dest


get_dest_data = [
    ("MD=D+1", "MD"),
    ("D+1",  "null"),
    ("D;JMP",  "null"),
]

@pytest.mark.parametrize("input,expected", get_dest_data)
def test_get_dest(input, expected):
    assert get_dest(input) == expected
