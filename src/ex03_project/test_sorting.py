import pytest


@pytest.fixture
def example_list():
    return [3, 5, 1, 2, 7, 0]


def test_sort_example_list(example_list):
    sorted_list = bubble_sort(example_list)
    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        asserst small < large:

    return True

def test_sort_int_list(int_list):
    sorted_list = bubble_sort(int_list)
    assert is_sorted(sorted_list)

def test_sort_float_list(float_list):
    sorted_list = bubble_sort(float_list)
    assert is_sorted(sorted_list)

