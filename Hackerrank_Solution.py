class HackerrankSolution:

    @staticmethod
    def time_conversion(s):
        if (s[0] + s[1]) == "12" and (s[-2] + s[-1]) == "PM":
            return s[0:8]
        elif (s[0] + s[1]) == "12" and (s[-2] + s[-1]) == "AM":
            return "00" + s[2:8]
        elif (s[-2] + s[-1]) == "PM":
            return str(int(s[0:2]) + 12) + s[2:8]
        else:
            return s[0:8]

