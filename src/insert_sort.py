"""Insert sort sorting method."""


def insert_sort(ilist):
    """Insert sort function."""
    if isinstance(ilist, list):
        for numbers in range(len(ilist) - 1):
            for i in range(numbers + 1, 0, -1):
                if ilist[i] < ilist[i - 1]:
                    num_holder = ilist[i]
                    ilist[i] = ilist[i - 1]
                    ilist[i - 1] = num_holder
        return ilist
    else:
        raise TypeError('Function only accepts lists')


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = [17, 9, 7, 4, 1, 0]

    time_1 = ti.timeit("insert_sort(sort_1[:])",
                       setup="from __main__ import sort_1, insert_sort")
    time_2 = ti.timeit("insert_sort(sort_2[:])",
                       setup="from __main__ import sort_2, insert_sort")
    print("""
        Input: [1, 2, 4, 9, 10, 11]
        Good case: {}
        Input: [17, 9, 7, 4, 1, 0]
        Bad case: {}""".format(time_1, time_2))
