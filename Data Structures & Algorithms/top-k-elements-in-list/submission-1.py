class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}
        output = []
        for ch in nums:
            frq[ch]  = frq.get(ch , 0) + 1
        
        output = sorted(frq , key=frq.get , reverse=True)
        return output[:k]