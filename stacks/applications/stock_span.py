"""
Stock Span Problem

Calculate the stock span for each day using stack.

Problem Statement:
-------------------
The stock span is the maximum number of consecutive days (including current day)
for which the stock price was less than or equal to current day's price.

Example:
    Input: [100, 80, 60, 70, 60, 75, 85]
    Output: [1, 1, 1, 2, 1, 4, 6]
    Explanation:
        Day 0: 100 -> span = 1 (only itself)
        Day 1: 80 -> span = 1 (80 < 100)
        Day 2: 60 -> span = 1 (60 < 80)
        Day 3: 70 -> span = 2 (70 >= 60, 70 < 80)
        Day 4: 60 -> span = 1 (60 < 70)
        Day 5: 75 -> span = 4 (75 >= 60, 70, 60, 75 < 80)
        Day 6: 85 -> span = 6 (85 >= 75, 60, 70, 60, 80, 85 < 100)

Why Stack?
----------
- Need to find previous greater element
- Stack maintains decreasing sequence
- Efficient O(n) solution

Useful in:
- Financial calculations
- Monotonic stack problems
- Medium difficulty interview problems
"""

from typing import List


# ----------------------------------------------------------------------
# Stock Span Problem (Language-agnostic)
# ----------------------------------------------------------------------
def stock_span(prices: List[int]) -> List[int]:
    """
    Calculate stock span for each day using stack.

    Algorithm:
    1. Use stack to store indices of prices
    2. For each day, pop indices where price <= current
    3. Span = current index - previous greater index
    4. Push current index to stack

    Args:
        prices (List[int]): Stock prices for each day

    Returns:
        List[int]: Span for each day

    Complexity:
        Time: O(n)     - Each index pushed and popped at most once.
        Space: O(n)   - Stack and result array storage.
    """
    n = len(prices)
    span = [0] * n
    stack: List[int] = []  # Store indices
    
    for i in range(n):
        # Pop indices where price <= current price
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        # Calculate span
        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1  # All previous days
        
        stack.append(i)
    
    return span


# ----------------------------------------------------------------------
# Stock Span (Alternative Implementation)
# ----------------------------------------------------------------------
def stock_span_alternative(prices: List[int]) -> List[int]:
    """
    Alternative implementation of stock span.

    Args:
        prices (List[int]): Stock prices

    Returns:
        List[int]: Span for each day

    Complexity:
        Time: O(n)     - Single pass through prices.
        Space: O(n)   - Stack and result storage.
    """
    n = len(prices)
    span = [1] * n
    stack: List[int] = []
    
    for i in range(n):
        while stack and prices[stack[-1]] < prices[i]:
            stack.pop()
        
        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1
        
        stack.append(i)
    
    return span


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Stock Span Problem Demonstration")
    
    prices = [100, 80, 60, 70, 60, 75, 85]
    print(f"Stock prices: {prices}")
    
    span = stock_span(prices)
    print(f"Stock span:   {span}")
    
    print("\nDetailed explanation:")
    for i, (price, s) in enumerate(zip(prices, span)):
        print(f"  Day {i}: Price = {price}, Span = {s}")
    
    # Another example
    print("\n" + "="*50)
    prices2 = [10, 4, 5, 90, 120, 80]
    print(f"Stock prices: {prices2}")
    span2 = stock_span(prices2)
    print(f"Stock span:   {span2}")

