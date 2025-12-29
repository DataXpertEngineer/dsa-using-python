"""
Bit Operations in Python

Bit manipulation involves working with individual bits of numbers.
Understanding bit operations is crucial for efficient algorithms and low-level programming.

Covered topics:
- Basic bitwise operators (AND, OR, XOR, NOT)
- Shift operations (left/right shifts)
- Bit toggling and manipulation
- Binary representation
- Common bit patterns
- Basic time & space complexity notes
"""

if __name__ == "__main__":
    # ----------------------------
    # 1. Basic Bitwise Operators
    # ----------------------------
    print("\n🔹 1. BASIC BITWISE OPERATORS")
    
    a = 5   # Binary: 0101
    b = 3   # Binary: 0011
    
    print(f"a = {a} (binary: {bin(a)})")
    print(f"b = {b} (binary: {bin(b)})")
    print()
    
    # AND (&)
    result_and = a & b
    print(f"AND (a & b): {result_and} (binary: {bin(result_and)})")
    print("  Explanation: 0101 & 0011 = 0001 (1)")
    
    # OR (|)
    result_or = a | b
    print(f"OR (a | b): {result_or} (binary: {bin(result_or)})")
    print("  Explanation: 0101 | 0011 = 0111 (7)")
    
    # XOR (^)
    result_xor = a ^ b
    print(f"XOR (a ^ b): {result_xor} (binary: {bin(result_xor)})")
    print("  Explanation: 0101 ^ 0011 = 0110 (6)")
    
    # NOT (~)
    result_not_a = ~a
    print(f"NOT (~a): {result_not_a} (binary: {bin(result_not_a & 0xFF)})")
    print("  Explanation: ~0101 = ...11111010 (two's complement)")
    
    # Time Complexity: All bitwise operations are O(1)
    # Space Complexity: O(1)

    # ----------------------------
    # 2. Shift Operations
    # ----------------------------
    print("\n🔹 2. SHIFT OPERATIONS")
    
    num = 5  # Binary: 0101
    print(f"Number: {num} (binary: {bin(num)})")
    
    # Left shift (<<)
    left_shift = num << 1
    print(f"Left shift (num << 1): {left_shift} (binary: {bin(left_shift)})")
    print("  Explanation: 0101 << 1 = 1010 (10) - multiply by 2")
    
    left_shift2 = num << 2
    print(f"Left shift (num << 2): {left_shift2} (binary: {bin(left_shift2)})")
    print("  Explanation: 0101 << 2 = 10100 (20) - multiply by 4")
    
    # Right shift (>>)
    right_shift = num >> 1
    print(f"Right shift (num >> 1): {right_shift} (binary: {bin(right_shift)})")
    print("  Explanation: 0101 >> 1 = 0010 (2) - divide by 2")
    
    right_shift2 = num >> 2
    print(f"Right shift (num >> 2): {right_shift2} (binary: {bin(right_shift2)})")
    print("  Explanation: 0101 >> 2 = 0001 (1) - divide by 4")
    
    # Time Complexity: Shift operations are O(1)
    # Space Complexity: O(1)

    # ----------------------------
    # 3. Bit Toggling
    # ----------------------------
    print("\n🔹 3. BIT TOGGLING")
    
    num = 5  # Binary: 0101
    print(f"Original: {num} (binary: {bin(num)})")
    
    # Set bit at position i (make it 1)
    i = 0
    num_set = num | (1 << i)
    print(f"Set bit at position {i}: {num_set} (binary: {bin(num_set)})")
    
    # Clear bit at position i (make it 0)
    i = 2
    num_clear = num & ~(1 << i)
    print(f"Clear bit at position {i}: {num_clear} (binary: {bin(num_clear)})")
    
    # Toggle bit at position i (flip it)
    i = 1
    num_toggle = num ^ (1 << i)
    print(f"Toggle bit at position {i}: {num_toggle} (binary: {bin(num_toggle)})")
    
    # Check if bit is set
    i = 0
    is_set = (num >> i) & 1
    print(f"Bit at position {i} is set: {bool(is_set)}")

    # ----------------------------
    # 4. Common Bit Patterns
    # ----------------------------
    print("\n🔹 4. COMMON BIT PATTERNS")
    
    # All ones
    all_ones = (1 << 8) - 1  # 8 bits all set
    print(f"All ones (8 bits): {all_ones} (binary: {bin(all_ones)})")
    
    # Power of 2
    power_of_2 = 1 << 5  # 2^5 = 32
    print(f"Power of 2 (2^5): {power_of_2} (binary: {bin(power_of_2)})")
    
    # Mask for lower n bits
    n = 4
    lower_n_bits = (1 << n) - 1
    print(f"Mask for lower {n} bits: {lower_n_bits} (binary: {bin(lower_n_bits)})")
    
    # Isolate rightmost set bit
    num = 12  # Binary: 1100
    rightmost_set = num & (-num)
    print(f"Rightmost set bit of {num}: {rightmost_set} (binary: {bin(rightmost_set)})")

    # ----------------------------
    # 5. Binary Representation
    # ----------------------------
    print("\n🔹 5. BINARY REPRESENTATION")
    
    num = 42
    print(f"Number: {num}")
    print(f"Binary: {bin(num)}")
    print(f"Binary (without 0b): {bin(num)[2:]}")
    print(f"Binary with padding: {bin(num)[2:].zfill(8)}")
    
    # Convert binary string to int
    binary_str = "101010"
    num_from_binary = int(binary_str, 2)
    print(f"\nBinary string '{binary_str}' to int: {num_from_binary}")

    # ----------------------------
    # 6. Summary of Complexity
    # ----------------------------
    print("\n" + "="*60)
    print("SUMMARY OF TIME & SPACE COMPLEXITY")
    print("="*60)
    print("""
Operation                     Time Complexity    Space Complexity
----------------------------------------------------------------
AND (&), OR (|), XOR (^)      O(1)              O(1)
NOT (~)                       O(1)              O(1)
Left shift (<<)               O(1)              O(1)
Right shift (>>)               O(1)              O(1)
Set/Clear/Toggle bit          O(1)              O(1)
Check bit                     O(1)              O(1)
Binary conversion              O(log n)          O(log n)

Where n is the number value.
All bitwise operations are extremely fast (hardware-level).
""")

