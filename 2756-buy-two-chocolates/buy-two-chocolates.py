
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # sorted the array
        # if the sum of first two element > money: 
        # return money
        sort_prices = sorted(prices)
        cheapset_combine = sort_prices[0]+ sort_prices[1]
        if cheapset_combine > money:
            return money
        else:
            return money - cheapset_combine

        

        