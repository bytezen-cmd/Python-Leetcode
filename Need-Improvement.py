from typing import List

def buddy_strings(s: str, goal: str) -> bool:
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if (s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]) == goal:
                return True
    return False

def add_spaces(s: str, spaces: List[int]) -> str:
    for y in range(len(spaces)):
        spaces[y] += y
    for x in range(len(spaces)):
        s = s[:spaces[x]] + " " + s[spaces[x]:]
    return s
