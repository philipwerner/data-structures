"""Test module for quick sort."""
import pytest
from quick_sort import qs


alist = [1, 2, 3, 4, 5, 6, 7]
blist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
clist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
dlist = [99, 11]


def test_quick_sort_ordered_list():
    """Test that an ordered list is returned the same."""
    assert qs(alist) == [1, 2, 3, 4, 5, 6, 7]


def test_quick_sort_on_reverse_numerical_list():
    """Test that a reversed numerical list is properly returned."""
    assert qs(blist) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_quick_sort_on_unordered_list():
    """Test that a unordered list is properly ordered."""
    assert qs(clist) == [17, 20, 26, 31, 44, 54, 55, 77, 93]


def test_proper_handling_of_a_list_of_2():
    """Test that a list of two is properly returned."""
    assert qs(dlist) == [11, 99]



