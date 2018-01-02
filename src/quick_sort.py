"""Quick Sort module."""


def qs(ilist):
    """Quick sort an inputed list."""
    if len(ilist) == 1 or len(ilist) == 0:
        return ilist
    elif len(ilist) == 2:
        if ilist[0] > ilist[1]:
            ilist[0], ilist[1] = ilist[1], ilist[0]
        return ilist
    else:
        pivot = ilist[0]
        i = 0
        for j in range(len(ilist) - 1):
            if ilist[j + 1] < pivot:
                ilist[j + 1], ilist[i + 1] = ilist[i + 1], ilist[j + 1]
                i += 1
        ilist[0], ilist[i] = ilist[i], ilist[0]
        l_list = qs(ilist[:i])
        r_list = qs(ilist[i + 1:])
        l_list.append(ilist[i])
        return l_list + r_list


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 7, 8, 9, 10]
    sort_2 = [15, 10, 6, 3, 2, 0]
    sort_3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    time_1 = ti.timeit("qs(sort_1[:])",
                       setup="from __main__ import sort_1, qs")
    time_2 = ti.timeit("qs(sort_2[:])",
                       setup="from __main__ import sort_2, qs")
    time_3 = ti.timeit("qs(sort_3[:])",
                       setup="from __main__ import sort_3, qs")
    print("""
        Input: [1, 2, 7, 8, 9, 10]
        Good case: {}
        Input: [15, 10, 6, 2, 3, 0]
        Bad case: {}
        Input: [54, 26, 93, 17, 77, 31, 44, 55, 20]
        Average case: {}""".format(time_1, time_2, time_3))
