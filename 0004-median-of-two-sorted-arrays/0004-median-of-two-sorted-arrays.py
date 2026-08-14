class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final = sorted(nums1 + nums2)
        mid = len(final)//2
        if len(final) % 2 == 1:
            return float(final[mid])

        return (final[mid] + final[mid-1]) / 2
        