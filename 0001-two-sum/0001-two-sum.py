class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapN = {}
        for i, num in enumerate(nums):
            dupe = target - num
            if dupe in mapN:
                return [mapN[dupe], i]
            mapN[num] = i

        