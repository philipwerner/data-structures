"""Test file for Linked List implementation"""
from linked_list import Node
from linked_list import LinkedList
import pytest

def test_node_has_attributes():
    """Test that the node contains proper attributes."""
    n = Node(1, None)
    assert hasattr(n, 'data')
    assert hasattr(n, 'next')


def test_linked_list_has_head():
    """Test that there is a head node in the LL."""
    l = LinkedList()
    assert l.head is None


def test_linked_list_insert_adds_new_item():
    """Test that when a new node is added, it is assigned as the head as well."""
    l = LinkedList()
    l.insert('val')
    assert l.head.data == 'val'


def test_linked_list_insert_two_last_value_is_head():
    """Test that the head is reassigned when adding another node to the LL."""
    l = LinkedList()
    l.insert('val')
    l.insert('val2')
    assert l.head.data == 'val2'


def test_linked_list_insert_two_last_value_is_next_head():
    """Test that the head next value is correctly assigned."""
    l = LinkedList()
    l.insert('val')
    l.insert('val2')
    assert l.head.next.data == 'val'


def test_linked_list_removes_and_returns_head():
    """Test that removing only node makes the head none."""
    l = LinkedList()
    l.insert('potato')
    l.pop()
    assert l.head is None


def test_linked_list_removes_and_returns_head_value():
    """Test that the value of removed node is returned."""
    l = LinkedList()
    l.insert('potato')
    output = l.pop()
    assert output == 'potato'


def test_linked_list_pop_shifts_head_properly():
    """Test that when node removed the head properly assigned."""
    l = LinkedList()
    l.insert('potato')
    l.insert('cabbage')
    l.pop()
    assert l.head.data == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """Test that an error is raised when popping an empty LL."""
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_returns_size_returns_list_length():
    """Test length works on empty LL."""
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(10))
def test_linked_list_returns_size_returns_list_length_one(n):
    """Test multiple lengths are returned properly."""
    l = LinkedList()
    for i in range(n):
        l.insert(i)
    assert l.size() == n


@pytest.mark.parametrize('n', range(10))
def test_linked_list_returns_size_returns_list_len_function(n):
    """Test that len method finds the right length."""
    l = LinkedList()
    for i in range(n):
        l.insert(i)
    assert len(l) == n


def test_linked_list_search_empty_returns_none():
    """Test that nothing is found when LL is empty"""
    l = LinkedList()
    assert l.search(0) is None


def test_linked_list_search_with_one_node_returns_node():
    """Test that search finds proper node."""
    l = LinkedList()
    l.insert(1)
    assert l.search(1) == l.head


def test_linked_list_search_one_returns_none():
    """Test for proper response when search value does not exist."""
    l = LinkedList()
    l.insert(1)
    assert l.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_in_many_returns_proper_node(n):
    """Test search method works."""
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.insert(i)
    search_me = randint(1, n)
    assert l.search(search_me).data == search_me


def test_linked_list_can_take_iterable():
    """Test that a LL object can be instantiated with iterable arg."""
    a_list = [5, 2, 9, 0, 1]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item


def test_display_with_one_node():
    """Test that display works with one node in LL."""
    l = LinkedList()
    l.insert(8)
    assert l.display() == '(8)'


def test_display_with_mult_nodes():
    """Test displaying LL with more than one node."""
    l = LinkedList()
    l.insert(8)
    l.insert(9)
    l.insert(55)
    assert l.display() == '(55, 9, 8)'


def test_remove_linked_list_single():
    """Test that you can remove the only node in a LL."""
    l = LinkedList()
    l.insert(8)
    l.remove(8)
    assert l.display() == '()'


def test_remove_linked_list():
    """Test that you can remove nodes from the LL with multiple nodes."""
    l = LinkedList()
    l.insert(8)
    l.insert(9)
    l.insert(10)
    l.remove(9)
    assert l.display() == '(10, 8)'


def test_remove_linked_list_empty():
    """Test that an error is thrown when removing from empty LL."""
    l = LinkedList()
    with pytest.raises(IndexError):
        assert l.remove(8)


def test_print():
    """Test the print method prints properly."""
    l = LinkedList()
    l.insert(8)
    l.insert(9)
    l.insert(10)
    l.remove(9)
    assert l.__str__() == '(10, 8)'


def test_len():
    """Test that the len method works."""
    l = LinkedList()
    l.insert(8)
    l.insert(9)
    l.insert(10)
    assert l.__len__() == 3