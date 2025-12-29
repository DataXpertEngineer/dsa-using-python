"""
Greedy Algorithms

Greedy algorithms make locally optimal choices at each step with the hope
of finding a global optimum.

Why Greedy?
-----------
- Simple and intuitive
- Often efficient
- Good for optimization problems
- Foundation for many algorithms

Characteristics:
- Make best choice at each step
- No reconsideration of previous choices
- Hope local optimum leads to global optimum

Useful in:
- Optimization problems
- Scheduling problems
- Graph algorithms (MST, shortest path)
- Common interview problems
"""

from typing import List, Tuple, Optional


# ----------------------------------------------------------------------
# Greedy Algorithm Template
# ----------------------------------------------------------------------
def greedy_template(items: List, criteria: callable) -> List:
    """
    Generic greedy algorithm template.

    Algorithm:
    1. Sort items by some criteria
    2. Process items in order
    3. Make greedy choice at each step
    4. Return solution

    Args:
        items (List): Items to process
        criteria (callable): Sorting criteria

    Returns:
        List: Greedy solution

    Complexity:
        Time: O(n log n)  - Sorting + processing.
        Space: O(n)      - Storage for solution.
    """
    # Sort by criteria
    sorted_items = sorted(items, key=criteria)
    
    solution = []
    for item in sorted_items:
        # Make greedy choice
        if is_valid_choice(item, solution):
            solution.append(item)
    
    return solution


def is_valid_choice(item, solution: List) -> bool:
    """
    Check if item can be added to solution.

    Args:
        item: Item to check
        solution (List): Current solution

    Returns:
        bool: True if valid choice
    """
    # Implementation depends on problem
    return True


# ----------------------------------------------------------------------
# Example: Coin Change (Greedy)
# ----------------------------------------------------------------------
def coin_change_greedy(amount: int, coins: List[int]) -> Optional[List[int]]:
    """
    Greedy coin change (works for certain coin systems).

    Note: Greedy doesn't always give optimal solution.
    Works for: US coins (1, 5, 10, 25)

    Args:
        amount (int): Target amount
        coins (List[int]): Available coins (sorted descending)

    Returns:
        Optional[List[int]]: Coins used, None if impossible

    Complexity:
        Time: O(amount / min_coin)  - Number of iterations.
        Space: O(amount / min_coin) - Storage for result.
    """
    coins.sort(reverse=True)
    result = []
    remaining = amount
    
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result.extend([coin] * count)
            remaining -= coin * count
        
        if remaining == 0:
            return result
    
    return None if remaining > 0 else result


# ----------------------------------------------------------------------
# Example: Fractional Knapsack
# ----------------------------------------------------------------------
def fractional_knapsack(capacity: int, items: List[Tuple[int, int]]) -> float:
    """
    Fractional knapsack using greedy (value/weight ratio).

    Args:
        capacity (int): Knapsack capacity
        items (List[Tuple[int, int]]): List of (value, weight) pairs

    Returns:
        float: Maximum value

    Complexity:
        Time: O(n log n)  - Sort by ratio.
        Space: O(1)     - Only uses variables.
    """
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for value, weight in items:
        if remaining_capacity >= weight:
            # Take entire item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            break
    
    return total_value


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Greedy Algorithms Demonstration")
    
    # Coin change
    print("Coin Change (Greedy):")
    amount = 67
    coins = [25, 10, 5, 1]
    result = coin_change_greedy(amount, coins)
    print(f"  Amount: {amount}, Coins: {coins}")
    print(f"  Result: {result}")
    
    # Fractional knapsack
    print("\n" + "="*50)
    print("Fractional Knapsack:")
    capacity = 50
    items = [(60, 10), (100, 20), (120, 30)]
    max_value = fractional_knapsack(capacity, items)
    print(f"  Capacity: {capacity}")
    print(f"  Items (value, weight): {items}")
    print(f"  Maximum value: {max_value}")
    
    print("\n" + "="*60)
    print("GREEDY ALGORITHM CONCEPTS SUMMARY")
    print("="*60)
    print("""
Greedy Algorithm Properties:
- Makes locally optimal choice at each step
- Never reconsider previous choices
- Hopes local optimum = global optimum
- Simple and efficient

When Greedy Works:
- Greedy choice property: Local optimum leads to global optimum
- Optimal substructure: Optimal solution contains optimal sub-solutions
- Examples: MST, shortest path (Dijkstra), activity selection

When Greedy Fails:
- Coin change (general case)
- 0/1 Knapsack
- Job scheduling (general case)

Common Patterns:
1. Sort by some criteria
2. Process in order
3. Make greedy choice
4. Verify solution
""")

