"""
Infix to Postfix Conversion

Convert infix expression to postfix (Reverse Polish Notation) using stack.

Problem Statement:
-------------------
Convert an infix expression (e.g., "A + B * C") to postfix (e.g., "A B C * +").

Infix: Operator between operands (A + B)
Postfix: Operator after operands (A B +)

Why Stack?
----------
- Need to handle operator precedence
- Parentheses change evaluation order
- Stack maintains operators in correct order

Useful in:
- Expression evaluation
- Compiler design
- Calculator implementations
- Common interview problems
"""

from typing import List, Dict


# ----------------------------------------------------------------------
# Infix to Postfix Conversion (Language-agnostic)
# ----------------------------------------------------------------------
def infix_to_postfix(infix: str) -> str:
    """
    Convert infix expression to postfix using stack.

    Algorithm:
    1. Scan expression left to right
    2. If operand, add to output
    3. If '(', push to stack
    4. If ')', pop until '('
    5. If operator, pop higher precedence operators, then push
    6. Pop remaining operators

    Args:
        infix (str): Infix expression (space-separated tokens)

    Returns:
        str: Postfix expression

    Complexity:
        Time: O(n)     - Single pass through expression, each token processed once.
        Space: O(n)   - Stack and output storage.
    """
    precedence: Dict[str, int] = {
        '+': 1, '-': 1,
        '*': 2, '/': 2,
        '^': 3
    }
    
    stack: List[str] = []
    output: List[str] = []
    tokens = infix.split()
    
    for token in tokens:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)
    
    # Pop remaining operators
    while stack:
        output.append(stack.pop())
    
    return ' '.join(output)


# ----------------------------------------------------------------------
# Infix to Postfix (Single Character, No Spaces)
# ----------------------------------------------------------------------
def infix_to_postfix_compact(infix: str) -> str:
    """
    Convert infix to postfix for single-character operands (no spaces).

    Args:
        infix (str): Infix expression without spaces

    Returns:
        str: Postfix expression

    Complexity:
        Time: O(n)     - Single pass through expression.
        Space: O(n)   - Stack and output storage.
    """
    precedence: Dict[str, int] = {
        '+': 1, '-': 1,
        '*': 2, '/': 2,
        '^': 3
    }
    
    stack: List[str] = []
    output: List[str] = []
    
    for char in infix:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Infix to Postfix Conversion Demonstration")
    
    # Test cases with spaces
    test_cases = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A + B * C - D",
        "A ^ B ^ C",
        "( A + B ) * ( C - D )"
    ]
    
    print("Infix to Postfix (with spaces):")
    for infix in test_cases:
        postfix = infix_to_postfix(infix)
        print(f"  {infix:30} -> {postfix}")
    
    # Test cases without spaces
    print("\nInfix to Postfix (compact, no spaces):")
    compact_tests = [
        "A+B",
        "A+B*C",
        "(A+B)*C",
        "A+B*C-D",
        "A^B^C"
    ]
    
    for infix in compact_tests:
        postfix = infix_to_postfix_compact(infix)
        print(f"  {infix:20} -> {postfix}")

