import pytest
from radix_sort import radix_sort as rs

sb_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bs_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
uo_list = [56, 3, 78, 79, 34, 22, 87, 1, 23]
big_list = [945, 1023, 43, 198, 2, 743, 3219, 219, 574, 206, 919, 342]
dupe_list = [76, 44, 923, 123, 44, 56, 923, 76, 3, 2]
three = [78, 34, 57]
two = [99, 1]
one = [999]


def test_radix_on_list_of_3():
    """Test that radix sort works on list of 3."""
    assert rs(three) == [34, 57, 78]


def test_radix_on_list_of_2():
    """Test that radix sort works on list of 2."""
    assert rs(two) == [1, 99]


def test_radix_on_list_of_1():
    """Test that radix sort works on list of 1."""
    assert rs(one) == [999]


def test_radix_on_sorted_list():
    """Test that radix returns same list as inputed."""
    assert rs(sb_list) == sb_list


def test_radix_on_reverse_numerical_list():
    """Test that radix returns list properly ordered."""
    assert rs(bs_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_radix_on_unordered_list():
    """Test that radix properly orders a unordered list."""
    assert rs(uo_list) == [1, 3, 22, 23, 34, 56, 78, 79, 87]


def test_radix_works_on_large_numbers():
    """Test that radix properly sorts larger numbers."""
    rs(big_list)
    assert big_list == [2, 43, 198, 206, 219, 342, 574, 743, 919, 945, 1023, 3219]


def test_radix_raises_type_error_when_input_is_not_list():
    """Test that a type error is raised with invalid input."""
    not_a_list = 999
    with pytest.raises(TypeError):
        rs(not_a_list)


def test_radix_works_with_duplicate_values_in_list():
    """Test that duplicate values are properly sorted."""
    rs(dupe_list)
    assert dupe_list == [2, 3, 44, 44, 56, 76, 76, 123, 923, 923]
