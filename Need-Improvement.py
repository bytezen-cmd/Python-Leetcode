def buddy_strings(s: str, goal: str) -> bool:
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if (s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]) == goal:
                return True
    return False
