"""
Array (list) operations in Python.

Covered topics:
- Creation
- Access
- Updating
- Insertion
- Deletion
- Traversal / Iteration
- Searching
- Common array operations (sum, max, min, reverse, slicing)
- Basic time & space complexity notes
"""

if __name__ == "__main__":
    # ----------------------------
    # 1. Creating Arrays / Lists
    # ----------------------------
    print("\n🔹 1. ARRAY CREATION")

    arr1 = []                 # empty list
    arr2 = [1, 2, 3, 4]       # direct initialization
    arr3 = list(range(5))     # [0, 1, 2, 3, 4]

    print("arr1 (empty):", arr1)
    print("arr2:", arr2)
    print("arr3 (from range):", arr3)

    # Time Complexity:
    # - Creating with a literal (like [1, 2, 3, 4]) is O(n) for n elements.
    # - Creating with range + list() is O(n) because it materializes n elements.
    # Space Complexity: O(n) for storing n elements.

    # ----------------------------
    # 2. Accessing & Slicing
    # ----------------------------
    print("\n🔹 2. ACCESSING ELEMENTS & SLICES")

    print("First element of arr2:", arr2[0])
    print("Last element of arr2:", arr2[-1])
    print("Slice arr2[1:3]:", arr2[1:3])

    # Time Complexity:
    # - Accessing arr2[i] is O(1) because the list can compute the address
    #   of the i-th element directly.
    # - Slicing arr2[a:b] is O(k) where k is the number of elements in the slice,
    #   because Python has to copy those k elements into a new list.
    # Space Complexity:
    # - Single element access: O(1) extra space.
    # - Slicing: O(k) extra space for the new list.

    # ----------------------------
    # 3. Updating Elements
    # ----------------------------
    print("\n🔹 3. UPDATING ELEMENTS")

    print("Before update arr2:", arr2)
    arr2[0] = 10    # update the first element
    print("After arr2[0] = 10:", arr2)

    # Time Complexity:
    # - Updating by index is O(1) because it overwrites the value at a known position.
    # Space Complexity: O(1) extra space.

    # ----------------------------
    # 4. Insertion
    # ----------------------------
    print("\n🔹 4. INSERTION")

    arr2.append(5)        # add at end
    arr2.insert(1, 7)     # insert 7 at index 1
    print("After append(5) and insert(1, 7):", arr2)

    # Time Complexity:
    # - append(x) → O(1) amortized:
    #   Most appends just fill the next free slot.
    #   Occasionally, Python resizes the list and copies elements (that step is O(n)),
    #   but this happens rarely enough that the average cost stays O(1).
    # - insert(i, x) → O(n):
    #   Elements from index i onward must be shifted one position to the right,
    #   which may touch up to n elements.
    # Space Complexity: O(1) extra space for both operations (ignoring rare resize).

    # ----------------------------
    # 5. Deletion
    # ----------------------------
    print("\n🔹 5. DELETION")

    arr2.pop()             # remove last element
    arr2.remove(7)         # remove first occurrence of 7
    print("After pop() and remove(7):", arr2)

    # Time Complexity:
    # - pop() at end → O(1):
    #   Just drops the last element without shifting others.
    # - pop(i) or remove(value) → O(n):
    #   May require shifting many elements left to fill the gap.
    # Space Complexity: O(1) extra space.

    # ----------------------------
    # 6. Traversal / Iteration
    # ----------------------------
    print("\n🔹 6. TRAVERSAL / ITERATION")

    print("Traversal using for loop:", end=" ")
    for elem in arr2:
        print(elem, end=" ")
    print()

    print("Traversal using while loop:", end=" ")
    i = 0
    while i < len(arr2):
        print(arr2[i], end=" ")
        i += 1
    print()

    # List comprehension example (transformation)
    squared = [x**2 for x in arr2]
    print("Squared elements using list comprehension:", squared)

    # Time Complexity:
    # - Traversal (for/while) is O(n) because each element is visited once.
    # - List comprehension that processes all elements is also O(n).
    # Space Complexity:
    # - Simple traversal (printing only) uses O(1) extra space.
    # - List comprehension creates a new list of size n → O(n) space.

    # ----------------------------
    # 7. Common Array Operations
    # ----------------------------
    print("\n🔹 7. COMMON ARRAY OPERATIONS")

    arr = [1, 2, 3, 4, 5]

    total = sum(arr)        # O(n)
    max_val = max(arr)      # O(n)
    min_val = min(arr)      # O(n)
    rev_new = arr[::-1]     # O(n), creates new list
    arr.reverse()           # in-place reverse → O(n)

    print("Original [1,2,3,4,5] → arr after reverse():", arr)
    print("Sum:", total, "Max:", max_val, "Min:", min_val)
    print("Reversed copy using slicing arr[::-1]:", rev_new)

    # Time Complexity:
    # - sum, max, min → O(n) because each function must inspect every element.
    # - arr[::-1] → O(n) because a new reversed list of size n is built.
    # - arr.reverse() → O(n) because elements are swapped from ends toward the center.
    # Space Complexity:
    # - sum, max, min, reverse() in-place → O(1) extra space.
    # - slicing to reverse (arr[::-1]) → O(n) space for the new list.

    # ----------------------------
    # 8. Searching & Membership
    # ----------------------------
    print("\n🔹 8. SEARCHING & MEMBERSHIP")

    nums = [10, 20, 30, 40]
    print("nums:", nums)

    target = 30
    if target in nums:                # membership test
        index = nums.index(target)    # find index of first occurrence
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found")

    # Time Complexity:
    # - "x in list" → O(n) in the worst case:
    #   Python may need to scan each element until it finds x or reaches the end.
    # - list.index(x) → O(n) for the same reason.
    # Space Complexity: O(1) extra space.

    # ----------------------------
    # 9. Length, Copy, and Subarrays
    # ----------------------------
    print("\n🔹 9. LENGTH, COPY & SUBARRAYS")

    print("nums:", nums)
    print("Length of nums:", len(nums))

    nums_copy = nums.copy()
    print("Copy of nums:", nums_copy)

    sub = nums[1:3]
    print("Subarray nums[1:3]:", sub)

    # Time Complexity:
    # - len(list) → O(1) because Python stores the length as a field on the list object.
    # - copy() → O(n) because it copies all n references into a new list.
    # - slicing list[a:b] → O(k) where k = b - a (number of elements copied).
    # Space Complexity:
    # - len(list) → O(1) extra.
    # - copy() and slicing → O(k) extra space for the new lists.

# ----------------------------
# 10. Summary of Complexity
# ----------------------------
"""
Summary of Time & Space Complexity (n = number of elements)

1. Access (arr[i])
   - Time: O(1)
     Why: The position of element i can be computed directly using its index.
   - Space: O(1)
     Why: No new data structure is created.

2. Append at end (arr.append(x))
   - Time: O(1) amortized
     Why: Most appends write into existing free space. Only when the list is full
          does Python allocate a bigger block and copy elements (that resize is O(n),
          but happens rarely relative to the number of appends).
   - Space: O(1) extra
     Why: Only one new element reference is added (ignoring occasional resize).

3. Insert/Delete at arbitrary index (arr.insert(i, x), arr.pop(i), arr.remove(x))
   - Time: O(n)
     Why: Elements after index i must be shifted to keep the list contiguous,
          which may involve moving up to n elements.
   - Space: O(1) extra
     Why: The operation reuses the existing list, only changing positions.

4. Traversal / Iteration (for x in arr, while loop)
   - Time: O(n)
     Why: Each element is visited once.
   - Space: O(1) extra
     Why: No additional large data structure is created for simple iteration.

5. Sum / Max / Min (sum(arr), max(arr), min(arr))
   - Time: O(n)
     Why: Every element must be checked to compute the total, maximum, or minimum.
   - Space: O(1) extra
     Why: Only a few variables are used to track running totals or extrema.

6. Reverse in-place (arr.reverse())
   - Time: O(n)
     Why: Elements are swapped from both ends toward the center, touching each element.
   - Space: O(1) extra
     Why: Swapping uses only a few temporary variables.

7. Reverse with slicing (arr[::-1])
   - Time: O(n)
     Why: A new list of size n is built and filled with elements in reverse order.
   - Space: O(n)
     Why: A separate list containing n elements is created.

8. Copy and Slicing (arr.copy(), arr[a:b])
   - Time: O(k) where k is the number of elements copied
     Why: Each of the k elements must be copied into the new list.
   - Space: O(k)
     Why: The new list holds k element references.

9. Length (len(arr))
   - Time: O(1)
     Why: Python stores the length internally, so it can be returned directly.
   - Space: O(1)
     Why: No extra structures are created.
"""
