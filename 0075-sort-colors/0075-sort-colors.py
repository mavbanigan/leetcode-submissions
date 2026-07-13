class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 0
        e = len(nums)-1
        while r <= e:
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
            elif nums[r] == 1:
                r+=1
            else:
                nums[r], nums[e] = nums[e], nums[r]
                e-=1
        
        