class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profix = 0 
        min_price = prices[0]

        for i in range (1, len(prices)):
            current_price = prices[i]
            if (current_price < min_price):
                min_price = current_price
            current_profix = prices[i] - min_price
            if (max_profix < current_profix):
                max_profix = current_profix

        return max_profix
        