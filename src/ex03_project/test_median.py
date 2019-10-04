import pytest
from .median import median


def test_median_of_singleton():
    assert median([4]) == 4


def test_odd_numbers_of_elements_list():
    assert median([3, 5, 1, 7, 9]) == 5


def test_even_numbers_of_elements_list():
    assert median([1, 2, 2, 1]) == 1.5


def test_median_ordered_list():
    assert median([1, 2, 3, 4, 5]) == 3


def test_median_reversed_ordered_list():
    assert median([5, 4, 3, 2, 1]) == 3


def test_median_unordered_elements_list():
    assert median([3, 5, 1, 7, 9]) == 5


def test_median_rasis_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])


def test_func_leaves_orginal_data_unchanged():
    data = [1, 3, 5]
    assert median(data) == 3 and data == [1, 3, 5]



