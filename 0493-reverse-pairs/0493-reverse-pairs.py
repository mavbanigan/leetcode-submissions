class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        if len(nums) > 1:
            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            count += self.reversePairs(left_half)
            count += self.reversePairs(right_half)

            j=0
            for i in range(len(left_half)):
                while j < len(right_half) and left_half[i] > 2 * right_half[j]:
                    j+=1
                count+=j
            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] > right_half[j]:
                    nums[k] = right_half[j]
                    j+=1
                else:
                    nums[k] = left_half[i]
                    i+=1
                k+=1
            while i < len(left_half):
                nums[k] = left_half[i]
                i+=1
                k+=1
            while j < len(right_half):
                nums[k] = right_half[j]
                j+=1
                k+=1
        return count