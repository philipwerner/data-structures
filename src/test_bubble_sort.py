"""Test module for Bubble sort."""
import pytest
from bubble_sort import b_sort

sb_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bs_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
uo_list = [56, 3, 78, 79, 34, 22, 87, 1, 23]


def test_bubble_sort_with_numerical_ordered_list():
    """Test that a already sorted list returns how it went in."""
    b_sort(sb_list)
    assert sb_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bubble_sort_a_simple_sort():
    """Test on a reverse numerical list."""
    b_sort(bs_list)
    assert sb_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bubble_sort_on_out_of_order_list():
    """Test sorting a non numerical list."""
    b_sort(uo_list)
    assert uo_list == [1, 3, 22, 23, 34, 56, 78, 79, 87]
