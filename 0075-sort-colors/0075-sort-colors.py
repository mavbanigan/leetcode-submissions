class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        ptr = 0
        while ptr <= r:
            if nums[ptr] == 0:
                nums[ptr], nums[l] = nums[l], nums[ptr]
                l+=1
                ptr+=1
            elif nums[ptr] == 1:
                ptr+=1
            else:
                nums[ptr], nums[r] = nums[r], nums[ptr]
                r-=1
        