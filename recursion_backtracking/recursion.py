"""
Recursion in Python

Recursion is a programming technique where a function calls itself to solve
a problem by breaking it down into smaller subproblems.

Key Concepts:
1. Base Case: Condition that stops recursion
2. Recursive Case: Function calls itself with smaller input
3. Call Stack: Stack of function calls during execution

Why Recursion?
--------------
- Natural for problems with recursive structure
- Cleaner code for tree/graph traversals
- Divide and conquer algorithms
- Backtracking problems

Useful in:
- Tree/graph traversals
- Divide and conquer
- Dynamic programming
- Backtracking
- Common interview problems
"""

from typing import Any, List


# ----------------------------------------------------------------------
# Factorial (Classic Recursion Example)
# ----------------------------------------------------------------------
def factorial(n: int) -> int:
    """
    Calculate factorial using recursion.

    Base case: n == 0 or n == 1, return 1
    Recursive case: n * factorial(n - 1)

    Args:
        n (int): Non-negative integer

    Returns:
        int: Factorial of n

    Complexity:
        Time: O(n)     - Makes n recursive calls.
        Space: O(n)   - Call stack depth is n.
    """
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)


# ----------------------------------------------------------------------
# Fibonacci (Recursion with Memoization)
# ----------------------------------------------------------------------
def fibonacci(n: int, memo: dict = None) -> int:
    """
    Calculate Fibonacci number using recursion with memoization.

    Args:
        n (int): Position in Fibonacci sequence
        memo (dict): Memoization dictionary

    Returns:
        int: nth Fibonacci number

    Complexity:
        Time: O(n)     - With memoization, each number calculated once.
        Space: O(n)    - Call stack + memo storage.
    """
    if memo is None:
        memo = {}
    
    # Base cases
    if n <= 1:
        return n
    
    # Check memo
    if n in memo:
        return memo[n]
    
    # Recursive case with memoization
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# ----------------------------------------------------------------------
# Sum of Array (Recursion)
# ----------------------------------------------------------------------
def sum_array(arr: List[int]) -> int:
    """
    Calculate sum of array using recursion.

    Args:
        arr (List[int]): Input array

    Returns:
        int: Sum of all elements

    Complexity:
        Time: O(n)     - Processes each element once.
        Space: O(n)   - Call stack depth is n.
    """
    # Base case
    if not arr:
        return 0
    
    # Recursive case: first element + sum of rest
    return arr[0] + sum_array(arr[1:])


# ----------------------------------------------------------------------
# Power Function (Recursion)
# ----------------------------------------------------------------------
def power(base: int, exponent: int) -> int:
    """
    Calculate base^exponent using recursion.

    Args:
        base (int): Base number
        exponent (int): Non-negative exponent

    Returns:
        int: base^exponent

    Complexity:
        Time: O(log exponent)  - Recursive calls reduce exponent by half.
        Space: O(log exponent) - Call stack depth.
    """
    # Base case
    if exponent == 0:
        return 1
    
    # Recursive case: divide exponent by 2
    if exponent % 2 == 0:
        half = power(base, exponent // 2)
        return half * half
    else:
        return base * power(base, exponent - 1)


# ----------------------------------------------------------------------
# Call Stack Visualization
# ----------------------------------------------------------------------
def demonstrate_call_stack(n: int, depth: int = 0) -> None:
    """
    Demonstrate call stack behavior in recursion.

    Args:
        n (int): Number to count down from
        depth (int): Current recursion depth

    Complexity:
        Time: O(n)     - Makes n recursive calls.
        Space: O(n)   - Call stack depth is n.
    """
    indent = "  " * depth
    print(f"{indent}Call: factorial({n})")
    
    if n <= 1:
        print(f"{indent}Base case reached, returning 1")
        return 1
    
    print(f"{indent}Recursive call: {n} * factorial({n - 1})")
    result = n * demonstrate_call_stack(n - 1, depth + 1)
    print(f"{indent}Returning: {result}")
    return result


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Recursion Concepts Demonstration")
    
    # Factorial
    print("Factorial:")
    for n in range(6):
        print(f"  {n}! = {factorial(n)}")
    
    # Fibonacci
    print("\nFibonacci:")
    for n in range(10):
        print(f"  F({n}) = {fibonacci(n)}")
    
    # Sum of array
    print("\nSum of array:")
    arr = [1, 2, 3, 4, 5]
    print(f"  Sum of {arr} = {sum_array(arr)}")
    
    # Power
    print("\nPower:")
    print(f"  2^10 = {power(2, 10)}")
    
    print("\n" + "="*60)
    print("CALL STACK DEMONSTRATION")
    print("="*60)
    print("Call stack for factorial(4):")
    demonstrate_call_stack(4)
    
    print("\n" + "="*60)
    print("RECURSION COMPLEXITY SUMMARY")
    print("="*60)
    print("""
Operation          Time Complexity    Space Complexity
------------------------------------------------------
Factorial          O(n)               O(n) - call stack
Fibonacci (memo)   O(n)               O(n) - memo + stack
Sum Array          O(n)               O(n) - call stack
Power              O(log n)           O(log n) - call stack

Key Points:
- Base case must be reached to avoid infinite recursion
- Each recursive call uses stack space
- Memoization can reduce time complexity
- Tail recursion optimization can reduce space
""")

