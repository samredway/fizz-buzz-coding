"""
Pydantic schemas for validating user input
"""

from pydantic import BaseModel, field_validator, model_validator


class FizzBuzzInput(BaseModel):
    lower_bound: int
    upper_bound: int

    @field_validator('lower_bound')
    @classmethod
    def lower_bound_must_not_be_less_than_1(cls, lower_bound: int) -> int:
        if lower_bound < 1:
            raise ValueError('The lower bound must not be less than 1')
        return lower_bound

    @field_validator('upper_bound')
    @classmethod
    def upper_bound_must_not_be_more_than_100(cls, upper_bound: int) -> int:
        if upper_bound > 100:
            raise ValueError('The upper bound must not be more than 100')
        return upper_bound

    @model_validator(mode='after')
    def lower_bound_must_not_be_greater_than_upper_bound(self) -> 'FizzBuzzInput':
        if self.lower_bound > self.upper_bound:
            raise ValueError('The lower bound must not be greater than the upper bound')
        return self
