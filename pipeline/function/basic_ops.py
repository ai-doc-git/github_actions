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

# def append_list(num):
#     """
#     Function to append items to list in a specific range using for loop.
#     """
#     lst = []
#     for item in range(0,num):
#         lst.append(item)
#     return lst

def append_list(num):
    """
    Function to append items to list in a specific range using list comprehension.
    """
    return [item for item in range(1,num)]
