"""Tests for DLL."""
import pytest
from dll import DoubleLinkedList
from dll import Node


@pytest.fixture
def double(scope="function"):
    """Return dbly linked list for testing."""
    dll = DoubleLinkedList()
    return dll


def test_node_has_attributes():
    """Test node."""
    n = Node(1, None, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'next')
    assert hasattr(n, 'prev')


def test_doubly_linked_list_has_head(double):
    """Test head."""
    assert double.list.head is None


def test_doubly_linked_list_push_adds_new_item(double):
    """Test push."""
    double.push('val')
    assert double.head.data == 'val'


def test_doubly_linked_list_counter(double):
    """Test counter."""
    double.push(1)
    double.push(2)
    assert len(double) == 2


def test_doubly_linked_list_push(double):
    """Test push."""
    double.push(1)
    assert len(double) == 1


def test_doubly_linked_list_append(double):
    """Test append."""
    double.append(1)
    assert len(double) == 1


def test_doubly_linked_shift(double):
    """Test pop."""
    double.push(77)
    assert double.pop() == 77


def test_doubly_pop_and_append(double):
    """Test popping an append."""
    double.append(77)
    assert double.pop() == 77


def test_pop_when_empty_list_exception(double):
    """Test error for pop of empty list."""
    with pytest.raises(IndexError):
        double.pop()


def test_shift_returns_correct_val(double):
    """Test shift."""
    double.push(77)
    double.push(66)
    double.push(55)
    assert double.shift() == 77


def test_shift_when_empty_list_exception(double):
    """Test error for pop of empty list."""
    with pytest.raises(IndexError):
        double.shift()


def test_doubly_next_val_assign_when(double):
    """Test popping an append."""
    double.append(77)
    double.append(66)
    double.append(55)
    assert double.pop() == 77
    assert double.pop() == 66
    assert double.pop() == 55


def test_init_iterable():
    """Test for handling interable on init."""
    dll = DoubleLinkedList((77, 66, 55))
    assert dll.pop() == 77
    assert dll.pop() == 66
    assert dll.pop() == 55


def test_remove_method(double):
    """Test remove method."""
    double.push(3)
    double.push(2)
    double.push(1)
    double.remove(2)
    assert double.pop() == 1
    assert double.pop() == 3


def test_remove_when_val_not_in_list(double):
    """Test error for pop of empty list."""
    with pytest.raises(ValueError):
        double.push(1)
        double.push(1)
        double.remove(2)


def test_pop(double):
    """Test error for pop of empty list."""
    double.push(1)
    assert double.pop() == 1
