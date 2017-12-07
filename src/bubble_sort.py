"""Bubble sort module."""


def b_sort(ilist):
    """Bubble sorting function."""
    for numbers in range(len(ilist) -1, 0, -1):
        for i in range(numbers):
            if ilist[i] > ilist[i + 1]:
                num_holder = ilist[i]
                ilist[i] = ilist[i + 1]
                ilist[i + 1] = num_holder
    return ilist
