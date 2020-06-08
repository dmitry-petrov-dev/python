# Main program - task6.py
# Cycle of elements
from itertools import cycle


def my_cycle(var=[], stop=0):
    """Generate list with cycle of elements
        var - List
        stop - number of iteration
    """
    i = 1
    my_list = []
    for el in cycle(var):
        if i > stop:
            break
        my_list.append(el)
        i += 1
    return my_list
