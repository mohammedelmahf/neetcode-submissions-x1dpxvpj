class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_area = 0
        for buy in range(len(prices)):
            for sell in range(buy + 1 , len(prices)):
                area = prices[sell] - prices[buy] 
                if area < 0:
                    area = 0
                max_area = max(area , max_area)
        return max_area