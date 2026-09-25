class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1
        prev = 1
        for i in range(1, n):
            curr, prev = curr + prev, curr
        return curr