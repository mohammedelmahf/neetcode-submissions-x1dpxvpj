class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        check = 0
        l = 0
        output = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                check += 1
            while check > k:
                if nums[l] == 0:
                    check -= 1
                l+= 1
            output = max(output , 1 + i - l)
        return output