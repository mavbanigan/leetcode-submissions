class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapN = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in mapN:
                return [mapN[diff], i]
            mapN[num] = i


