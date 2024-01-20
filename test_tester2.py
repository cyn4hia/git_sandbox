def test_binary_search():
    # Test case 1: Target element is present in the array
    arr1 = [1, 2, 3, 4, 5]
    target1 = 3
    assert binary_search(arr1, target1) == 2

    # Test case 2: Target element is not present in the array
    arr2 = [10, 20, 30, 40, 50]
    target2 = 35
    assert binary_search(arr2, target2) == -1

    # Test case 3: Target element is the first element in the array
    arr3 = [5, 10, 15, 20, 25]
    target3 = 5
    assert binary_search(arr3, target3) == 0

    # Test case 4: Target element is the last element in the array
    arr4 = [5, 10, 15, 20, 25]
    target4 = 25
    assert binary_search(arr4, target4) == 4

    # Test case 5: Empty array
    arr5 = []
    target5 = 10
    assert binary_search(arr5, target5) == -1

    print("All test cases passed!")

test_binary_search()