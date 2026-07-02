class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        if x < 0:
            x = abs(x)
            count = 1
        quotient = x
        res = 0
        while quotient > 0:
            quotient, remainder = divmod(quotient, 10)
            res = res * 10 + remainder
        if res < -2 ** 31 or res > (2 ** 31) - 1:
            return 0
        if count == 1:
            return -res
        return res




        