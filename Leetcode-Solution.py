from typing import List, Any, Optional
import math

# Data Structures
class ListNode:
     def __init__(self, val=0, next_=None):
         self.val = val
         self.next = next_
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> Any | None:
        if len(self.queue) != 0:
            return self.queue.pop(0)
        return None

    def peek(self) -> Any | None:
        if len(self.queue) != 0:
            return self.queue[0]
        return None
    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

# Problem Solutions
class LeetcodeSolution:

    def __init__(self):
        self.stack = []
        self.cache_stairs = [0, 1, 2, 3]
        self.traverse_inorder = []
        self.happy_sequence = []
        self.left_leaves_entry = []
        self.total_nodes = 0
        self.node_count = 0

    @staticmethod
    def insert_greatest_common_divisors(head: Optional[ListNode]) -> Optional[ListNode]:
        z = head
        while head and head.next:
            x = head.val
            y = head.next.val
            a = ListNode(val=math.gcd(x, y))
            a.next = head.next
            head.next = a
            head = head.next.next
        return z

    @staticmethod
    def weight(order, x):
        if x not in order:
            return float('inf')
        else:
            return order.index(x)

    @staticmethod
    def custom_sort_string(order: str, s: str) -> str:
        s = [char for char in s]
        s.sort(key=lambda x: LeetcodeSolution.weight(order, x))
        return "".join(s)

    @staticmethod
    def sort_array_by_parity(nums: List[int]) -> List[int]:
        even = []
        odd = []
        for entry in nums:
            if entry % 2 == 0:
                even.append(entry)
            else:
                odd.append(entry)
        return even + odd

    @staticmethod
    def is_monotonic(nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)

    @staticmethod
    def smaller_numbers_than_current(nums: List[int]) -> List[int]:
        n = []
        for x in range(len(nums)):
            count = 0
            for y in range(len(nums)):
                if nums[y] < nums[x]:
                    count += 1
            n.append(count)
        return n

    @staticmethod
    def unique_morse_representations(words: List[str]) -> int:
        memo = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
        }
        table = str.maketrans(memo)
        for x in range(len(words)):
            words[x] = words[x].translate(table)
        words = set(words)
        return len(words)

    @staticmethod
    def uncommon_from_sentences(s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        output = []
        for char in s1:
            if s1.count(char) == 1 and char not in s2:
                output.append(char)

        for char in s2:
            if s2.count(char) == 1 and char not in s1:
                output.append(char)
        return output

    @staticmethod
    def rotate_string(s: str, goal: str) -> bool:
        for _ in range(len(s)):
            if s == goal:
                return True
            else:
                s = s[1:] + s[0]
        return False

    @staticmethod
    def count_negatives(grid: List[List[int]]) -> int:
        count = 0
        for gri in grid:
            for gr in gri:
                if gr < 0:
                    count += 1
        return count

    @staticmethod
    def number_of_steps(num: int) -> int:
        step = 0
        while num:
            num = num // 2 if num % 2 == 0 else num - 1
            step += 1
        return step

    @staticmethod
    def maximum_69_number(num: int) -> int:
        num = str(num)
        if '6' in num:
            return int(num[:num.index('6')] + '9' + num[num.index('6') + 1:])
        else:
            return int(num)

    @staticmethod
    def get_no_zero_integers(n: int) -> list[int] | None:
        for x in range(n):
            if '0' not in str(x) and '0' not in str(n - x):
                return [x, n - x]
        return None

    @staticmethod
    def reorder_spaces(text: str) -> str:
        count = 0
        for x in text:
            if x == " ":
                count += 1
        if len(text.strip().split()) == 1:
            return "".join(text.strip().split()) + (" " * count)
        words = text.strip().split()
        initial = " " * (count // (len(words) - 1))
        extra = " " * (count % (len(words) - 1))
        return initial.join(words) + extra

    @staticmethod
    def sum_odd_length_subarrays(arr: List[int]) -> int:
        result = 0
        for y in range(1, len(arr) + 1, 2):
            for x in range(len(arr) - y + 1):
                result += sum(arr[x:x + y])
        return result

    @staticmethod
    def num_special(mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and all([mat[i][k] == 0 for k in range(len(mat[i])) if k != j]) and all(
                        [mat[l][j] == 0 for l in range(len(mat)) if l != i]):
                    count += 1
        return count

    @staticmethod
    def min_operations(nums: List[int]) -> int:
        count = 0
        index = 1
        if len(nums) == 1:
            return 0
        while index < len(nums):
            if nums[index] <= nums[index - 1]:
                count += nums[index - 1] - nums[index] + 1
                nums[index] += nums[index - 1] - nums[index] + 1
            index += 1
        return count

    @staticmethod
    def array_sign(nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        if product == 0:
            return 0
        elif product > 0:
            return 1
        else:
            return -1

    @staticmethod
    def truncate_sentence(s: str, k: int) -> str:
        array = s.split()
        return " ".join(array[:k])

    @staticmethod
    def percentage_letter(s: str, letter: str) -> int:
        count = 0
        for char in s:
            if char == letter:
                count += 1
        return (count * 100) // len(s)

    @staticmethod
    def square_is_white(coordinates: str) -> bool:
        column = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        return (column[coordinates[0]] % 2) != (int(coordinates[1]) % 2)

    @staticmethod
    def digit_count(num: str) -> bool:
        num = [int(char) for char in num]
        for x in range(len(num)):
            if num.count(x) != num[x]:
                return False
        return True

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if root:
            self.node_count += 1
            if root.left:
                self.count_nodes(root.left)
            if root.right:
                self.count_nodes(root.right)
        return self.node_count

    @staticmethod
    def check_zero_ones(s: str) -> bool:
        array1 = s.split("0")
        array0 = s.split("1")
        max0 = 0
        max1 = 0
        for arr in array0:
            if len(arr) > max0:
                max0 = len(arr)
        for arr in array1:
            if len(arr) > max1:
                max1 = len(arr)
        return max1 > max0


    @staticmethod
    def get_min_distance(nums: List[int], target: int, start: int) -> int:
        minimum = float("inf")
        for i in range(len(nums)):
            if nums[i] == target and abs(i - start) < minimum:
                minimum = abs(i - start)
        return minimum

    @staticmethod
    def sum_base(n: int, k: int) -> int:
        array = []
        while n != 0:
            array.append(n % k)
            n //= k
        return sum(array)

    @staticmethod
    def check_if_pangram(sentence: str) -> bool:
        check = 'abcdefghijklmnopqrstuvwxyz'
        if all([sentence.count(char) > 0 for char in check]):
            return True
        return False

    @staticmethod
    def separate_digits(nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            for char in str(num):
                output.append(int(char))
        return output

    @staticmethod
    def sort_people(names: List[str], heights: List[int]) -> List[str]:
        joined = []
        for x in range(len(names)):
            joined.append([heights[x], names[x]])
        output = []
        joined = reversed(sorted(joined))
        for entry in joined:
            output.append(entry[1])
        return output

    @staticmethod
    def smallest_even_multiple(n: int) -> int:
        return n if n % 2 == 0 else n * 2

    @staticmethod
    def third_max(nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        first = -float('inf')
        second = -float('inf')
        third = -float('inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
        if len(nums) < 3:
            return first
        else:
            return third

    @staticmethod
    def fizz_buzz(n: int) -> List[str]:
        answer = []
        for x in range(1, n + 1):
            if (x % 15) == 0:
                answer.append("FizzBuzz")
            elif (x % 5) == 0:
                answer.append("Buzz")
            elif (x % 3) == 0:
                answer.append("Fizz")
            else:
                answer.append(f"{x}")
        return answer

    @staticmethod
    def find_the_difference(s: str, t: str) -> str | None:
        s = [char for char in s]
        for char in t:
            if char not in s:
                return char
            else:
                s.remove(char)
        return None

    def number_of_nodes(self, root: Optional[TreeNode]) -> int:
        if root:
            self.total_nodes += 1
        if root.left:
            self.number_of_nodes(root.left)
        if root.right:
            self.number_of_nodes(root.right)
        return self.total_nodes

    def sum_of_left_leaves(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            self.left_leaves_entry.append(root.val)
        if root.left:
            self.sum_of_left_leaves(root.left)
        if root.right and (root.right.left or root.right.right):
            self.sum_of_left_leaves(root.right)
        if self.number_of_nodes(root) != 1:
            return sum(self.left_leaves_entry)
        else:
            return 0

    @staticmethod
    def can_construct(ransom_note: str, magazine: str) -> bool:
        magazine_arr = [char for char in magazine]
        for char in ransom_note:
            if char in magazine_arr:
                magazine_arr.remove(char)
            else:
                return False
        return True

    @staticmethod
    def summary_ranges(nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [f"{nums[0]}"]

        answers = []
        start = 0
        for index in range(1, len(nums)):
            if nums[index] - nums[index - 1] > 1:
                answers.append(nums[start:index])
                start = index
        answers.append(nums[start:len(nums)])
        answer = []
        for ans in answers:
            if ans not in answer:
                answer.append(ans)

        for i in range(len(answer)):
            if answer[i][0] == answer[i][-1]:
                answer[i] = f"{answer[i][0]}"
            else:
                answer[i] = f"{answer[i][0]}->{answer[i][-1]}"

        return answer

    @staticmethod
    def is_palindrome_linked_list(head: Optional[ListNode]) -> bool:
        head_lv = []
        while head:
            try:
                head_lv.append(head.val)
                head = head.next
            except AttributeError:
                break
        if head_lv == head_lv[::-1]:
            return True
        return False

    @staticmethod
    def is_power_of_two(n: int) -> bool:
        if n < 1:
            return False

        while n != 1:
            if n % 2 == 1:
                return False
            else:
                n //= 2
        return True

    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        return not (len(nums) == len(set(nums)))

    def is_happy(self, n: int) -> bool:
        while (n != 1) and (n not in self.happy_sequence):
            self.happy_sequence.append(n)
            n = sum([int(x) ** 2 for x in str(n)])
        if n == 1:
            return True
        else:
            return False

    @staticmethod
    def hamming_weight(n: int) -> int:
        return bin(n)[2:].count("1")

    @staticmethod
    def reverse_bits(n: int) -> int:
        b_str = ((32 - len(bin(n)[2:])) * "0") + bin(n)[2:]
        b_str = b_str[::-1]
        return int(b_str, 2)

    @staticmethod
    def majority_element(nums: List[int]) -> int | None:
        values = list(set(nums))
        for val in values:
            if nums.count(val) > len(nums) / 2:
                return val
        return None

    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result

    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = [num for num in nums1 if num in nums2]
        return list(set(intersection))

    @staticmethod
    def reverse_vowels(s: str) -> str:
        start = 0
        end = len(s) - 1
        s = [char for char in s]
        check = ['A', 'U', 'O', 'I', 'E', 'a', 'e', 'i', 'o', 'u']
        while start < end:
            if s[start] not in check:
                start += 1
            if s[end] not in check:
                end -= 1
            if s[start] in check and s[end] in check:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return "".join(s)

    @staticmethod
    def is_power_of_four(n: int) -> bool:
        if n < 1:
            return False
        while n != 1:
            if n % 4 == 0:
                n //= 4
            else:
                return False
        return True

    @staticmethod
    def count_bits(n: int) -> List[int]:
        ans = []
        for x in range(n + 1):
            ans.append(bin(x).count("1"))
        return ans

    @staticmethod
    def num_of_pairs(nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        count += 1

        return count

    @staticmethod
    def count_segments(s: str) -> int:
        a = s.split()
        return len(a)

    @staticmethod
    def interpret(command: str) -> str:
        m = ""
        for x in range(len(command)):
            if command[x] == "G":
                m += "G"
            if not (x + 2 > len(command)):
                if command[x:x + 2] == "()":
                    m += "o"
            if not (x + 4 > len(command)):
                if command[x:x + 4] == "(al)":
                    m += "al"
        return m

    @staticmethod
    def find_middle_index(nums: List[int]) -> int:
        for x in range(len(nums)):
            if sum(nums[:x]) == sum(nums[x + 1:]):
                return x
        return -1

    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inorder_traversal(root.left)
            self.traverse_inorder.append(root.val)
            self.inorder_traversal(root.right)
        return self.traverse_inorder

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

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        c = True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p and q:
            c = c and (p.val == q.val)
            if p.left and q.left:
                c = c and self.is_same_tree(p.left, q.left)
            if p.right and q.right:
                c = c and self.is_same_tree(p.right, q.right)
            if (p.left and not q.left) or (not p.left and q.left) or (p.right and not q.right) or (
                    not p.right and q.right):
                return False
        return c

    @staticmethod
    def find_peaks(mountain: List[int]) -> List[int]:
        peaks = []
        for x in range(len(mountain)):
            if x - 1 != -1 and x + 1 != len(mountain):
                if (mountain[x] > mountain[x - 1]) and (mountain[x] > mountain[x + 1]):
                    peaks.append(x)
        return peaks

