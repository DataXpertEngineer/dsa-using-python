"""
Recent Counter / Events Counter

Count events in the last time window using queue.

Problem Statement:
-------------------
Design a RecentCounter class that counts the number of recent requests
within a certain time frame.

Example:
    counter = RecentCounter()
    counter.ping(1)   # Returns 1 (requests: [1])
    counter.ping(100) # Returns 2 (requests: [1, 100])
    counter.ping(3001) # Returns 3 (requests: [1, 100, 3001])
    counter.ping(3002) # Returns 3 (requests: [100, 3001, 3002])
                      # Request at 1 is outside [3002-3000, 3002]

Why Queue?
----------
- Need to remove old events outside time window
- FIFO order matches time order
- Efficient removal from front

Useful in:
- Event tracking
- Rate limiting
- Common interview problems
"""

from collections import deque


class RecentCounter:
    """
    Recent counter that counts events in the last time window.
    """
    
    def __init__(self, window_size: int = 3000):
        """
        Initialize recent counter with time window.

        Args:
            window_size (int): Size of time window in milliseconds

        Complexity:
            Time: O(1)     - Constant time initialization.
            Space: O(1)   - Creates empty deque.
        """
        self.window_size = window_size
        self.requests = deque()
    
    def ping(self, t: int):
        """
        Record a request at time t and return count of recent requests.

        Args:
            t (int): Current timestamp in milliseconds

        Returns:
            int: Number of requests in [t - window_size, t]

        Complexity:
            Time: O(n)     - May need to remove n old requests.
            Space: O(n)   - Stores requests in window.
        """
        # Remove requests outside time window
        while self.requests and self.requests[0] < t - self.window_size:
            self.requests.popleft()
        
        # Add current request
        self.requests.append(t)
        
        return len(self.requests)


# ----------------------------------------------------------------------
# Recent Counter (Alternative: Using List)
# ----------------------------------------------------------------------
class RecentCounterList:
    """
    Recent counter using list (less efficient).
    """
    
    def __init__(self, window_size: int = 3000):
        """
        Initialize recent counter with time window.

        Args:
            window_size (int): Size of time window
        """
        self.window_size = window_size
        self.requests: list[int] = []
    
    def ping(self, t: int):
        """
        Record a request at time t and return count of recent requests.

        Args:
            t (int): Current timestamp

        Returns:
            int: Number of requests in time window

        Complexity:
            Time: O(n)     - May need to remove n old requests.
            Space: O(n)   - Stores requests in window.
        """
        # Remove requests outside time window
        self.requests = [req for req in self.requests if req >= t - self.window_size]
        
        # Add current request
        self.requests.append(t)
        
        return len(self.requests)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Recent Counter Demonstration")
    
    counter = RecentCounter()
    
    print("Recording requests:")
    print(f"  ping(1):    {counter.ping(1)}    requests")
    print(f"  ping(100):  {counter.ping(100)}  requests")
    print(f"  ping(3001): {counter.ping(3001)} requests")
    print(f"  ping(3002): {counter.ping(3002)} requests")
    print(f"  ping(3003): {counter.ping(3003)} requests")
    
    print("\nExplanation:")
    print("  Window size: 3000ms")
    print("  At t=3002: Requests in [2, 3002] are [100, 3001, 3002]")
    print("  Request at t=1 is outside the window")

