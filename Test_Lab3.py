import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_sort_n_more_10():
    result = []
    input_arr = [64, 34, 2,235,6,3,5,23,23,4,5,3,2]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)


def test_bubble_sort_n_equal_0():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)


def test_bubble_sort_not_a_int():
    result = []
    input_arr = [1, 2, "je;;p"]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)
    assert (Lab3.bubble_sort([1, 2, 3.4], Lab3.SORT_DESCENDING) == 2)
    assert (Lab3.bubble_sort(["b", "a", "c"], Lab3.SORT_DESCENDING) == 2)