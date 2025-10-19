class Solution:

    @staticmethod
    def is_lucky(s) -> bool:
        lucky = [char for char in s]
        lucky = list(set(lucky))
        if lucky != [7,4] or lucky != [4,7] or lucky != [4] or lucky != [7]:
            return False
        return True

    @staticmethod
    def nearly_lucky() -> None:
        line = input()
        count = 0
        for i in range(len(line)):
            if line[i] == "4" or  line[i] == "7":
                count += 1
        str_count = str(count)
        if Solution.is_lucky(str_count):
            print("NO")
        else:
            print("YES")

Solution.nearly_lucky()