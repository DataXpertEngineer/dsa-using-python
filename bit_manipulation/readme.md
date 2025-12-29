# Bit Manipulation

Bit manipulation involves working with individual bits of numbers. Understanding bit operations is crucial for efficient algorithms, low-level programming, and solving many competitive programming problems.

## 📁 Folder Structure

```
bit_manipulation/
├── bits.py                            # Core bit operations ⭐ MOST IMPORTANT
├── techniques/                        # Bit manipulation techniques
│   ├── bitmasking.py                  # Set, clear, toggle bits, subset generation ⭐ MOST IMPORTANT
│   ├── xor_tricks.py                  # XOR properties, swapping, unique elements ⭐ MOST IMPORTANT
│   ├── counting_bits.py               # Count set bits (Brian Kernighan, lookup) ⭐ MOST IMPORTANT
│   ├── shift_operations.py            # Left/right shifts, arithmetic vs logical shift ⭐ MOST IMPORTANT
│   └── power_checks.py                # Power of 2, 4 checks using bits ⭐ MOST IMPORTANT
├── algorithms/                        # Bit-based algorithms
│   ├── single_number.py               # Find element appearing once/twice/thrice ⭐ MOST IMPORTANT
│   ├── subset_generation.py           # Generate all subsets using bitmasking 🟡 MEDIUM
│   ├── gray_code.py                   # Gray code generation 🔴 LEAST IMPORTANT
│   └── hamming_distance.py            # Hamming distance and similarity ⭐ MOST IMPORTANT
├── math_and_number_theory/            # Bitwise math problems
│   ├── fast_exponentiation.py         # Binary exponentiation 🟡 MEDIUM
│   ├── add_without_plus.py            # Add numbers without '+' operator 🟡 MEDIUM
│   └── divide_without_operator.py     # Divide without *, /, % 🔴 LEAST IMPORTANT
├── interview_problems/                # Common interview questions
│   ├── set_bits_count.py              # Count number of 1s in binary ⭐ MOST IMPORTANT
│   ├── power_of_two.py                # Check if number is power of 2 ⭐ MOST IMPORTANT
│   ├── missing_number.py              # Find missing number using XOR ⭐ MOST IMPORTANT
│   ├── find_two_unique.py             # Two unique numbers in array ⭐ MOST IMPORTANT
│   ├── reverse_bits.py                # Reverse bits of an integer 🟡 MEDIUM
│   ├── bit_difference.py              # Number of bits to flip A → B ⭐ MOST IMPORTANT
│   └── maximum_xor.py                 # Maximum XOR of two numbers 🟡 MEDIUM
└── advanced/                          # Advanced & less common (but valuable)
    ├── trie_bitwise.py                # Bitwise Trie for max XOR problems 🔴 LEAST IMPORTANT
    ├── range_xor.py                   # XOR of range queries 🔴 LEAST IMPORTANT
    └── masks_dp.py                    # DP with bitmasking (TSP, assignments) 🔴 LEAST IMPORTANT
```

## 📚 Core Concepts

### Basic Bitwise Operators

- **AND (&)**: Both bits must be 1
- **OR (|)**: At least one bit is 1
- **XOR (^)**: Bits differ (exactly one is 1)
- **NOT (~)**: Flip all bits
- **Left Shift (<<)**: Multiply by powers of 2
- **Right Shift (>>)**: Divide by powers of 2

### Key Properties

1. **XOR Properties**:
   - `a ^ a = 0` (XOR with itself is zero)
   - `a ^ 0 = a` (XOR with zero is identity)
   - `a ^ b = b ^ a` (commutative)
   - `(a ^ b) ^ c = a ^ (b ^ c)` (associative)

2. **Power of 2**:
   - Has exactly one set bit
   - `n & (n - 1) == 0` for n > 0

3. **Bitmasking**:
   - Use binary numbers to represent sets
   - Each bit represents presence/absence of element
   - Efficient set operations (union, intersection, difference)

## 🎯 Techniques

### 1. Bitmasking (`techniques/bitmasking.py`)
- Set, clear, toggle bits
- Subset generation
- Set operations (union, intersection, difference)
- **Time Complexity**: O(1) for basic operations, O(n * 2^n) for subset generation
- **Space Complexity**: O(1) for basic operations, O(n * 2^n) for subsets

### 2. XOR Tricks (`techniques/xor_tricks.py`)
- Swap without temporary variable
- Find single/double unique elements
- Missing number detection
- **Time Complexity**: O(n) for array operations
- **Space Complexity**: O(1)

### 3. Counting Bits (`techniques/counting_bits.py`)
- Naive approach: O(log n)
- Brian Kernighan's algorithm: O(k) where k is number of set bits
- Lookup table: O(1) for 32/64-bit numbers
- **Space Complexity**: O(1) for all approaches

### 4. Shift Operations (`techniques/shift_operations.py`)
- Left shift: multiply by 2^positions
- Right shift: divide by 2^positions
- Bit extraction
- Rotation
- **Time Complexity**: O(1) for all operations

### 5. Power Checks (`techniques/power_checks.py`)
- Power of 2: O(1) using `n & (n - 1) == 0`
- Power of 4: Check power of 2 and even bit position
- **Time Complexity**: O(1) for power checks

## 🔍 Algorithms

### 1. Single Number Problems (`algorithms/single_number.py`)
- **Single Number**: All appear twice except one → O(n) time, O(1) space
- **Single Number II**: All appear three times except one → O(n) time, O(1) space
- **Single Number III**: All appear twice except two → O(n) time, O(1) space

### 2. Subset Generation (`algorithms/subset_generation.py`)
- Generate all subsets using bitmasking
- **Time Complexity**: O(n * 2^n)
- **Space Complexity**: O(n * 2^n)

### 3. Gray Code (`algorithms/gray_code.py`)
- Generate n-bit Gray code sequence
- Convert binary to Gray code and vice versa
- **Time Complexity**: O(2^n) for generation

### 4. Hamming Distance (`algorithms/hamming_distance.py`)
- Calculate Hamming distance between two numbers
- Total Hamming distance for all pairs
- **Time Complexity**: O(log n) or O(k) where k is number of differing bits

## 🧮 Math & Number Theory

### 1. Fast Exponentiation (`math_and_number_theory/fast_exponentiation.py`)
- Binary exponentiation: O(log b) time
- Modular exponentiation
- **Space Complexity**: O(1)

### 2. Add Without Plus (`math_and_number_theory/add_without_plus.py`)
- Add two numbers using only bitwise operations
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

### 3. Divide Without Operator (`math_and_number_theory/divide_without_operator.py`)
- Divide using only bitwise operations
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## 💼 Interview Problems

### Most Important (⭐)

1. **Set Bits Count** (`interview_problems/set_bits_count.py`)
   - Count number of 1s in binary representation
   - Multiple approaches: naive, Kernighan's, built-in

2. **Power of Two** (`interview_problems/power_of_two.py`)
   - Check if number is power of 2
   - O(1) solution using bit manipulation

3. **Missing Number** (`interview_problems/missing_number.py`)
   - Find missing number using XOR
   - O(n) time, O(1) space

4. **Find Two Unique** (`interview_problems/find_two_unique.py`)
   - Find two numbers appearing once
   - Uses XOR and bit partitioning

5. **Bit Difference** (`interview_problems/bit_difference.py`)
   - Number of bits to flip to convert A to B
   - Hamming distance calculation

### Medium Difficulty (🟡)

6. **Reverse Bits** (`interview_problems/reverse_bits.py`)
   - Reverse bits of 32-bit integer
   - Multiple approaches

7. **Maximum XOR** (`interview_problems/maximum_xor.py`)
   - Maximum XOR of two numbers in array
   - Brute force and Trie-based solutions

## 🚀 Advanced Topics

### 1. Bitwise Trie (`advanced/trie_bitwise.py`)
- Trie optimized for bitwise operations
- Maximum XOR queries: O(32) per query
- **Time Complexity**: O(n * 32) for n numbers
- **Space Complexity**: O(n * 32)

### 2. Range XOR (`advanced/range_xor.py`)
- Efficient range XOR queries using prefix XOR
- O(1) query time after O(n) preprocessing
- **Space Complexity**: O(n) for prefix array

### 3. DP with Bitmasking (`advanced/masks_dp.py`)
- Traveling Salesman Problem (TSP)
- Assignment problems
- **Time Complexity**: O(n² * 2^n) for TSP
- **Space Complexity**: O(n * 2^n)

## 📊 Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Basic bitwise operations | O(1) | O(1) |
| Count set bits (naive) | O(log n) | O(1) |
| Count set bits (Kernighan) | O(k) | O(1) |
| Single number (XOR) | O(n) | O(1) |
| Subset generation | O(n * 2^n) | O(n * 2^n) |
| Fast exponentiation | O(log b) | O(1) |
| Maximum XOR (Trie) | O(n * 32) | O(n * 32) |
| TSP with bitmasking | O(n² * 2^n) | O(n * 2^n) |

Where:
- `n` = number of elements
- `k` = number of set bits
- `b` = exponent value

## 🎓 Learning Path

1. **Start with**: `bits.py` - Understand basic operations
2. **Learn techniques**: 
   - `bitmasking.py` - Set operations
   - `xor_tricks.py` - XOR properties
   - `counting_bits.py` - Bit counting
3. **Practice algorithms**:
   - `single_number.py` - Unique element problems
   - `hamming_distance.py` - Distance calculations
4. **Solve interview problems**: Start with ⭐ marked problems
5. **Advanced topics**: Explore when comfortable with basics

## 💡 Key Insights

1. **XOR is powerful**: Use for finding unique elements, swapping, canceling pairs
2. **Bitmasking for subsets**: Efficient representation of sets and combinations
3. **Power of 2 checks**: `n & (n - 1) == 0` is O(1)
4. **Brian Kernighan's algorithm**: Clears rightmost set bit efficiently
5. **Shift operations**: Fast multiplication/division by powers of 2

## 🔗 Related Topics

- **Arrays**: Bit manipulation often used in array problems
- **Dynamic Programming**: Bitmasking for state representation
- **Trie**: Bitwise Trie for XOR problems
- **Number Theory**: Fast exponentiation, modular arithmetic

## 📝 Notes

- All implementations include both language-agnostic and Python-specific approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings

