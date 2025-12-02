"""
Best Time to Buy and Sell Stock Problem

Find the maximum profit from buying and selling a stock.

Problem Statement:
------------------
You are given an array prices where prices[i] is the price of a given stock on day i.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.

Example:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Variations:
- Single transaction (this problem)
- Multiple transactions allowed
- At most k transactions
- With cooldown period

Useful in:
- Dynamic programming
- Array manipulation
- Common interview problem
"""

from typing import List, Tuple


# ----------------------------------------------------------------------
# Brute-force Approach (Language-agnostic)
# ----------------------------------------------------------------------
def max_profit_naive(prices: List[int]) -> int:
    """
    Find maximum profit using brute-force approach (check all pairs).

    This approach works in all programming languages.

    Args:
        prices (List[int]): Array of stock prices

    Returns:
        int: Maximum profit (0 if no profit possible)

    Complexity:
        Time: O(n²)    - Nested loops check all buy-sell pairs.
        Space: O(1)   - Only uses variables for tracking max profit.
    """
    max_profit = 0
    n = len(prices)
    
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit


# ----------------------------------------------------------------------
# Optimal Approach (Language-agnostic)
# ----------------------------------------------------------------------
def max_profit(prices: List[int]) -> int:
    """
    Find maximum profit using optimal single-pass approach.

    Track the minimum price seen so far and calculate profit for each day.

    Args:
        prices (List[int]): Array of stock prices

    Returns:
        int: Maximum profit (0 if no profit possible)

    Complexity:
        Time: O(n)     - Single pass through array, constant work per element.
        Space: O(1)   - Only uses variables for min_price and max_profit.
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        # Calculate profit if we sell today
        profit = price - min_price
        max_profit = max(max_profit, profit)
    
    return max_profit


def max_profit_with_days(prices: List[int]) -> Tuple[int, int, int]:
    """
    Find maximum profit and return the buy and sell days.

    Args:
        prices (List[int]): Array of stock prices

    Returns:
        Tuple[int, int, int]: (max_profit, buy_day, sell_day)

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(1)   - Only uses variables for tracking.
    """
    if not prices:
        return (0, 0, 0)
    
    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0
    min_day = 0
    
    for i in range(1, len(prices)):
        price = prices[i]
        if price < min_price:
            min_price = price
            min_day = i
        
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
            buy_day = min_day
            sell_day = i
    
    return (max_profit, buy_day, sell_day)


# ----------------------------------------------------------------------
# Multiple Transactions Allowed (Language-agnostic)
# ----------------------------------------------------------------------
def max_profit_multiple_transactions(prices: List[int]) -> int:
    """
    Find maximum profit when multiple transactions are allowed.

    Strategy: Buy before every price increase, sell before every price decrease.
    Essentially, sum all positive price differences.

    Args:
        prices (List[int]): Array of stock prices

    Returns:
        int: Maximum profit from multiple transactions

    Complexity:
        Time: O(n)     - Single pass through array.
        Space: O(1)   - Only uses variables for tracking profit.
    """
    if not prices:
        return 0
    
    max_profit = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    
    return max_profit


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Best Time to Buy and Sell Stock Demonstration")
    
    prices1 = [7, 1, 5, 3, 6, 4]
    print("Stock prices:", prices1)
    
    # Single transaction
    profit = max_profit(prices1)
    print(f"\nMaximum profit (single transaction): {profit}")
    
    profit, buy_day, sell_day = max_profit_with_days(prices1)
    print(f"Buy on day {buy_day} (price={prices1[buy_day]}), "
          f"sell on day {sell_day} (price={prices1[sell_day]})")
    print(f"Profit: {prices1[sell_day]} - {prices1[buy_day]} = {profit}")
    
    # Multiple transactions
    print("\n" + "="*50)
    profit_multiple = max_profit_multiple_transactions(prices1)
    print(f"Maximum profit (multiple transactions): {profit_multiple}")
    print("Strategy: Buy at 1, sell at 5; buy at 3, sell at 6")
    print("Total profit: (5-1) + (6-3) = 7")
    
    # Test with decreasing prices (no profit)
    print("\n" + "="*50)
    prices2 = [7, 6, 4, 3, 1]
    print("Stock prices (decreasing):", prices2)
    profit2 = max_profit(prices2)
    print(f"Maximum profit: {profit2} (no profit possible)")
    
    # Test with single price
    print("\n" + "="*50)
    prices3 = [5]
    print("Stock prices (single day):", prices3)
    profit3 = max_profit(prices3)
    print(f"Maximum profit: {profit3}")

