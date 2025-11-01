# Python Coding Solutions

A comprehensive collection of Python solutions for popular competitive programming platforms including LeetCode, Codewars, and Codeforces.

## Project Structure

```
.
├── Leetcode-Solution.py     # LeetCode problem solutions
├── Codewars-Solution.py     # Codewars challenge solutions
├── Codeforces-Solution.py   # Codeforces problem solutions
├── Tests.py                 # Test cases and experiments
└── LICENSE.txt              # MIT License
```

## Features

### Data Structures

**Custom Implementations:**
- `ListNode`: Singly linked list node
- `TreeNode`: Binary tree node
- `MyQueue`: Queue implementation using lists
- `Stack`: Custom stack implementation (in `dir_reduction`)

### Platform Solutions

#### LeetCode Solutions (70+ Problems)

**Array & String Problems:**
- Two Sum (#1)
- Roman to Integer (#13)
- Longest Common Prefix (#14)
- Valid Parentheses (#20)
- Remove Duplicates from Sorted Array (#26)
- Remove Element (#27)
- Search Insert Position (#35)
- Length of Last Word (#58)
- Plus One (#66)
- Add Binary (#67)
- Climbing Stairs (#70)
- Merge Sorted Array (#88)
- Majority Element (#169)
- Contains Duplicate (#217)
- Summary Ranges (#228)
- Third Maximum Number (#414)
- Find the Difference (#389)
- Number of Segments in a String (#434)
- Hamming Weight (#191)
- Reverse Bits (#190)
- Count Segments (#434)
- Reverse Vowels (#345)
- Intersection of Two Arrays (#349, #350)

**Linked List Problems:**
- Merge Two Sorted Lists (#21)
- Remove Duplicates from Sorted List (#83)
- Palindrome Linked List (#234)

**Tree Problems:**
- Same Tree (#100)
- Binary Tree Inorder Traversal (#94)
- Sum of Left Leaves (#404)
- Count Complete Tree Nodes (#222)

**Math & Bit Manipulation:**
- Palindrome Number (#9)
- Square Root (#69)
- Power of Two (#231)
- Power of Four (#342)
- Counting Bits (#338)
- Happy Number (#202)
- Find GCD of Array (#1979)

**Other Problems:**
- FizzBuzz (#412)
- Ransom Note (#383)
- Goal Parser Interpretation (#1678)
- Find Middle Index (#1991)
- Find Peaks in Array (#2951)
- Number of Pairs of Strings (#2023)

#### Codewars Solutions

**Array Manipulation:**
- `comp()`: Check if arrays are compositions (squares)
- `array_diff()`: Remove all occurrences of elements
- `find_uniq()`: Find unique element in array
- `find_even_index()`: Find equilibrium index

**String Problems:**
- `solution()`: Split string into pairs
- `likes()`: Format social media likes display
- `is_isogram()`: Check if string has repeating characters
- `create_phone_number()`: Format phone number

**Mathematical:**
- `digital_root()`: Calculate digital root
- `circle_diameter()`: Calculate circle diameter from polygon

**Algorithm Challenges:**
- `dir_reduction()`: Reduce opposite directions using stack

#### Codeforces Solutions

- **Nearly Lucky Number**: Check if count of lucky digits is lucky
- **Translation**: Check if strings are reverses of each other
- **Is Lucky**: Helper function to check lucky numbers

## Usage Examples

### LeetCode Solutions

```python
from Leetcode_Solution import Solution

# Two Sum Problem
sol = Solution()
result = sol.two_sum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]

# Valid Parentheses
is_valid = sol.is_valid("()[]{}")
print(is_valid)  # Output: True

# Climbing Stairs (with memoization)
steps = sol.climb_stairs(10)
print(steps)  # Output: 89
```

### Codewars Solutions

```python
from Codewars_Solution import Solution

# Likes formatting
print(Solution.likes([]))  
# Output: "no one likes this"

print(Solution.likes(["Peter"]))  
# Output: "Peter likes this"

print(Solution.likes(["Jacob", "Alex"]))  
# Output: "Jacob and Alex like this"

print(Solution.likes(["Max", "John", "Mark", "Ann"]))  
# Output: "Max, John and 2 others like this"

# Digital Root
print(Solution.digital_root(942))  
# Output: 6 (9+4+2=15, 1+5=6)

# Direction Reduction
print(Solution.dir_reduction(["NORTH", "SOUTH", "EAST", "WEST"]))
# Output: ["EAST", "WEST"]
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

## Requirements

- Python 3.13+
- `typing` module (standard library)
- `math` module (standard library)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python
   ```

2. Ensure Python 3.13 or higher is installed:
   ```bash
   python --version
   ```

3. Run any solution file:
   ```bash
   python Leetcode_Solution.py
   python Codewars_Solution.py
   python Codeforces_Solution.py
   ```

## Development Environment

**IDE Configuration:**
- PyCharm IDE (configuration in `.idea/`)
- Python 3.13 interpreter
- Black formatter configured
- Git version control

**Project Settings:**
- Virtual environment: `.venv/`
- Type hints enabled
- Static type checking recommended

## Key Algorithms & Techniques

### Algorithm Patterns
- **Two Pointers**: Array manipulation, string reversal
- **Stack**: Parentheses validation, direction reduction
- **Hash Map/Set**: Two sum, duplicate detection, intersection
- **Binary Search**: Search insert position
- **Dynamic Programming**: Climbing stairs with memoization
- **Recursion**: Tree traversal, mathematical calculations
- **Greedy**: Direction reduction, array processing

### Optimization Techniques
- Memoization/caching (climbing stairs)
- In-place array modification
- Early termination conditions
- Set operations for O(1) lookups

## Code Style

- Type hints for function parameters and return values
- Static methods where appropriate
- Descriptive variable names
- Minimal comments (self-documenting code)
- Consistent formatting

## Testing

Basic tests are available in `Tests.py` for experimentation and verification:

```python
python Tests.py
```

## Contributing

Contributions are welcome! When adding solutions:

1. Follow existing code structure and naming conventions
2. Use type hints for all function signatures
3. Keep solutions in their respective platform files
4. Add static methods where state isn't needed
5. Include docstrings for complex algorithms
6. Test your solution before committing

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

**Copyright © 2025 Himansh Mewada**

## Acknowledgments

- Solutions are inspired by problems from:
  - [LeetCode](https://leetcode.com/)
  - [Codewars](https://www.codewars.com/)
  - [Codeforces](https://codeforces.com/)

## Contact

Feel free to reach out for questions, suggestions, or collaboration opportunities!

---

**Note**: This repository is intended for educational purposes and personal skill development. Solutions may not always represent the most optimal approach but prioritize clarity and correctness.