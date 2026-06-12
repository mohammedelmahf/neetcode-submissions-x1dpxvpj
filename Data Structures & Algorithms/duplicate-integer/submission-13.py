class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frq = {}
        for ch in nums:
            frq[ch] = frq.get(ch , 0) + 1
        for i in range(len(nums)):
            if frq[nums[i]] > 1:
                return True

        return False