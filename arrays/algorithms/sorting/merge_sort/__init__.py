"""
Merge Sort Implementation Module

This module contains two implementations of merge sort:
1. Primitive approach - Returns new sorted array
2. Optimized approach - Sorts in-place

Both implementations demonstrate the divide-and-conquer paradigm.
"""

from .merge_sort_primitive import merge_sort as merge_sort_primitive, merge_two_sorted_lists
from .merge_sort_optimised import merge_sort as merge_sort_optimised

__all__ = [
    'merge_sort_primitive',
    'merge_sort_optimised',
    'merge_two_sorted_lists'
]
