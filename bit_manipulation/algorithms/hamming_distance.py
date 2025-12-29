"""
Hamming Distance and Similarity

Hamming distance is the number of positions at which corresponding bits differ.
Used to measure similarity between binary representations.

Problem Statement:
------------------
Calculate Hamming distance between two integers (number of differing bits).

Example:
    Input: x = 1 (binary: 0001), y = 4 (binary: 0100)
    Output: 2
    Explanation: Bits differ at positions 0 and 2

Useful in:
- Error detection and correction
- Measuring similarity
- Common interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Hamming Distance (Language-agnostic)
# ----------------------------------------------------------------------
def hamming_distance(x: int, y: int) -> int:
    """
    Calculate Hamming distance between two integers.

    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Hamming distance (number of differing bits)

    Complexity:
        Time: O(log n)  - Processes each bit, n is max(x, y).
        Space: O(1)   - Only uses counter variable.
    """
    xor_result = x ^ y
    distance = 0
    
    while xor_result:
        distance += xor_result & 1
        xor_result >>= 1
    
    return distance


def hamming_distance_kernighan(x: int, y: int) -> int:
    """
    Calculate Hamming distance using Brian Kernighan's algorithm.

    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Hamming distance

    Complexity:
        Time: O(k)     - Where k is number of set bits in XOR.
        Space: O(1)   - Only uses counter variable.
    """
    xor_result = x ^ y
    distance = 0
    
    while xor_result:
        xor_result &= xor_result - 1  # Clear rightmost set bit
        distance += 1
    
    return distance


# ----------------------------------------------------------------------
# Total Hamming Distance
# ----------------------------------------------------------------------
def total_hamming_distance(nums: List[int]) -> int:
    """
    Calculate total Hamming distance for all pairs in array.

    Args:
        nums (List[int]): Array of numbers

    Returns:
        int: Sum of Hamming distances for all pairs

    Complexity:
        Time: O(n * log m)  - n numbers, m is max value, processes each bit.
        Space: O(1)       - Only uses variables.
    """
    total = 0
    n = len(nums)
    
    # For each bit position
    for i in range(32):
        count_ones = 0
        for num in nums:
            if (num >> i) & 1:
                count_ones += 1
        # Pairs with different bits: count_ones * (n - count_ones)
        total += count_ones * (n - count_ones)
    
    return total


# ----------------------------------------------------------------------
# Hamming Weight (Number of Set Bits)
# ----------------------------------------------------------------------
def hamming_weight(n: int) -> int:
    """
    Calculate Hamming weight (number of set bits).

    Args:
        n (int): Number

    Returns:
        int: Number of set bits

    Complexity:
        Time: O(log n)  - Processes each bit.
        Space: O(1)   - Only uses counter variable.
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Hamming Distance Demonstration")
    
    x, y = 1, 4
    print(f"x = {x} (binary: {bin(x)})")
    print(f"y = {y} (binary: {bin(y)})")
    distance = hamming_distance(x, y)
    print(f"Hamming distance: {distance}")
    print("Expected: 2")
    
    # Total Hamming distance
    nums = [4, 14, 2]
    print(f"\nArray: {nums}")
    total = total_hamming_distance(nums)
    print(f"Total Hamming distance: {total}")
    
    # Hamming weight
    num = 11  # Binary: 1011
    print(f"\nNumber: {num} (binary: {bin(num)})")
    weight = hamming_weight(num)
    print(f"Hamming weight (set bits): {weight}")

