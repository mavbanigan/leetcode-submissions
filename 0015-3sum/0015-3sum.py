class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i != 0:
                continue
            target = nums[i] * -1
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                else:
                    l+=1
        return res
                



        ''
        