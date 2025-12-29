"""
Frequency Maps Using Hash Tables

Count frequency of elements in arrays, strings, etc. using hash tables.

Problem Statement:
-------------------
Count how many times each element appears in a collection.

Example:
    Input: [1, 2, 2, 3, 3, 3]
    Output: {1: 1, 2: 2, 3: 3}

Why Hash Tables?
----------------
- O(1) average time for insert/update
- O(n) time to count all frequencies
- Simple and efficient

Useful in:
- Counting elements
- Finding duplicates
- Common interview problems
"""

from typing import List, Dict, Any
from collections import Counter, defaultdict


# ----------------------------------------------------------------------
# Count Frequency (Language-agnostic)
# ----------------------------------------------------------------------
def count_frequency(arr: List[Any]) -> Dict[Any, int]:
    """
    Count frequency of each element in array.

    Args:
        arr (List[Any]): Input array

    Returns:
        Dict[Any, int]: Frequency map

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores frequency map.
    """
    freq_map: Dict[Any, int] = {}
    
    for element in arr:
        freq_map[element] = freq_map.get(element, 0) + 1
    
    return freq_map


# ----------------------------------------------------------------------
# Count Frequency (Using defaultdict)
# ----------------------------------------------------------------------
def count_frequency_defaultdict(arr: List[Any]) -> Dict[Any, int]:
    """
    Count frequency using defaultdict.

    Args:
        arr (List[Any]): Input array

    Returns:
        Dict[Any, int]: Frequency map

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(n)   - Stores frequency map.
    """
    freq_map = defaultdict(int)
    
    for element in arr:
        freq_map[element] += 1
    
    return dict(freq_map)


# ----------------------------------------------------------------------
# Count Frequency (Using Counter)
# ----------------------------------------------------------------------
def count_frequency_counter(arr: List[Any]) -> Dict[Any, int]:
    """
    Count frequency using Python's Counter.

    Args:
        arr (List[Any]): Input array

    Returns:
        Dict[Any, int]: Frequency map

    Complexity:
        Time: O(n)     - Counter processes array.
        Space: O(n)   - Stores frequency map.
    """
    return dict(Counter(arr))


# ----------------------------------------------------------------------
# Count Character Frequency in String
# ----------------------------------------------------------------------
def count_char_frequency(s: str) -> Dict[str, int]:
    """
    Count frequency of each character in string.

    Args:
        s (str): Input string

    Returns:
        Dict[str, int]: Character frequency map

    Complexity:
        Time: O(n)     - Single pass through string.
        Space: O(k)   - k is number of unique characters.
    """
    freq_map: Dict[str, int] = {}
    
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1
    
    return freq_map


# ----------------------------------------------------------------------
# Find Most Frequent Element
# ----------------------------------------------------------------------
def most_frequent(arr: List[Any]) -> Any:
    """
    Find most frequent element in array.

    Args:
        arr (List[Any]): Input array

    Returns:
        Any: Most frequent element

    Complexity:
        Time: O(n)     - Count frequencies + find max.
        Space: O(n)   - Stores frequency map.
    """
    freq_map = count_frequency(arr)
    return max(freq_map, key=freq_map.get)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Frequency Maps Demonstration")
    
    # Count frequency in array
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(f"Array: {arr}")
    
    freq1 = count_frequency(arr)
    print(f"Frequency map: {freq1}")
    
    freq2 = count_frequency_defaultdict(arr)
    print(f"Using defaultdict: {freq2}")
    
    freq3 = count_frequency_counter(arr)
    print(f"Using Counter: {freq3}")
    
    # Count character frequency
    print("\n" + "="*50)
    s = "hello world"
    print(f"String: '{s}'")
    char_freq = count_char_frequency(s)
    print(f"Character frequency: {char_freq}")
    
    # Most frequent element
    print("\n" + "="*50)
    arr2 = [1, 2, 2, 3, 3, 3, 2, 2]
    print(f"Array: {arr2}")
    most_freq = most_frequent(arr2)
    print(f"Most frequent element: {most_freq}")

