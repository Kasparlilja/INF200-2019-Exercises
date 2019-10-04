# -*- coding: utf-8 -*-

__author__ = 'Kaspar Akilles Lilja'
__email__ = 'kalilja@nmbu.no'


def example_list():
    return [3, 5, 1, 9, 2]


def bubble_sort(data):
    datalist = list(data)
    for i in range(0, len(datalist) - 1):
        for j in range(0, len(datalist) - 1 - i):
            if datalist[j] > datalist[j + 1]:
                datalist[j], datalist[j + 1] = datalist[j + 1], datalist[j]
    return datalist


def test_empty():
    """Test that the sorting function works for empty list"""
    empty_list = []
    assert bubble_sort(empty_list) == empty_list


def test_single():
    """Test that the sorting function works for single-element list"""
    single_element_list = [2]
    assert bubble_sort(single_element_list) == single_element_list


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert id(data) != id(sorted_data)


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1] and sorted_data != [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3, 4, 6, 9]
    sorted_data = bubble_sort(data)
    for small, large in zip(sorted_data[:-1], sorted_data[1:]):
        assert small < large


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [9, 6, 4, 3, 2, 1]
    sorted_data = bubble_sort(data)
    for small, large in zip(sorted_data[:-1], sorted_data[1:]):
        assert small < large


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [9, 2, 3, 5, 8, 9]
    sorted_data = bubble_sort(data)
    assert sorted_data == [2, 3, 5, 8, 9, 9]


def test_sort_float_list():
    float_list = [4.33, 3.2, 6.6798]
    sorted_list = bubble_sort(float_list)
    assert sorted_list == [3.2, 4.33, 6.6798]


def test_comparing_two_lists():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    list1 = [3, 2, 1]
    list2 = [4, 5, 2, 7]
    sorted_list1 = bubble_sort(list1)
    sorted_list2 = bubble_sort(list2)
    assert sorted_list1 < sorted_list2



