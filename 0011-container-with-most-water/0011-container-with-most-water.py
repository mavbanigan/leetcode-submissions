class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_count = 0
        while l < r:
            count = min(height[l], height[r]) * (r-l)
            if count > max_count:
                max_count = count
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return max_count
        