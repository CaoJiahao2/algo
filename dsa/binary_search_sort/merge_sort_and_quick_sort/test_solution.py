from dsa.binary_search_sort.merge_sort_and_quick_sort.solution import merge_sort, quick_sort

def test_merge_sort():
    assert merge_sort([3, 1, 2]) == [1, 2, 3]
    assert merge_sort([]) == []

def test_quick_sort():
    assert quick_sort([5, 2, 3, 1]) == [1, 2, 3, 5]

