class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapN = {}
        for i, num in enumerate(nums):
            if num in mapN:
                if abs(i - mapN[num]) <= k:
                    return True
            mapN[num] = i
        return False

        