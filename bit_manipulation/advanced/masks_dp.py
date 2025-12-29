"""
Dynamic Programming with Bitmasking

Use bitmasks to represent states in dynamic programming problems.

Common Problems:
1. Traveling Salesman Problem (TSP)
2. Assignment problems
3. Subset DP problems

Why Bitmasking in DP?
---------------------
- Compact state representation
- Efficient state transitions
- Useful for subset-based problems

Useful in:
- TSP and variants
- Assignment problems
- Advanced DP problems
- Less common but valuable
"""

from typing import List


# ----------------------------------------------------------------------
# Traveling Salesman Problem (TSP) with Bitmasking
# ----------------------------------------------------------------------
def tsp_bitmasking(dist: List[List[int]]) -> int:
    """
    Solve Traveling Salesman Problem using DP with bitmasking.

    State: dp[mask][last] = minimum cost to visit all cities in mask,
           ending at city 'last'

    Args:
        dist (List[List[int]]): Distance matrix (n x n)

    Returns:
        int: Minimum cost to visit all cities and return to start

    Complexity:
        Time: O(n² * 2^n)  - n² states, 2^n masks.
        Space: O(n * 2^n) - DP table storage.
    """
    n = len(dist)
    INF = float('inf')
    
    # dp[mask][last] = minimum cost
    dp = [[INF] * n for _ in range(1 << n)]
    
    # Base case: starting from city 0
    dp[1][0] = 0
    
    # Fill DP table
    for mask in range(1, 1 << n):
        for last in range(n):
            if not (mask & (1 << last)):
                continue
            
            if dp[mask][last] == INF:
                continue
            
            # Try visiting next unvisited city
            for next_city in range(n):
                if mask & (1 << next_city):
                    continue
                
                new_mask = mask | (1 << next_city)
                dp[new_mask][next_city] = min(
                    dp[new_mask][next_city],
                    dp[mask][last] + dist[last][next_city]
                )
    
    # Return to starting city (city 0)
    final_mask = (1 << n) - 1
    min_cost = INF
    
    for last in range(n):
        if dp[final_mask][last] != INF:
            min_cost = min(min_cost, dp[final_mask][last] + dist[last][0])
    
    return min_cost if min_cost != INF else -1


# ----------------------------------------------------------------------
# Assignment Problem with Bitmasking
# ----------------------------------------------------------------------
def assignment_bitmasking(cost: List[List[int]]) -> int:
    """
    Solve assignment problem: assign n tasks to n workers with minimum cost.

    State: dp[mask] = minimum cost to assign tasks represented by mask

    Args:
        cost (List[List[int]]): Cost matrix (n x n), cost[i][j] = cost of
                               assigning task i to worker j

    Returns:
        int: Minimum total cost

    Complexity:
        Time: O(n * 2^n)  - n workers, 2^n masks.
        Space: O(2^n)    - DP table storage.
    """
    n = len(cost)
    INF = float('inf')
    
    # dp[mask] = minimum cost to assign tasks in mask
    dp = [INF] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        # Count assigned tasks
        assigned = bin(mask).count('1')
        
        if assigned == n:
            continue
        
        # Try assigning next task to each worker
        for worker in range(n):
            if mask & (1 << worker):
                continue
            
            new_mask = mask | (1 << worker)
            dp[new_mask] = min(
                dp[new_mask],
                dp[mask] + cost[assigned][worker]
            )
    
    return dp[(1 << n) - 1]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: DP with Bitmasking Demonstration")
    
    # TSP example
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print("TSP Distance Matrix:")
    for row in dist:
        print(row)
    
    min_cost = tsp_bitmasking(dist)
    print(f"Minimum TSP cost: {min_cost}")
    
    # Assignment problem
    cost = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]
    print("\nAssignment Cost Matrix:")
    for row in cost:
        print(row)
    
    min_assignment = assignment_bitmasking(cost)
    print(f"Minimum assignment cost: {min_assignment}")

