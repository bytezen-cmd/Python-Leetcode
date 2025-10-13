from typing import List, Any, Optional

# Data Structures
class ListNode:
     def __init__(self, val=0, next_=None):
         self.val = val
         self.next = next_

# Problem Solutions
class Solution:
    def __init__(self):
        self.stack = []
        self.cache_stairs = [0, 1, 2, 3]

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

    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

    @staticmethod
    def str_str(haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    @staticmethod
    def length_of_last_word(s: str) -> int:
        s = s.strip()
        m = s.split()
        return len(m[-1])

    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        a = ""
        for x in digits:
            a += str(x)
        b = int(a) + 1
        c = []
        for l in str(b):
            c.append(int(l))
        return c

    @staticmethod
    def add_binary(a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        return bin(a + b)[2:]

    @staticmethod
    def my_sqrt(x: int) -> int:
        r = 1
        while True:
            if r * r < x:
                r += 1
            elif r * r == x:
                return r
            else:
                return r - 1

    @staticmethod
    def find_gcd(nums: List[int]) -> int:
        small = max(nums)
        large = 0
        for n in nums:
            if n < small:
                small = n
            if n > large:
                large = n

        remainder = 1
        while remainder != 0:
            remainder = large % small
            if remainder != 0:
                large = small
                small = remainder
        return small


    def climb_stairs(self, n: int) -> int:
        if n < len(self.cache_stairs):
            return self.cache_stairs[n]
        else:
            self.cache_stairs.append(self.climb_stairs(n - 1) + self.climb_stairs(n - 2))
        return self.cache_stairs[n]

    @staticmethod
    def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        vals = sorted(list(set(vals)))
        z = ListNode()
        r = z
        for x in vals:
            z.next = ListNode(val=x)
            z = z.next
        return r.next

    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int]) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = sorted(nums1[:m] + nums2)
        for x in range(len(nums1)):
            nums1[x] = a[x]