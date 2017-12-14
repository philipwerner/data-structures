"""Test module for merge_sort."""
import pytest
from merge_sort import merge_sort

sb_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bs_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
uo_list = [56, 3, 78, 79, 34, 22, 87, 1, 23]
short = [19, 3]
three_list = [19, 56, 5]
one_list = [9345]


def test_merge_sort_with_numerical_ordered_list():
    """Test that a already sorted list returns how it went in."""
    merge_sort(sb_list)
    assert sb_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_merge_sort_a_simple_sort():
    """Test on a reverse numerical list."""
    merge_sort(bs_list)
    assert sb_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_merge_sort_on_out_of_order_list():
    """Test sorting a non numerical list."""
    result = merge_sort(uo_list)
    assert result == [1, 3, 22, 23, 34, 56, 78, 79, 87]


def test_merge_sort_on_list_of_2():
    """Test that merge sort can sort small lists."""
    result = merge_sort(short)
    assert result == [3, 19]


def test_merge_sort_on_list_of_3():
    """Test that merge sort can sort small lists."""
    result = merge_sort(three_list)
    assert result == [5, 19, 56]


def test_merge_sort_with_list_length_of_1():
    """Test that merge sort returns a 1 length list."""
    assert merge_sort(one_list) == [9345]
