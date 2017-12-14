"""Module for merge sort method."""


def merge_sort(ilist):
    """Merge sort function."""
    if isinstance(ilist, list):
        if len(ilist) <= 1:
            return ilist
        elif len(ilist) == 2:
            if ilist[0] > ilist[1]:
                ilist[0], ilist[1] = ilist[1], ilist[0]
            else:
                return ilist
        split_list = len(ilist) // 2
        left_list = merge_sort(ilist[:split_list])
        right_list = merge_sort(ilist[split_list:])
        ilist = _join_list(left_list, right_list)
        return ilist
    else:
        raise TypeError('Merge Sort requires a list')


def _join_list(left_list, right_list):
    """Create and join sorted left and right lists."""
    l_index = 0
    r_index = 0
    result = []
    while l_index < len(left_list) and r_index < len(right_list):
        if left_list[l_index] < right_list[r_index]:
            result.append(left_list[l_index])
            l_index += 1
        else:
            result.append(right_list[r_index])
            r_index += 1
    result += left_list[l_index:]
    result += right_list[r_index:]
    return result

if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 7, 8, 9, 10]
    sort_2 = [15, 10, 6, 2, 3, 0]

    time_1 = ti.timeit("merge_sort(sort_1[:])",
                       setup="from __main__ import sort_1, merge_sort")
    time_2 = ti.timeit("merge_sort(sort_2[:])",
                       setup="from __main__ import sort_2, merge_sort")
    print("""
        Input: [1, 2, 7, 8, 9, 10]
        Good case: {}
        Input: [15, 10, 6, 2, 3, 0]
        Bad case: {}""".format(time_1, time_2))
