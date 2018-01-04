"""Tests for Trie Module."""
import pytest
from trie import Trie


@pytest.fixture
def empty_trie():
    """Create a blank trie."""
    return Trie()


@pytest.fixture
def words():
    """Trie with words."""
    a = Trie()
    a.insert('popcorn')
    a.insert('chicken')
    a.insert('potato')
    a.insert('dragon')
    a.insert('flamingo')
    return a


def test_insert_into_empty_trie(empty_trie):
    """Test the insert function."""
    empty_trie.insert('popcorn')
    empty_trie.size == 1


def test_insert_multiple_words(empty_trie):
    """Test ability to enter multiple words."""
    empty_trie.insert('popcorn')
    empty_trie.insert('chicken')
    empty_trie.insert('potato')
    empty_trie.size == 3


def test_invalid_input_raises_error(empty_trie):
    """Test that a error is raised with invalid input."""
    with pytest.raises(ValueError):
        empty_trie.insert(5)


def test_contains_works(empty_trie):
    """Test that contains returns true when true."""
    empty_trie.insert('popcorn')
    assert empty_trie.contains('popcorn') is True


def test_contains_returns_false_when_word_not_there(empty_trie):
    """Test for a false response when the word does not exist."""
    empty_trie.insert('popcorn')
    assert empty_trie.contains('mushroom') is False


def test_size_works_on_empty(empty_trie):
    """Test that size works on empty trie."""
    assert empty_trie.size == 0


def test_size_works_after_insert_of_single_word(empty_trie):
    """Test that size still works after inserting a word."""
    empty_trie.insert('word')
    assert empty_trie.size == 1


def test_size_works_after_insert_of_multiple_words(empty_trie):
    """Test that size still works after inserting a word."""
    empty_trie.insert('word')
    empty_trie.insert('words')
    empty_trie.insert('worded')
    empty_trie.insert('wordy')
    assert empty_trie.size == 4


def test_remove_method(empty_trie):
    """Test that remove works."""
    empty_trie.insert('popcorn')
    empty_trie.insert('chicken')
    empty_trie.insert('potato')
    empty_trie.remove('popcorn')
    assert empty_trie.size == 2


def test_invalid_remove(words):
    """Test that error is raised when word doens't exist."""
    with pytest.raises(ValueError):
        words.remove('unicorn')


def test_traversal_letter_method(words):
    """Test traversal method works properly."""
    result = words.traversal_letter('pot')
    assert 'a' in next(result)


def test_traversal_method_raise_error(words):
    """Test traversal method raises error with invalid input."""
    with pytest.raises(ValueError):
        words.traversal_letter(100)


def test_traverse_method_letter(words):
    """Test traversal word method finds proper words."""
    result = words.traversal_word('po')
    assert 'potato' or 'popcorn' in next(result)


def test_traverse_method_non_existing_prefix(words):
    """Test traversal word method with non existent prefix."""
    assert words.traversal_word('stre') == []


def test_traverse_method_raise_error(words):
    """Test traversal word method raises error with invalid input."""
    with pytest.raises(ValueError):
        words.traversal_word(100)
