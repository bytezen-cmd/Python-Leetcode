from typing import List, Any, Optional

# Data Structures
class ListNode:
     def __init__(self, val=0, next_=None):
         self.val = val
         self.next = next_

# Problem Solutions
class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> list[int | Any] | None:
        hashmap = {}
        for index, number in enumerate(nums):
            if (target - number) in hashmap:
                return [index, hashmap[target - number]]
            else:
                hashmap[number] = index
        return None

    @staticmethod
    def is_palindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]

    @staticmethod
    def roman_to_int(s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = 0

        for x in reversed(s):
            value = roman_dict[x]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total

    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        x = strs[0]
        for y in strs:
            if y < x:
                x = y

        for z in range(len(x), -1, -1):
            if all(x[:z] == s[:z] for s in strs):
                return x[:z]

        return ""

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def curr(self):
        return self.stack[-1]

    def is_valid(self, s: str) -> bool:

        for x in s:
            if x == "{" or x == "(" or x == "[":
                self.stack.append(x)
            elif x == "}" and not self.is_empty():
                if self.curr() == "{":
                    self.stack.pop()
                else:
                    return False
            elif x == "]" and not self.is_empty():
                if self.curr() == "[":
                    self.stack.pop()
                else:
                    return False
            elif x == ")" and not self.is_empty():
                if self.curr() == "(":
                    self.stack.pop()
                else:
                    return False
            else:
                return False
        if self.is_empty():
            return True
        else:
            return False

    @staticmethod
    def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val >= list2.val:
                tail.next = ListNode(list2.val)
                list2 = list2.next
                tail = tail.next
            else:
                tail.next = ListNode(list1.val)
                list1 = list1.next
                tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        a = sorted(list(set(nums)))
        for x in range(len(a)):
            nums[x] = a[x]
        return len(a)