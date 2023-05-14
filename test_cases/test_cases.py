from main import sum_of_two_numbers


def test_sum_function_01():
    assert sum_of_two_numbers(15, 2) == 17
    
def test_sum_function_02():
    assert sum_of_two_numbers(0, 1) == 1
    
def test_sum_function_03():
    assert sum_of_two_numbers(4, 4) == 5