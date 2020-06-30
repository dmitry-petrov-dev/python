# Main program - task6.py
# Generator of int numbers in sequence
from itertools import count


def my_generator(start=0, finish=0):
    """ Sequence generation of integer
    start - first number
    finish - length
    Returns List
    """
    i = 1
    my_list = []
    for el in count(start):
        if i > finish:
            break
        my_list.append(el)
        i += 1
    return my_list
