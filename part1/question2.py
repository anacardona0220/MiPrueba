################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`

swapper = None 
def swapper(tupla):
    """
    Swap the elements of a tuple.

    Args:
        tupla (tuple): A tuple with two elements.

    Returns:
        tuple: A new tuple with the elements swapped.

    Example:
        >>> swapper((3, 5))
        (5, 3)
    """
    x, y = tupla
    return (y, x)

def run_swapper(list_of_tuples):
    """
    Apply the swapper function to each tuple in the list.

    Args:
        list_of_tuples (list of tuples): A list of tuples, where each tuple contains two elements.

    Returns:
        list of tuples: A new list of tuples with elements swapped.

    Example:
        >>> run_swapper([(1, 2), (3, 4), (5, 6)])
        [(2, 1), (4, 3), (6, 5)]
    """
    return list(map(swapper, list_of_tuples))
