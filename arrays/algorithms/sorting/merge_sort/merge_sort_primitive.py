def merge_sort(arr):
    """
    Sort array using merge sort (returns new array).
    
    Args:
        arr: Input array to be sorted (not modified)
    
    Returns:
        New sorted array
    
    Complexity:
        Time: O(n log n)
        Space: O(n log n) - Creates new arrays at each recursive level
    """
    # Base case: array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Divide: split array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conquer: recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine: merge the two sorted halves
    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(a, b):
    """
    Merge two sorted arrays into one sorted array.
    
    This is the core operation of merge sort. It combines two already-sorted
    arrays by comparing elements and taking the smaller one at each step.
    
    Args:
        a: First sorted array
        b: Second sorted array
    
    Returns:
        Merged sorted array containing all elements from a and b
    
    Complexity:
        Time: O(n + m)  - Where n = len(a), m = len(b)
        Space: O(n + m) - Creates new array to store merged result
    """
    sorted_list = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    # Compare elements from both arrays and add smaller one
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    # Add remaining elements from array a (if any)
    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    # Add remaining elements from array b (if any)
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == '__main__':
    print("\n📌 Example: Merge Sort (Primitive Implementation)")
    print("=" * 60)
    
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    print(f"Original array: {arr}")
    
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}")
    print(f"Original array (unchanged): {arr}")
    
    # Test with different cases
    print("\n" + "=" * 60)
    print("Testing with various inputs:")
    
    test_cases = [
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [64, 34, 25, 12, 22, 11, 90]
    ]
    
    for test_arr in test_cases:
        original = test_arr.copy()
        sorted_result = merge_sort(test_arr)
        print(f"Input: {original} -> Output: {sorted_result}")
