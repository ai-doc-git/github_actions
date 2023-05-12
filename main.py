"""
Main module.
"""

import numpy as np

def sum_of_two_numbers(first_num, second_num):
    """
    Function to add two numbers.
    """
    return first_num + second_num

def numpy_sqrt_op(num):
    """
    Function to calculate square root of a number.
    """
    return int(np.sqrt(num))

if __name__ == "__main__":
    print(sum_of_two_numbers(1,9))
    print(numpy_sqrt_op(625))
