
import pytest

from counter import Counter

@pytest.fixture(scope="function")
def counter():
    return Counter()

def test_new_counter(counter):
    """Tests state of a new lock."""
    assert counter.get_count() == 0

def tests_inctrement(counter):
    """Tests state after lock is locked."""
    counter.increment()
    assert counter.get_count() == 1
