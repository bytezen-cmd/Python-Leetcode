from typing import List
import math

class Solution:

    @staticmethod
    def comp(array1, array2):
        if array1 == [] and array2 == []:
            return True
        elif (array1 == [] and array2 != []) or (array1 != [] and array2 == []):
            return False
        for element in array1:
            if element ** 2 in array2:
                array2.remove(element ** 2)
            else:
                return False
        return True

    @staticmethod
    def solution(s):
        answer = []
        for x in range(0, len(s), 2):
            if x + 1 != len(s):
                answer.append(f"{s[x]}{s[x + 1]}")
            else:
                answer.append(f"{s[x]}_")
        return answer

    @staticmethod
    def circle_diameter(sides, side_length):
        return side_length / math.tan(math.pi / sides)

    @staticmethod
    def dir_reduction(arr):
        class Stack:
            def __init__(self):
                self.stack = []

            def copy(self):
                return self.stack

            def last(self):
                try:
                    return self.stack[-1]
                except IndexError:
                    return None

            def push(self, x):
                self.stack.append(x)

            def pop(self):
                return self.stack.pop()

        stack = Stack()
        dict_x = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
        for DIR in arr:
            if stack.last():
                if dict_x[DIR] == stack.last():
                    stack.pop()
                else:
                    stack.push(DIR)
            else:
                stack.push(DIR)
        return stack.copy()

    @staticmethod
    def likes(names: List[str]):
        if len(names) == 0:
            return "no one likes this"
        elif len(names) == 1:
            return f"{names[0]} likes this"
        elif len(names) == 2:
            return f"{names[0]} and {names[1]} like this"
        elif len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        else:
            return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

    @staticmethod
    def digital_root(n):
        while len(str(n)) != 1:
            string_n = str(n)
            sum_n = 0
            for digit in string_n:
                sum_n += int(digit)
            n = sum_n
        return n

    @staticmethod
    def create_phone_number(n):
        return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

    @staticmethod
    def is_isogram(string):
        if string == "":
            return True

        string = string.lower()

        if len(string) == len(set(string)):
            return True
        return False

    @staticmethod
    def find_even_index(arr):
        for i in range(0, len(arr)):
            if sum(arr[:i]) == sum(arr[i + 1:]):
                return i
        return -1

    @staticmethod
    def find_uniq(arr):
        if len(arr) <= 2:
            return arr[0]
        if arr[0] != arr[1] and arr[1] == arr[2]:
            return arr[0]
        elif arr[-1] != arr[-2] and arr[-2] == arr[-3]:
            return arr[-1]

        for i in range(1, len(arr) - 1):
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]
        return None

    @staticmethod
    def array_diff(a, b):
        for num in b:
            for _ in range(a.count(num)):
                a.remove(num)
        return a