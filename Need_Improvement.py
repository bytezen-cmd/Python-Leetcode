from typing import List
from xml.etree.ElementTree import VERSION


def hamming(n):
    o = []
    for i in range(n // 2 + 1):
        for j in range(n // 3 + 1):
            for k in range(n // 5 + 1):
                o.append(2 ** i * 3 ** j * 5 ** k)
    return sorted(o)[n-1]

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
