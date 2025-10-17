# Python Coding Solutions

A collection of Python solutions for popular coding challenge platforms including LeetCode and Codewars.

## Project Structure

```
.
├── Leetcode-Solution.py    # LeetCode problem solutions
├── Codewars-Solution.py    # Codewars challenge solutions
└── Tests.py                # Test cases and experiments
```

## Features

### Data Structures
- **ListNode**: Singly linked list implementation
- **TreeNode**: Binary tree implementation

### LeetCode Solutions

The repository includes solutions to various LeetCode problems across different difficulty levels:

#### Easy Problems
- Two Sum
- Palindrome Number
- Roman to Integer
- Longest Common Prefix
- Valid Parentheses
- Merge Two Sorted Lists
- Remove Duplicates from Sorted Array
- Remove Element
- Find the Index of the First Occurrence in a String
- Search Insert Position
- Length of Last Word
- Plus One
- Add Binary
- Square Root
- Climbing Stairs
- Remove Duplicates from Sorted List
- Merge Sorted Array
- Same Tree
- Binary Tree Inorder Traversal
- Count Segments
- Find GCD of Array
- Find Middle Index
- Find Peaks in Array

#### String Problems
- Goal Parser Interpretation
- Count Segments

### Codewars Solutions
- **Likes Function**: Formats social media likes (e.g., "Alex likes this", "Alex and 2 others like this")

## Usage

### Running Solutions

```python
from Leetcode-Solution import Solution

# Example: Two Sum
sol = Solution()
result = sol.two_sum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]

# Example: Valid Parentheses
result = sol.is_valid("()")
print(result)  # Output: True
```

### Data Structure Usage

```python
from Leetcode-Solution import ListNode, TreeNode

# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

## Requirements

- Python 3.13+
- typing module (standard library)

## Setup

1. Clone the repository
2. Ensure Python 3.13 or higher is installed
3. No additional dependencies required

## Development Environment

This project uses:
- PyCharm IDE (configuration files in `.idea/`)
- Python 3.13
- Git version control

## Key Algorithms Implemented

- **Two Pointers**: Remove duplicates, merge sorted arrays
- **Stack**: Valid parentheses
- **Hash Map**: Two sum problem
- **Binary Search**: Search insert position
- **Dynamic Programming**: Climbing stairs with memoization
- **Tree Traversal**: Inorder traversal, tree comparison
- **String Manipulation**: Roman numerals, binary addition

## Contributing

Feel free to add more solutions or optimize existing ones. When adding new solutions:
1. Follow the existing code structure
2. Use type hints
3. Add descriptive method names
4. Include docstrings for complex solutions

## License

This project is open source and available for educational purposes.

## Notes

- Solutions prioritize clarity and correctness
- Some solutions use memoization for optimization
- Test cases can be found in `Tests.py`