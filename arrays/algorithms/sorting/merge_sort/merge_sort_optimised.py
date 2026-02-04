def merge_sort(arr):
    """
    Sort array in-place using merge sort.
    
    Args:
        arr: Input array to be sorted (modified in-place)
    
    Returns:
        None (array is sorted in-place)
    
    Complexity:
        Time: O(n log n)
        Space: O(n) - Uses temporary arrays only during merge
    """
    # Base case: array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return

    # Divide: split array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conquer: recursively sort both halves
    merge_sort(left)
    merge_sort(right)

    # Combine: merge the two sorted halves back into original array
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    """
    Merge two sorted arrays into the original array (in-place).
    
    Args:
        a: First sorted array
        b: Second sorted array
        arr: Target array where merged result will be stored
    
    Returns:
        None (modifies arr in-place)
    
    Complexity:
        Time: O(n + m) where n = len(a), m = len(b)
        Space: O(1) - Only uses variables, modifies arr in-place
    """
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    # Compare elements from both arrays and place smaller one in arr
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    # Copy remaining elements from array a (if any)
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    # Copy remaining elements from array b (if any)
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == '__main__':
    print("\n📌 Example: Merge Sort (Optimized Implementation)")
    print("=" * 60)
    
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        original = arr.copy() if arr else []
        merge_sort(arr)
        print(f"Input: {original} -> Output: {arr}")
    
    # Detailed example
    print("\n" + "=" * 60)
    print("Detailed Example:")
    print("=" * 60)
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before sorting: {arr}")
    merge_sort(arr)
    print(f"After sorting:  {arr}")
    
    # Test with already sorted array
    print("\n" + "=" * 60)
    sorted_arr = [1, 2, 3, 4, 5, 6, 7]
    print(f"Already sorted: {sorted_arr}")
    merge_sort(sorted_arr)
    print(f"After merge sort: {sorted_arr}")
    
    # Test with reverse sorted array
    print("\n" + "=" * 60)
    reverse_arr = [7, 6, 5, 4, 3, 2, 1]
    print(f"Reverse sorted: {reverse_arr}")
    merge_sort(reverse_arr)
    print(f"After merge sort: {reverse_arr}")
