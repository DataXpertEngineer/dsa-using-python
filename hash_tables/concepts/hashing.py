"""
Hash Functions and Hashing Concepts

Hash functions map data of arbitrary size to fixed-size values (hash codes).
Good hash functions distribute keys uniformly across hash table.

Types of Hash Functions:
1. Modular hashing: h(k) = k mod m
2. Multiplicative hashing
3. String hashing (polynomial rolling hash)
4. Universal hashing

Why Hash Functions?
-------------------
- Fast key-to-index mapping
- Uniform distribution reduces collisions
- Essential for hash table performance

Useful in:
- Hash table implementation
- String matching
- Cryptography
- Common interview problems
"""

from typing import Any


# ----------------------------------------------------------------------
# Modular Hashing
# ----------------------------------------------------------------------
def modular_hash(key: int, table_size: int) -> int:
    """
    Hash function using modular arithmetic.

    Formula: h(k) = k mod m

    Args:
        key (int): Key to hash
        table_size (int): Size of hash table

    Returns:
        int: Hash index

    Complexity:
        Time: O(1)     - Single modulo operation.
        Space: O(1)   - Only uses variables.
    """
    return key % table_size


# ----------------------------------------------------------------------
# Multiplicative Hashing
# ----------------------------------------------------------------------
def multiplicative_hash(key: int, table_size: int, A: float = 0.6180339887) -> int:
    """
    Multiplicative hash function.

    Formula: h(k) = floor(m * ((k * A) mod 1))
    where A is a constant (often (sqrt(5) - 1) / 2)

    Args:
        key (int): Key to hash
        table_size (int): Size of hash table
        A (float): Multiplicative constant

    Returns:
        int: Hash index

    Complexity:
        Time: O(1)     - Constant time operations.
        Space: O(1)   - Only uses variables.
    """
    import math
    fractional_part = (key * A) % 1
    return int(table_size * fractional_part)


# ----------------------------------------------------------------------
# String Hashing (Polynomial Rolling Hash)
# ----------------------------------------------------------------------
def string_hash(s: str, base: int = 31, mod: int = 10**9 + 7) -> int:
    """
    Hash function for strings using polynomial rolling hash.

    Formula: hash(s) = (s[0] * base^0 + s[1] * base^1 + ... + s[n-1] * base^(n-1)) mod m

    Args:
        s (str): String to hash
        base (int): Base for polynomial (prime number)
        mod (int): Modulus (large prime)

    Returns:
        int: Hash value

    Complexity:
        Time: O(n)     - Processes each character once.
        Space: O(1)   - Only uses variables.
    """
    hash_value = 0
    power = 1
    
    for char in s:
        hash_value = (hash_value + (ord(char) * power)) % mod
        power = (power * base) % mod
    
    return hash_value


# ----------------------------------------------------------------------
# String Hashing (Simple)
# ----------------------------------------------------------------------
def simple_string_hash(s: str, table_size: int) -> int:
    """
    Simple string hash function (sum of character codes).

    Args:
        s (str): String to hash
        table_size (int): Size of hash table

    Returns:
        int: Hash index

    Complexity:
        Time: O(n)     - Sums all character codes.
        Space: O(1)   - Only uses variables.
    """
    hash_value = 0
    for char in s:
        hash_value += ord(char)
    return hash_value % table_size


# ----------------------------------------------------------------------
# Python Built-in Hash
# ----------------------------------------------------------------------
def python_hash(key: Any) -> int:
    """
    Use Python's built-in hash function.

    Args:
        key: Key to hash (must be hashable)

    Returns:
        int: Hash value

    Complexity:
        Time: O(1) for simple types, O(n) for strings.
        Space: O(1) - Only uses variables.
    """
    return hash(key)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Hash Functions Demonstration")
    
    # Modular hashing
    print("Modular Hashing:")
    keys = [10, 25, 37, 42, 58]
    table_size = 7
    for key in keys:
        index = modular_hash(key, table_size)
        print(f"  {key} -> {index}")
    
    # Multiplicative hashing
    print("\nMultiplicative Hashing:")
    for key in keys:
        index = multiplicative_hash(key, table_size)
        print(f"  {key} -> {index}")
    
    # String hashing
    print("\nString Hashing (Polynomial Rolling):")
    strings = ["hello", "world", "python", "hash"]
    for s in strings:
        hash_val = string_hash(s)
        print(f"  '{s}' -> {hash_val}")
    
    # Simple string hash
    print("\nSimple String Hashing:")
    for s in strings:
        index = simple_string_hash(s, table_size)
        print(f"  '{s}' -> {index}")
    
    # Python built-in hash
    print("\nPython Built-in Hash:")
    test_keys = [10, "hello", (1, 2, 3)]
    for key in test_keys:
        hash_val = python_hash(key)
        print(f"  {key} -> {hash_val}")

