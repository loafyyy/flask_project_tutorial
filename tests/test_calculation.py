import pytest
import mock
from lib.calculation import Exponentiator, generate_random_number

@pytest.fixture
def squarer():
    ''' return exponentiator that raises input to power of 2 '''
    return Exponentiator(power=2)

def test_square_number_no_decorators():
    ''' test simple test cases '''
    squarer = Exponentiator(power=2)
    assert squarer.exponentiate(0) == 0
    assert squarer.exponentiate(1) == 1
    assert squarer.exponentiate(2) == 4
    assert squarer.exponentiate(3) == 9
    assert squarer.exponentiate(4) == 16
    random_number = generate_random_number()
    assert squarer.exponentiate(random_number) == random_number ** 2

@pytest.mark.parametrize("test_input,expected", [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)])
def test_square_number(test_input, expected):
    ''' use pytest parametrization '''
    squarer = Exponentiator(power=2)
    assert squarer.exponentiate(test_input) == expected

def test_square_number_with_fixture(squarer):
    ''' use pytest fixtures '''
    assert squarer.exponentiate(5) == 25

@mock.patch("lib.calculation.generate_random_number")
@mock.patch("lib.calculation.Exponentiator")
def test_square_number_with_mock(mock_exponentiator, mock_generate_random_number):
    ''' use mocks '''
    mock_generate_random_number.return_value = 5
    random_number= mock_generate_random_number()
    assert random_number == 5
    mock_generate_random_number.assert_called_once()

    mock_exponentiator.exponentiate.return_value = "hi"
    result = mock_exponentiator.exponentiate(5)
    assert result == "hi"
    mock_exponentiator.exponentiate.assert_called_once_with(5)