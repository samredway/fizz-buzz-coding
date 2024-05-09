"""
1. Take two integers between 1 and 100 (inclusive)

2. Loop from the first integer to the second integer

3. Write out each integer

4. If the integer is divisible by 3 also print out ‘fizz’

5. If the integer is divisible by 5 also print out ‘buzz’
"""

import argparse
from typing import Generator

from schema import FizzBuzzInput


def fizz_buzz_output_generator(fizz_buzz_input: FizzBuzzInput) -> Generator[str, None, None]:
    """
    Returns a generator object producing strings which conform to the required
    output defined by the fizz buzz rules in module doc string.
    """
    for i in range(fizz_buzz_input.lower_bound, fizz_buzz_input.upper_bound + 1):
        output_line = f'{i}'
        if i % 3 == 0:
            output_line += ' fizz'
        if i % 5 == 0:
            output_line += ' buzz'
        yield output_line


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate fizz buzz output from two ints (a lower and upper bound)')
    parser.add_argument('lower_bound', help='Integer between 1-100 (inclusive)', type=int)
    parser.add_argument('upper_bound', help='Integer between 1-100 (inclusive)', type=int)
    args = parser.parse_args()

    validated_input = FizzBuzzInput(lower_bound=args.lower_bound, upper_bound=args.upper_bound)
    print(line for line in fizz_buzz_output_generator(validated_input))
