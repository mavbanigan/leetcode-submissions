class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        new = 0
        c=0
        while x > new:
            x, c = divmod(x, 10)
            new = new * 10 + c
        return new == x or x == new // 10

        