"""
Functions module.
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

def append_create(num):
    """
    Function to calculate square root of a number.
    """
    lst = []
    for item in range(0,10):
        lst = lst.append(item)
    return lst
