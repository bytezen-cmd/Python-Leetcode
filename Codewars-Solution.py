from typing import List

class Solution:

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