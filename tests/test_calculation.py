import pytest
from lib.calculation import square_number

# simple test that makes sure square_number function works as expected
@pytest.mark.parametrize("test_input,expected", [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)])
def test_square_number(test_input, expected):
    assert square_number(test_input) == expected