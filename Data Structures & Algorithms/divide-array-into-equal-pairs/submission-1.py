class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)
        size = len(s)

        return size == 0