class CodeforcesSolution:

    @staticmethod
    def is_lucky(s) -> bool:
        for char in s:
            if char != "4" and char != "7":
                return False
        return True

    @staticmethod
    def nearly_lucky() -> None:
        line = input()
        count = 0
        for char in line:
            if (char == "4") or (char == "7"):
                count += 1
        if Solution.is_lucky(str(count)):
            print("YES")
        else:
            print("NO")

    @staticmethod
    def translation():
        line1 = input()
        line2 = input()
        if line1[::-1] == line2:
            print("YES")
        else:
            print("NO")


CodeforcesSolution.translation()