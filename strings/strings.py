"""
String operations in Python.

Covered topics:
- Creation
- Access
- Slicing
- Concatenation
- Length
- Basic manipulations
- Immutability
- Common string operations
- Basic time & space complexity notes
"""

if __name__ == "__main__":
    # ----------------------------
    # 1. Creating Strings
    # ----------------------------
    print("\n🔹 1. STRING CREATION")

    str1 = ""                    # empty string
    str2 = "Hello"               # direct initialization
    str3 = 'World'               # single quotes
    str4 = """Multi-line
    string"""                    # triple quotes
    str5 = str(123)              # conversion from number

    print("str1 (empty):", str1)
    print("str2:", str2)
    print("str3:", str3)
    print("str4:", str4)
    print("str5 (from number):", str5)

    # Time Complexity:
    # - Creating with a literal is O(n) for n characters.
    # - Conversion from other types depends on the type.
    # Space Complexity: O(n) for storing n characters.

    # ----------------------------
    # 2. Accessing & Slicing
    # ----------------------------
    print("\n🔹 2. ACCESSING CHARACTERS & SLICING")

    s = "Python"
    print("String:", s)
    print("First character s[0]:", s[0])
    print("Last character s[-1]:", s[-1])
    print("Slice s[1:4]:", s[1:4])
    print("Slice s[:3]:", s[:3])
    print("Slice s[3:]:", s[3:])
    print("Slice s[::-1]:", s[::-1])  # reverse

    # Time Complexity:
    # - Accessing s[i] is O(1) because strings support indexing.
    # - Slicing s[a:b] is O(k) where k is the length of the slice.
    # Space Complexity:
    # - Single character access: O(1) extra space.
    # - Slicing: O(k) extra space for the new string.

    # ----------------------------
    # 3. String Immutability
    # ----------------------------
    print("\n🔹 3. STRING IMMUTABILITY")

    s = "Hello"
    print("Original string:", s)
    # s[0] = 'h'  # This would raise TypeError: 'str' object does not support item assignment
    s = s + " World"  # Creates a new string
    print("After concatenation:", s)

    # Time Complexity:
    # - String concatenation creates a new string: O(n + m) where n and m are lengths.
    # Space Complexity: O(n + m) for the new string.

    # ----------------------------
    # 4. Concatenation
    # ----------------------------
    print("\n🔹 4. CONCATENATION")

    s1 = "Hello"
    s2 = "World"
    s3 = s1 + " " + s2           # Using + operator
    s4 = " ".join([s1, s2])      # Using join (more efficient for multiple strings)
    s5 = f"{s1} {s2}"            # Using f-string

    print("Using +:", s3)
    print("Using join:", s4)
    print("Using f-string:", s5)

    # Time Complexity:
    # - + operator: O(n + m) for each concatenation.
    # - join(): O(n) where n is total length (more efficient for multiple strings).
    # - f-string: O(n + m) for formatting.
    # Space Complexity: O(n + m) for new strings.

    # ----------------------------
    # 5. Length
    # ----------------------------
    print("\n🔹 5. LENGTH")

    s = "Python Programming"
    print("String:", s)
    print("Length len(s):", len(s))

    # Time Complexity:
    # - len(string) is O(1) because Python stores length internally.
    # Space Complexity: O(1) extra space.

    # ----------------------------
    # 6. Common String Operations
    # ----------------------------
    print("\n🔹 6. COMMON STRING OPERATIONS")

    s = "  Hello World  "
    print("Original:", repr(s))
    print("Upper:", s.upper())
    print("Lower:", s.lower())
    print("Strip:", s.strip())
    print("Replace:", s.replace("World", "Python"))
    print("Split:", s.split())
    print("Find 'World':", s.find("World"))
    print("Count 'l':", s.count("l"))

    # Time Complexity:
    # - upper(), lower(): O(n) - must process all characters.
    # - strip(): O(n) - may need to check both ends.
    # - replace(): O(n) - scans entire string.
    # - split(): O(n) - processes all characters.
    # - find(): O(n) - may scan entire string.
    # - count(): O(n) - scans entire string.
    # Space Complexity: O(n) for operations that create new strings.

    # ----------------------------
    # 7. Membership & Comparison
    # ----------------------------
    print("\n🔹 7. MEMBERSHIP & COMPARISON")

    s = "Python"
    print("String:", s)
    print("'th' in s:", "th" in s)
    print("'xyz' in s:", "xyz" in s)
    print("s.startswith('Py'):", s.startswith("Py"))
    print("s.endswith('on'):", s.endswith("on"))
    print("'Python' == 'Python':", "Python" == "Python")
    print("'Python' < 'Python3':", "Python" < "Python3")

    # Time Complexity:
    # - 'in' operator: O(n) in worst case (substring search).
    # - startswith(), endswith(): O(k) where k is length of prefix/suffix.
    # - Comparison: O(min(n, m)) where n and m are string lengths.
    # Space Complexity: O(1) extra space.

    # ----------------------------
    # 8. Iteration
    # ----------------------------
    print("\n🔹 8. ITERATION")

    s = "Python"
    print("String:", s)
    print("Iteration using for loop:", end=" ")
    for char in s:
        print(char, end=" ")
    print()

    print("Iteration with index:", end=" ")
    for i, char in enumerate(s):
        print(f"{i}:{char}", end=" ")
    print()

    # List comprehension
    chars = [c.upper() for c in s]
    print("Uppercase chars using list comprehension:", chars)

    # Time Complexity:
    # - Iteration is O(n) because each character is visited once.
    # - List comprehension is O(n) for processing all characters.
    # Space Complexity:
    # - Simple iteration: O(1) extra space.
    # - List comprehension: O(n) space for the new list.

    # ----------------------------
    # 9. String Formatting
    # ----------------------------
    print("\n🔹 9. STRING FORMATTING")

    name = "Alice"
    age = 30
    # Old style
    s1 = "Name: %s, Age: %d" % (name, age)
    # .format() method
    s2 = "Name: {}, Age: {}".format(name, age)
    # f-string (Python 3.6+)
    s3 = f"Name: {name}, Age: {age}"

    print("Old style (%):", s1)
    print(".format():", s2)
    print("f-string:", s3)

    # Time Complexity:
    # - All formatting methods: O(n) where n is length of result.
    # Space Complexity: O(n) for the formatted string.

    # ----------------------------
    # 10. Summary of Complexity
    # ----------------------------
    print("\n" + "="*60)
    print("SUMMARY OF TIME & SPACE COMPLEXITY")
    print("="*60)
    print("""
Operation                     Time Complexity    Space Complexity
----------------------------------------------------------------
Access s[i]                   O(1)              O(1)
Slice s[a:b]                  O(k)              O(k)
Concatenation s1 + s2          O(n + m)          O(n + m)
join([s1, s2, ...])           O(n)              O(n)
len(s)                        O(1)              O(1)
upper(), lower()               O(n)              O(n)
strip()                       O(n)              O(n)
replace()                     O(n)              O(n)
split()                       O(n)              O(n)
find(), index()               O(n)              O(1)
count()                       O(n)              O(1)
'in' operator                 O(n)              O(1)
startswith(), endswith()      O(k)              O(1)
Comparison (==, <, >)         O(min(n, m))      O(1)
Iteration                     O(n)              O(1)

Where:
- n, m = lengths of strings
- k = length of substring/slice
""")

