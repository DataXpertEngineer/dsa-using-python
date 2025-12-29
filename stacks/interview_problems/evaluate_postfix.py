"""
Evaluate Postfix Expression

Evaluate a postfix (Reverse Polish Notation) expression using stack.

Problem Statement:
-------------------
Given a postfix expression, evaluate it and return the result.

Postfix: Operator comes after operands (e.g., "3 4 +" = 3 + 4 = 7)

Example:
    Input: "3 4 + 2 *"
    Output: 14
    Explanation: (3 + 4) * 2 = 14

Why Stack?
----------
- Process operands before operators
- Stack stores operands until operator is found
- Natural LIFO order for evaluation

Useful in:
- Expression evaluation
- Calculator implementations
- Compiler design
- Medium difficulty interview problems
"""

from typing import List, Union


# ----------------------------------------------------------------------
# Evaluate Postfix (Language-agnostic)
# ----------------------------------------------------------------------
def evaluate_postfix(expression: str) -> Union[int, float]:
    """
    Evaluate postfix expression using stack.

    Algorithm:
    1. Scan expression left to right
    2. If operand, push to stack
    3. If operator, pop two operands, apply operator, push result
    4. Final result is on stack

    Args:
        expression (str): Postfix expression (space-separated tokens)

    Returns:
        Union[int, float]: Result of evaluation

    Complexity:
        Time: O(n)     - Single pass through expression, each token processed once.
        Space: O(n)   - Stack storage for operands.
    """
    stack: List[Union[int, float]] = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # Operand
            stack.append(int(token))
        else:
            # Operator
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            elif token == '^':
                result = a ** b
            else:
                raise ValueError(f"Unknown operator: {token}")
            
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack[0]


# ----------------------------------------------------------------------
# Evaluate Postfix (Single Character, No Spaces)
# ----------------------------------------------------------------------
def evaluate_postfix_compact(expression: str) -> Union[int, float]:
    """
    Evaluate postfix expression without spaces (single digits only).

    Args:
        expression (str): Postfix expression without spaces

    Returns:
        Union[int, float]: Result of evaluation

    Complexity:
        Time: O(n)     - Single pass through expression.
        Space: O(n)   - Stack storage.
    """
    stack: List[Union[int, float]] = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                result = a + b
            elif char == '-':
                result = a - b
            elif char == '*':
                result = a * b
            elif char == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            elif char == '^':
                result = a ** b
            else:
                raise ValueError(f"Unknown operator: {char}")
            
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack[0]


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Evaluate Postfix Expression Demonstration")
    
    # Test cases with spaces
    test_cases = [
        "3 4 +",
        "3 4 + 2 *",
        "5 1 2 + 4 * + 3 -",
        "10 2 /",
        "2 3 ^",
        "15 7 1 1 + - / 3 * 2 1 1 + + -"
    ]
    
    print("Postfix Evaluation (with spaces):")
    for expr in test_cases:
        try:
            result = evaluate_postfix(expr)
            print(f"  {expr:30} = {result}")
        except Exception as e:
            print(f"  {expr:30} = Error: {e}")
    
    # Test cases without spaces (single digits)
    print("\nPostfix Evaluation (compact, no spaces, single digits):")
    compact_tests = [
        "34+",
        "34+2*",
        "512+4*+3-",
        "102/",
        "23^"
    ]
    
    for expr in compact_tests:
        try:
            result = evaluate_postfix_compact(expr)
            print(f"  {expr:20} = {result}")
        except Exception as e:
            print(f"  {expr:20} = Error: {e}")

