class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = abs(x)
        new = 0
        c=0
        while temp > 0:
            new = new * 10 + temp % 10
            c+=1
            temp = temp // 10
        if new == x:
            return True
        return False

        