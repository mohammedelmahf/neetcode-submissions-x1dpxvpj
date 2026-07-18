class Solution:
    def maxDifference(self, s: str) -> int:
        frq = {}
        for c in s:
            if c in frq:
                frq[c] += 1
            else:
                frq[c] = 1
        maxv = 0
        minv = float('inf')
        for c in frq.values():
            if c % 2 == 0:
                minv  = min(minv , c)
            else :
                maxv = max(maxv , c)
        return maxv - minv
