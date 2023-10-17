from src.main import fizz_buzz_output_generator
from src.schema import FizzBuzzInput


def test_fizz_buzz_output_generator():
    fb_input = FizzBuzzInput(lower_bound=1, upper_bound=15)
    output = fizz_buzz_output_generator(fb_input)
    output_list = list(output)
    assert output_list == [
        '1', '2', '3 fizz', '4', '5 buzz', '6 fizz', '7', '8', '9 fizz', '10 buzz',
        '11', '12 fizz', '13', '14', '15 fizz buzz'
    ]
