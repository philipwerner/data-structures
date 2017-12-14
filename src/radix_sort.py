"""Radix sort module."""


def radix_sort(ilist):
    """Radix sorting method."""
    if isinstance(ilist, list):
        x = 10
        temp = -1
        place = 1
        max_length = False
        while not max_length:
            max_length = True
            buckets = [list() for i in range(x)]
            for j in ilist:
                temp = j / place
                buckets[temp % x].append(j)
                if max_length > 0 and temp > 0:
                    max_length = False
            y = 0
            for i in range(x):
                dump_bucket = buckets[i]
                for j in dump_bucket:
                    ilist[y] = j
                    y += 1
            place *= x
        return ilist
    else:
        raise TypeError('Radix sort is for lists only')


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = [17, 9, 7, 4, 1, 0]

    time_1 = ti.timeit("radix_sort(sort_1)",
                       setup="from __main__ import sort_1, radix_sort")
    time_2 = ti.timeit("radix_sort(sort_2)",
                       setup="from __main__ import sort_2, radix_sort")
    print("""
        Input: [1, 2, 4, 9, 10, 11]
        Good case: {}
        Input: [17, 9, 7, 4, 1, 0]
        Bad case: {}""".format(time_1, time_2))
