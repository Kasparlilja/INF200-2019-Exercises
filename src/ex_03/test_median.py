import pytest

def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    return (sorted_data[num_elements//2] if num_elements % 2 == 1
        else 0.5 * (sorted_data[num_elements//2 - 1] + sorted_data[num_elements//2]))

    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    else:
        return (sorted_data[num_elements // 2 - 1] + sorted_data[num_elements // 2]) / 2

def test_median_of_singleton():
    assert median([4]) == 4


def tes_median_rasis_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])

