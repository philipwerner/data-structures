"""Bubble sort module."""


def b_sort(ilist):
    """Bubble sorting function."""
    if isinstance(ilist, list):
        for numbers in range(len(ilist) -1, 0, -1):
            for i in range(numbers):
                if ilist[i] > ilist[i + 1]:
                    num_holder = ilist[i]
                    ilist[i] = ilist[i + 1]
                    ilist[i + 1] = num_holder
        return ilist
    else:
        raise TypeError('Bubble sort is for lists only')

if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = b_sort([17, 9, 7, 4, 1, 0])

    time_1 = ti.timeit("b_sort(sort_1)",
                       setup="from __main__ import sort_1, b_sort")
    time_2 = ti.timeit("b_sort(sort_2)",
                       setup="from __main__ import sort_2, b_sort")
    print("""
        Input: [1, 2, 4, 9, 10, 11]
        Good case: {}
        Input: [17, 9, 7, 4, 1, 0]
        Bad case: {}""".format(time_1, time_2))
