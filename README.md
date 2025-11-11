# Python Coding Solutions

A comprehensive collection of Python solutions for competitive programming platforms including LeetCode, Codewars, Codeforces, and HackerRank.

## Project Structure

```
.
├── Leetcode_Solution.py      # 70+ LeetCode problem solutions
├── Codewars_Solution.py      # Codewars challenge solutions
├── Codeforces_Solution.py    # Codeforces problem solutions
├── Hackerrank_Solution.py    # HackerRank problem solutions
├── Need_Improvement.py       # Problems requiring refinement
├── Tests.py                  # Test cases and experiments
├── LICENSE.txt               # MIT License
└── README.md                 # This file
```

## Features

### Custom Data Structures

**ListNode**: Singly linked list node implementation for linked list problems

**TreeNode**: Binary tree node for tree traversal and manipulation problems

**MyQueue**: Custom queue implementation using lists with push, pop, peek, and empty operations

**Stack**: Custom stack implementation used in direction reduction and validation problems

## Platform Solutions Overview

### LeetCode Solutions (70+ Problems)

**Array & String (23 problems)**
- Two Sum, Remove Duplicates, Remove Element
- Search Insert Position, Plus One, Add Binary
- Length of Last Word, Majority Element, Contains Duplicate
- Find the Difference, Intersection of Two Arrays, Reverse Vowels
- And more...

**Linked List (3 problems)**
- Merge Two Sorted Lists
- Palindrome Linked List
- Remove Duplicates from Sorted List

**Tree Problems (4 problems)**
- Same Tree, Binary Tree Inorder Traversal
- Sum of Left Leaves, Count Complete Tree Nodes

**Math & Bit Manipulation (11 problems)**
- Palindrome Number, Square Root, Power of Two
- Power of Four, Counting Bits, Happy Number
- Hamming Weight, Reverse Bits, and more

**Other Problems (29+ problems)**
- Valid Parentheses, FizzBuzz, Climbing Stairs
- Roman to Integer, Longest Common Prefix
- And numerous other challenges

### Codewars Solutions

**Array Manipulation**: `comp()`, `array_diff()`, `find_uniq()`, `find_even_index()`

**String Problems**: `likes()`, `is_isogram()`, `create_phone_number()`, `generate_hashtag()`

**Mathematical**: `digital_root()`, `circle_diameter()`, `expanded_form()`

**Advanced Algorithms**: `dir_reduction()`, `rot13()`, `order()`, and more

### Codeforces Solutions

- **Nearly Lucky Number**: Determines if digit count is lucky
- **Translation**: Checks if strings are reverses of each other
- **Helper Functions**: `is_lucky()` for validation

### HackerRank Solutions

- **Time Conversion**: Converts 12-hour to 24-hour time format

## Usage Examples

### LeetCode Usage

```python
from Leetcode_Solution import LeetcodeSolution

sol = LeetcodeSolution()

# Two Sum Problem
result = sol.two_sum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]

# Valid Parentheses
is_valid = sol.is_valid("()[]{}")
print(is_valid)  # Output: True

# Climbing Stairs (with memoization)
steps = sol.climb_stairs(10)
print(steps)  # Output: 89

# FizzBuzz
fizzbuzz = sol.fizz_buzz(15)
print(fizzbuzz)  # Output: ['1', '2', 'Fizz', '4', 'Buzz', ...]
```

### Codewars Usage

```python
from Codewars_Solution import CodewarsSolution

# Likes formatting
print(CodewarsSolution.likes([]))  
# Output: "no one likes this"

print(CodewarsSolution.likes(["Peter", "Julia"]))  
# Output: "Peter and Julia like this"

# Digital Root
print(CodewarsSolution.digital_root(942))  
# Output: 6 (9+4+2=15, 1+5=6)

# Direction Reduction
print(CodewarsSolution.dir_reduction(["NORTH", "SOUTH", "EAST", "WEST"]))
# Output: []

# ROT13 Cipher
print(CodewarsSolution.rot13("Test"))
# Output: "Grfg"
```

### Codeforces Usage

```python
from Codeforces_Solution import CodeforcesSolution

# Nearly Lucky Number
CodeforcesSolution.nearly_lucky()  # Input: 4474
# Output: YES

# Translation
CodeforcesSolution.translation()  # Input: abc, cba
# Output: YES
```

### Data Structure Usage

```python
from Leetcode_Solution import ListNode, TreeNode, MyQueue

# Linked List
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Binary Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Queue
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.pop())  # Output: 1
```

## Problem Categories

### Easy Level
- Palindrome Number
- Two Sum
- FizzBuzz
- Valid Parentheses
- Climbing Stairs

### Medium Level
- Longest Common Prefix
- Roman to Integer
- Binary Tree Inorder Traversal
- Digital Root
- Direction Reduction

### Hard Level
- Tree comparison and traversal
- Complex string manipulation
- Stack-based algorithms

## Key Algorithms & Techniques

**Two Pointers**: Array manipulation, string reversal, palindrome checking

**Stack**: Parentheses validation, direction reduction, symbol matching

**Hash Map/Set**: Two sum problems, duplicate detection, intersection finding

**Binary Search**: Search insert position, finding targets in sorted arrays

**Dynamic Programming**: Climbing stairs with memoization, Fibonacci optimization

**Recursion**: Tree traversal, mathematical calculations, permutations

**Greedy Algorithms**: Direction reduction, array processing

## Requirements

- Python 3.13+
- `typing` module (standard library)
- `math` module (standard library)

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python
   ```

2. Verify Python version:
   ```bash
   python --version  # Should be 3.13 or higher
   ```

3. Run solution files:
   ```bash
   python Leetcode_Solution.py
   python Codewars_Solution.py
   python Codeforces_Solution.py
   python Hackerrank_Solution.py
   ```

## Development Environment

**IDE**: PyCharm with Black formatter

**Python Interpreter**: Python 3.13

**Virtual Environment**: `.venv/` (configured)

**Version Control**: Git

**Code Quality**: Type hints enabled, static type checking recommended

## Code Style Guidelines

- Type hints for all function parameters and return values
- Static methods where appropriate (no instance state needed)
- Descriptive variable names for clarity
- Minimal comments with self-documenting code
- Consistent formatting and organization

## Testing

Experimental tests and function verification available in `Tests.py`:

```python
python Tests.py
```

## Performance Notes

**Optimizations Implemented:**
- Memoization for recursive problems (Fibonacci, climbing stairs)
- In-place array modifications where possible
- Early termination conditions
- Set operations for O(1) lookups
- Hash maps for efficient searching

**Time Complexities:** Solutions prioritize correctness and clarity over extreme optimization, but include standard algorithmic improvements.

## Problems Requiring Improvement

Some solutions in `Need_Improvement.py` include:

- **Hamming Numbers**: Inefficient triple-nested loop approach
- **Buddy Strings**: Brute force checking method
- **Add Spaces**: Initial suboptimal implementation with corrected version provided

## Contributing

When adding new solutions:

1. Follow existing code structure and naming conventions
2. Include type hints for all function signatures
3. Keep solutions in appropriate platform files
4. Use static methods when instance state isn't needed
5. Test thoroughly before committing
6. Add docstrings for complex algorithms

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

**Copyright © 2025 Himansh Mewada**

## Acknowledgments

Solutions are inspired by and derived from problems on:
- [LeetCode](https://leetcode.com/)
- [Codewars](https://www.codewars.com/)
- [Codeforces](https://codeforces.com/)
- [HackerRank](https://www.hackerrank.com/)

## Disclaimer

This repository is intended for educational purposes and personal skill development. Solutions prioritize clarity and correctness over absolute optimization. Different approaches may be equally valid depending on specific requirements and constraints.