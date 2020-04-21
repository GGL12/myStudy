class Solution:
    def myAtoi(self, str: str) -> int:
        res = 0
        i = 0
        flag = 1
        INT_MAX = 1 << 31 - 1
        INT_MIN = 1 << 31
        while (str[i] == " "): i += 1
        if not str[i:]:
            return 0
        if (str[i] == "-"): flag = -1
        if (str[i] == "+") or (str[i] == "-"): i += 1

        while ((i < len(str)) and str[i].isdigit()):
            value = ord(str[i]) - ord("0")
            res = res * 10 + value
            if res > INT_MIN:
                return -INT_MIN
            if res > INT_MAX:
                return INT_MAX
            i += 1

        return res if flag > 0 else -res

    def fun2(self, str):
        import re
        return max(min(int(re.findall("^[\+\-]?\d+", str.lstrip())), 2 ** 31 - 1), -2 ** 31)