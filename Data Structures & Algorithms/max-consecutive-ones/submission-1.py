class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        output = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                l = i + 1
            output = max(output , i - l + 1)

        return output