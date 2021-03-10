import pytest
from counter import Counter


@pytest.fixture(scope="function")
def counter():
    return Counter()


def test_new_counter(counter):
    """Tests state of a new counter."""
    assert counter.get_count() == 0


def tests_inctrement(counter):
    """Tests state after counter is incremented."""
    counter.increment()
    assert counter.get_count() == 1
