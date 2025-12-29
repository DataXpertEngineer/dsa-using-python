"""
Balanced Parentheses Checker

Check if a string of parentheses is balanced using stack.

Problem Statement:
-------------------
Given a string containing only parentheses characters '(', ')', '{', '}', '[', ']',
determine if the input string is valid (balanced).

Example:
    Input: "()[]{}"
    Output: True

    Input: "([)]"
    Output: False

Why Stack?
----------
- Need to match opening with closing parentheses
- Last opened must be first closed (LIFO)
- Stack naturally handles this pattern

Useful in:
- Expression validation
- Code parsing
- Common interview problems
"""

from typing import Dict


# ----------------------------------------------------------------------
# Balanced Parentheses Checker (Language-agnostic)
# ----------------------------------------------------------------------
def is_balanced(s: str) -> bool:
    """
    Check if parentheses string is balanced using stack.

    Algorithm:
    1. Use stack to store opening parentheses
    2. For closing parentheses, check if matches top of stack
    3. Stack should be empty at the end

    Args:
        s (str): String containing parentheses

    Returns:
        bool: True if balanced, False otherwise

    Complexity:
        Time: O(n)     - Single pass through string, each char processed once.
        Space: O(n)   - Stack can store up to n/2 opening parentheses.
    """
    stack = []
    mapping: Dict[str, str] = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing parenthesis
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Opening parenthesis
            stack.append(char)
    
    return len(stack) == 0


# ----------------------------------------------------------------------
# Balanced Parentheses with Multiple Types
# ----------------------------------------------------------------------
def is_balanced_multiple(s: str) -> bool:
    """
    Check balanced parentheses for multiple types: (), [], {}, <>

    Args:
        s (str): String containing parentheses

    Returns:
        bool: True if balanced, False otherwise

    Complexity:
        Time: O(n)     - Single pass through string.
        Space: O(n)   - Stack storage.
    """
    stack = []
    opening = set('([{<')
    closing = set(')]}>')
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            top = stack.pop()
            if pairs.get(top) != char:
                return False
    
    return len(stack) == 0


# ----------------------------------------------------------------------
# Count Minimum Additions to Make Balanced
# ----------------------------------------------------------------------
def min_add_to_make_valid(s: str) -> int:
    """
    Find minimum number of parentheses to add to make string valid.

    Args:
        s (str): String containing only '(' and ')'

    Returns:
        int: Minimum additions needed

    Complexity:
        Time: O(n)     - Single pass through string.
        Space: O(1)   - Only uses counter variables.
    """
    open_count = 0
    close_count = 0
    
    for char in s:
        if char == '(':
            open_count += 1
        else:  # char == ')'
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1
    
    return open_count + close_count


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Balanced Parentheses Checker Demonstration")
    
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "((()))",
        "((()",
        ""
    ]
    
    print("Testing balanced parentheses:")
    for test in test_cases:
        result = is_balanced(test)
        print(f"  '{test}': {result}")
    
    # Multiple types
    print("\nTesting multiple types:")
    multi_tests = ["([{}])", "<(>)>", "([)]", "<>"]
    for test in multi_tests:
        result = is_balanced_multiple(test)
        print(f"  '{test}': {result}")
    
    # Minimum additions
    print("\nMinimum additions to make valid:")
    add_tests = ["())", "(((", "()", "()))(("]
    for test in add_tests:
        result = min_add_to_make_valid(test)
        print(f"  '{test}': {result} additions needed")

