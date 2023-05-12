import numpy as np

def sum_of_two_numbers(a, b):
    return a + b

def numpy_sqrt_op(a):
    return int(np.sqrt(a))

if __name__ == "__main__":
    print(sum_of_two_numbers(1,9))
    print(numpy_sqrt_op(625))