"""."""
from linked_list import LinkedList


def sort(linked_list, val):
    """."""
    left = []
    right = []
    the_list = linked_list.display()
    for i in the_list:
        if i < val:
            left.append(i)
        else:
            right.append(i)
    final_left = left.reverse()
    final_right = right.reverse()
    result = LinkedList()
    for i in final_right:
        result.insert(i)
    for i in final_left:
        result.insert(i)
    return result
