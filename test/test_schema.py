"""
Test validation logic in schema
"""

import pytest
from src.schema import FizzBuzzInput


@pytest.mark.parametrize(
    'lower_bound,upper_bound',
    [
        (1, 100),
        (5, 50),
        (90, 91),
    ],
)
def test_fiz_buzz_input(lower_bound: int, upper_bound: int) -> None:
    FizzBuzzInput(lower_bound=lower_bound, upper_bound=upper_bound)


def test_fizz_buzz_input_lower_bound_must_be_less_than_upper_bound() -> None:
    with pytest.raises(ValueError):
        FizzBuzzInput(lower_bound=100, upper_bound=1)


def test_fizz_buzz_input_upper_bound_must_be_less_than_100() -> None:
    with pytest.raises(ValueError):
        FizzBuzzInput(lower_bound=1, upper_bound=101)


@pytest.mark.parametrize('lower_bound', [-1, 0])
def test_fizz_buzz_input_lower_bound_must_be_more_than_0(lower_bound: int) -> None:
    with pytest.raises(ValueError):
        FizzBuzzInput(lower_bound=lower_bound, upper_bound=100)
