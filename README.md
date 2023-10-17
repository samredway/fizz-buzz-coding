# Coding challenge

#### Business Requirements

1. Take two integers between 1 and 100

3. Loop from the first integer to the second integer

4. Write out each integer

5. If the integer is divisible by 3 also print out ‘fizz’

6. If the integer is divisible by 5 also print out ‘buzz’


#### Development Requirements

1. Before you write any code write some unit tests

2. As we are developing enterprise software, we will be paying particular attention to:
    
    a. Code clarity and ease of understanding

    b. Well commented code that gives clear and appropriate explanations
    
    c. Code that shows an understanding of Enterprise Software development requirements. i.e., we are just as interested in failure modes as in the happy path


## Setup

This was written with python 3.11.1

This code has a dependencies that you can install into your environment by doing the following from the terminal:

    pip install -r requirements.txt

## Running the tests

From the terminal do:

    PYTHONPATH=src pytest test/


## Running fizz buzz from terminal

From the terminal do:

    python src/main.py a b

where a and b are 2 integers which conform to the validation requirements.

for help you can do:

    python src/main.py -h

# NOTE:

- For the sake of clarity I have mde the two integers named variables one of which
is the lower bound and the other the upper bound rather than 2 unnamed variables.

- I chose to interpret 1-100 as being 1-100 inclusive rather than exclusive, both 
of these choices would have been checked with a product manager or clarified when
handed the spec in real life.
