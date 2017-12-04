"""Test the hash table."""
import pytest
from hash import HT


@pytest.fixture
def empty_table():
    """Make a empty additive hash table."""
    return HT()


@pytest.fixture
def b_table():
    """Make an empty bernstein table."""
    return HT(1024, 'bernstein')


@pytest.fixture
def sax_table():
    """Make an empty sax table."""
    return HT(1024, 'sax')


@pytest.fixture
def fnv_table():
    """Make an empty fnv table."""
    return HT(1024, 'fnv')


@pytest.fixture
def full_table():
    """Create a full hash table."""
    ht = HT()
    with open('/user/share/dict/words', 'r') as words:
        the_list = words.readLines()
    for word in the_list:
        ht.set(word.strip(), word.strip())
    return ht


def test_set_key_and_value(empty_table):
    """Test setting new key and val."""
    empty_table.set('lions', 9)
    assert [['lions', 9]] in empty_table.h_table


def test_get_method_when_key_exist(empty_table):
    """Test that the get method returns proper data."""
    empty_table.set('lions', 9)
    assert empty_table.get('lions') == 9


def test_set_with_invalid_key(empty_table):
    """Test set raises error when key is not a string."""
    with pytest.raises(TypeError):
        empty_table.set(99, 'rabbits')


def test_set_in_bernstein(b_table):
    """Test setting to a bernstein hash table."""
    b_table.set('lions', 99)
    assert [['lions', 99]] in b_table.h_table


def test_bernstein_hash(b_table):
    """Test hash for bernstein."""
    assert b_table._hash('lion') == 794


def test_additive_hash(empty_table):
    """Test hash for additive."""
    assert empty_table._hash('lion') == 434


def test_sax_hash(sax_table):
    """Test hash for sax."""
    assert sax_table._hash('lion') == 4045575


def test_fnv_hash(fnv_table):
    """Test hash for additive."""
    assert fnv_table._hash('lion') == 1684239992712