# Arrays in Python (Data Structures & Algorithms)

This folder focuses on **arrays** as a fundamental data structure and how they are represented using **Python lists**.

You’ll learn:

- The **DSA concept** of arrays (independent of any language)
- Static vs dynamic arrays
- How arrays are **implemented in Python**
- What a **dynamic array** is (size vs capacity, resizing, growth)
- How Python’s **list** behaves in terms of memory, performance, and operations

---

## A. Arrays (DSA Concept)

### 1. What is an Array?

An **array** is a collection of elements:

- Stored in **contiguous memory locations**
- Usually all of the **same type** in low-level languages
- Accessed by **zero-based index** (0, 1, 2, ...)

Think of an array as a row of lockers:

- Each locker has a fixed position (index)
- You can jump directly to locker 5 without opening 0–4
- This **direct jump** is called **random access** and runs in **O(1)** time

Mathematically, if:

- `base_address` = starting address of the array
- `i` = index
- `size_of_element` = bytes per element

Then:

```text
address_of(arr[i]) = base_address + i * size_of_element
````

That formula is why `arr[i]` is constant time.

---

### 2. Static vs Dynamic Arrays

#### Static Array

* Size is **fixed** when created
* Cannot grow or shrink
* Common in C/C++:

  ```c
  int a[5];  // static array of size 5
  ```

**Pros:**

* No resizing overhead
* Simple, predictable memory layout

**Cons:**

* Must know the size in advance
* Easy to waste memory or run out of space

#### Dynamic Array

* Can **grow** (and sometimes shrink) at runtime
* Internally:

  * Keeps a **capacity** (allocated slots) and a **size** (used slots)
  * When size reaches capacity, allocates a **larger block**, copies elements, frees old block

Examples:

* C++ `std::vector`
* Java `ArrayList`
* Python `list`

Dynamic arrays **trade performance spikes for flexibility**:

* You don’t need to know size upfront
* Occasionally pay a higher cost when resizing

---

### 3. Random Access

Arrays support **random access**:

* You can access `arr[i]` directly if you know `i`
* No traversal needed
* Time complexity: **O(1)**

Not all data structures support this.
For example, **linked lists** require walking node by node to reach index `i` → **O(n)**.

---

### 4. Strengths & Weaknesses of Arrays

#### Strengths

* **Fast random access** (`arr[i]` is O(1))
* **Cache-friendly** due to contiguous memory
* Simple and widely supported
* Great for:

  * Index-based lookups
  * Fixed-size collections
  * Building other structures (heaps, dynamic arrays, etc.)

#### Weaknesses

* **Insertion/deletion in the middle** is expensive:

  * Need to shift elements to keep them contiguous ⇒ **O(n)**
* **Static arrays** cannot change size
* **Dynamic arrays** still pay cost during resizes (allocate + copy)

---

### 5. Time & Space Complexity Summary (Conceptual Arrays)

| Operation                     | Time Complexity | Space Complexity |
| ----------------------------- | --------------- | ---------------- |
| Access by index (`arr[i]`)    | O(1)            | O(1)             |
| Update by index (`arr[i]=x`)  | O(1)            | O(1)             |
| Append at end (dynamic array) | O(1) amortized  | O(1)             |
| Insert at index               | O(n)            | O(1)             |
| Delete at index               | O(n)            | O(1)             |
| Search (linear scan)          | O(n)            | O(1)             |
| Traverse all elements         | O(n)            | O(1)             |

> **Amortized O(1)**: some operations are occasionally expensive, but the **average per operation** across many operations is constant.

---

## B. How Arrays Are Implemented in Python

In Python, the built-in **`list`** type is implemented as a **dynamic array**.

Understanding this helps you:

* Predict which operations are cheap or expensive
* Avoid slow patterns (e.g., repeated inserts at index 0)
* Write more efficient DSA solutions in Python

---

### 1. Python `list` = Dynamic Array of Pointers

Conceptually, a Python list is:

> A **contiguous array of pointers** to Python objects (`PyObject*`).

Key points:

* The list stores **references**, not raw values.
* The actual objects (ints, strings, etc.) live separately on the heap.
* Because it stores pointers, a list can hold:

  * Different types: `[1, "a", 3.14]`
  * Large objects
  * The same object multiple times

Example:

```python
a = [10, 20, 30]
```

Internally:

```text
+---------+---------+---------+
|  ptr1   |  ptr2   |  ptr3   |   <- contiguous array of pointers
+---------+---------+---------+

ptr1 -> PyObject for 10
ptr2 -> PyObject for 20
ptr3 -> PyObject for 30
```

So `a[i]` is:

1. Compute address of pointer at index `i` (O(1))
2. Follow pointer to the object in memory

---

### 2. Dynamic Array in Python: Size vs Capacity

Python lists conceptually track:

* **Size** → number of elements in the list: `len(a)`
* **Capacity** → how many elements fit in the **currently allocated** block

Example:

```python
a = []
# size = 0, capacity = small (implementation detail)

a.append(1)
# size = 1, capacity might be 4

a.append(2)
# size = 2, capacity still 4
```

* As long as `size < capacity`, appends just fill free slots.
* When `size == capacity`, a resize is needed:

  1. Allocate a larger block
  2. Copy all pointers
  3. Add the new element
  4. Release the old block

---

### 3. Overallocation & Growth (Why `append()` is Amortized O(1))

Resizing on every append would be too slow, so Python uses **overallocation**:

* When the internal array is full, it grows to a size **larger than needed**.
* Future appends can use this extra capacity without another resize.

Roughly:

```text
new_capacity ≈ old_capacity * growth_factor + constant
```

where growth_factor > 1.

Because of this:

* Resizes (O(n) copies) are **infrequent**.
* Most `append()` calls are just a simple write into the next free slot.

Over many appends, the **total cost** of all resizes is proportional to the number of appends, so:

> Average (amortized) cost of `append()` is **O(1)**.

---

### 4. Why Insertion/Deletion in the Middle is O(n)

Consider:

```python
a = [10, 20, 30, 40]
a.insert(1, 99)
```

Even ignoring resizing:

* To insert at index 1, elements at indices 1–3 (`20, 30, 40`) must be shifted **right** by one position.
* That’s up to **O(n)** element moves.

Similarly, for deletion:

```python
a.pop(1)
```

* Elements after index 1 must be shifted **left** to fill the gap.

So:

* `insert(i, x)`, `pop(i)` or `remove(x)` are **O(n)** due to shifting.
* `pop()` at the **end** is O(1) because no shifting is required.

---

### 5. Contiguous Memory & Cache Behavior

Even though list elements are pointers, those **pointers themselves** are stored in **contiguous memory**.

Benefits:

* Indexing `a[i]` is fast: compute address of pointer `i` and dereference.
* Iteration (e.g., `for x in a:`) walks through contiguous memory, which is **cache-friendly**.

This is why Python lists are still quite performant for random access and traversal, despite their extra level of indirection.

---

### 6. Difference from Static Arrays in C/C++

#### Static Arrays in C/C++

```c
int a[4] = {10, 20, 30, 40};
```

* Stores **raw integers** directly in contiguous memory.
* All elements same size (e.g., 4 bytes).
* No pointer indirection.
* Size fixed at compile time.

#### Python Lists

```python
a = [10, 20, 30, 40]
```

* Stores **pointers** to objects, not raw integers.
* Each integer object lives separately on the heap.
* Elements can be heterogeneous:

  ```python
  a = [10, "hello", 3.14]
  ```

**Trade-offs:**

* Static arrays (C/C++) → memory-efficient, very fast, but inflexible.
* Python lists → flexible, easy to use, but more memory and one extra pointer access.

---

### 7. When Python List Operations Become Expensive

Python lists are efficient when you:

* Append at the end (`append`, `extend`) most of the time
* Access by index (`a[i]`)
* Iterate over the whole list

They become expensive when you repeatedly:

* Insert at the **front**: `a.insert(0, x)`
* Delete from the **front**: `a.pop(0)` or `del a[0]`
* Insert/delete in the **middle** many times
* Rebuild lists in loops like:

  ```python
  b = []
  for x in data:
      b = b + [x]   # creates a new list every time → O(n²)
  ```

For front-heavy or queue-like patterns, **`collections.deque`** is a better fit.

---

### 8. Why Python Lists Store Pointers (PyObject*)

Python lists use pointers because:

1. **Dynamic typing**

   * Python variables are not bound to a fixed type.
   * Lists must be able to store any Python object.

2. **Heterogeneous elements**

   * A single list can mix types:

     ```python
     a = [1, "two", 3.0, [4, 5]]
     ```

3. **Object model**

   * In CPython, everything is a `PyObject*`.
   * Reference counting and garbage collection work with object pointers.

4. **Sharing objects**

   * Multiple lists can reference the **same object**:

     ```python
     x = [1, 2, 3]
     a = [x, x]
     ```

   * No copies are made; both entries point to the same list.

This design makes lists **flexible and powerful**, at the cost of:

* Higher memory usage than raw arrays
* An extra pointer dereference on access

---

### 9. Python List Operations – Cheat Sheet

These complexities match what you’ll see in `arrays.py`:

| Operation                         | Time Complexity | Space Complexity |
| --------------------------------- | --------------- | ---------------- |
| Access `arr[i]`                   | O(1)            | O(1)             |
| Update `arr[i] = x`               | O(1)            | O(1)             |
| `arr.append(x)`                   | O(1) amortized  | O(1)             |
| `arr.insert(i, x)`                | O(n)            | O(1)             |
| `arr.pop()` (end)                 | O(1)            | O(1)             |
| `arr.pop(i)` / `arr.remove(x)`    | O(n)            | O(1)             |
| Membership `x in arr` / `index()` | O(n)            | O(1)             |
| Traverse `for x in arr`           | O(n)            | O(1)             |
| `len(arr)`                        | O(1)            | O(1)             |
| Copy `arr.copy()`                 | O(n)            | O(n)             |
| Slice `arr[a:b]`                  | O(k)            | O(k)             |
| In-place reverse `arr.reverse()`  | O(n)            | O(1)             |
| Reverse copy `arr[::-1]`          | O(n)            | O(n)             |

---

## Summary

* Arrays (as a DSA concept) provide **contiguous memory** and **O(1) random access**.
* Python’s `list` is a **dynamic array of pointers**:

  * Fast for **indexing**, **iteration**, and **append** (amortized O(1))
  * Expensive for frequent **middle/front insertions and deletions** (O(n))
* Understanding:

  * **Static vs dynamic arrays**
  * **Size vs capacity**
  * **Resizing & overallocation**
  * **Pointer-based storage**

will help you:

* Reason about complexity
* Avoid slow patterns
* Write efficient solutions in Python for DSA and interview problems

Now you can explore `arrays.py` to see these ideas in action, and then build on top of them with array-based techniques and interview problems.
