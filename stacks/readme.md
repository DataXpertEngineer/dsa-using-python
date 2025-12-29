# Stacks

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. Elements are added and removed from the same end (top).

## 📁 Folder Structure

```
stacks/
├── stacks.py                            # Core stack implementation & operations ⭐ MOST IMPORTANT
├── implementations/                     # Stack implementation techniques
│   ├── array_stack.py                   # Stack using array/list
│   └── linked_list_stack.py             # Stack using linked list
├── applications/                        # Common stack applications
│   ├── parentheses_checker.py           # Balanced parentheses problem ⭐ MOST IMPORTANT
│   ├── infix_to_postfix.py              # Infix → Postfix conversion ⭐ MOST IMPORTANT
│   ├── next_greater_element.py          # Next greater element problem ⭐ MOST IMPORTANT
│   └── stock_span.py                    # Stock span problem 🟡 MEDIUM
└── interview_problems/                  # Typical interview questions
    ├── min_stack.py                     # Stack that supports getMin() in O(1) ⭐ MOST IMPORTANT
    ├── largest_rectangle_histogram.py   # Histogram area using stack 🟡 MEDIUM
    └── evaluate_postfix.py              # Evaluate postfix expression 🟡 MEDIUM
```

## 📚 Core Concepts

### Stack Operations

- **push(item)**: Add element to top - O(1)
- **pop()**: Remove and return top element - O(1)
- **peek()**: View top element without removing - O(1)
- **is_empty()**: Check if stack is empty - O(1)
- **size()**: Get number of elements - O(1)

### Characteristics

- **LIFO (Last In First Out)**: Last element added is first removed
- **Dynamic size**: Grows/shrinks as needed
- **Single access point**: Only top element is accessible
- **Efficient operations**: All basic operations are O(1)

## 🏗️ Implementations

### 1. Array-based Stack (`implementations/array_stack.py`)
- Uses Python list (dynamic array)
- **Advantages**: Simple, cache-friendly, O(1) amortized operations
- **Disadvantages**: Resizing overhead (amortized)
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) for n elements

### 2. Linked List-based Stack (`implementations/linked_list_stack.py`)
- Uses linked list structure
- **Advantages**: True O(1) operations, no resizing, dynamic size
- **Disadvantages**: Extra memory for pointers, not cache-friendly
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n) for n elements

## 🎯 Applications

### 1. Balanced Parentheses (`applications/parentheses_checker.py`) ⭐
- Check if parentheses are balanced
- **Algorithm**: Use stack to match opening with closing
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

### 2. Infix to Postfix (`applications/infix_to_postfix.py`) ⭐
- Convert infix expression to postfix
- **Algorithm**: Use stack to handle operator precedence
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

### 3. Next Greater Element (`applications/next_greater_element.py`) ⭐
- Find next greater element for each array element
- **Algorithm**: Monotonic stack technique
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

### 4. Stock Span (`applications/stock_span.py`) 🟡
- Calculate stock span for each day
- **Algorithm**: Stack to find previous greater element
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

## 💼 Interview Problems

### Most Important (⭐)

1. **Min Stack** (`interview_problems/min_stack.py`)
   - Design stack with getMin() in O(1)
   - Two approaches: (value, min) pairs or auxiliary stack
   - **Time Complexity**: O(1) for all operations
   - **Space Complexity**: O(n)

### Medium Difficulty (🟡)

2. **Largest Rectangle in Histogram** (`interview_problems/largest_rectangle_histogram.py`)
   - Find largest rectangle area in histogram
   - Uses monotonic stack
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

3. **Evaluate Postfix** (`interview_problems/evaluate_postfix.py`)
   - Evaluate postfix expression
   - Stack-based evaluation
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

## 📊 Complexity Summary

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| push() | O(1) | O(1) |
| pop() | O(1) | O(1) |
| peek() | O(1) | O(1) |
| is_empty() | O(1) | O(1) |
| size() | O(1) | O(1) |
| Balanced Parentheses | O(n) | O(n) |
| Infix to Postfix | O(n) | O(n) |
| Next Greater Element | O(n) | O(n) |
| Stock Span | O(n) | O(n) |
| Min Stack (all ops) | O(1) | O(n) |
| Largest Rectangle | O(n) | O(n) |
| Evaluate Postfix | O(n) | O(n) |

## 🎓 Learning Path

1. **Start with**: `stacks.py` - Understand basic operations
2. **Learn implementations**: 
   - `array_stack.py` - Array-based implementation
   - `linked_list_stack.py` - Linked list-based implementation
3. **Practice applications**: 
   - `parentheses_checker.py` - Balanced parentheses
   - `infix_to_postfix.py` - Expression conversion
   - `next_greater_element.py` - Monotonic stack
4. **Solve interview problems**: Start with ⭐ marked problems
5. **Advanced topics**: Explore histogram and evaluation problems

## 💡 Key Insights

1. **LIFO Principle**: Last element added is first removed
2. **Stack for Matching**: Perfect for matching problems (parentheses, brackets)
3. **Monotonic Stack**: Maintains increasing/decreasing sequence for efficient queries
4. **Expression Evaluation**: Stack naturally handles operator precedence
5. **O(1) Operations**: All basic stack operations are constant time

## 🔗 Related Topics

- **Arrays**: Array-based stack implementation
- **Linked Lists**: Linked list-based stack implementation
- **Queues**: Another linear data structure (FIFO)
- **Trees**: Stack used in tree traversals
- **Graphs**: Stack used in DFS

## 📝 Notes

- All implementations include both language-agnostic and Python-specific approaches
- Complexity analysis provided for all functions
- Example usage included in each file
- Follows clean code principles with detailed docstrings

