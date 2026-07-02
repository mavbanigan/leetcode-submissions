class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        count = 0
        max_count = 0
        minH = 0
        while l < r:
            minH = min(height[l], height[r])
            count = minH*(r-l)
            max_count = max(max_count, count)
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return max_count
                