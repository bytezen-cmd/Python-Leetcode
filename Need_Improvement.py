from typing import List
from xml.etree.ElementTree import VERSION


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
    # CORRECTED VERSION
    #
    # def addSpaces(self, s: str, spaces: List[int]) -> str:
    #     output = []
    #     prev = 0
    #     for x in spaces:
    #         output.append(s[prev:x])
    #         prev = x
    #     output.append(s[prev:])
    #     return " ".join(output)
