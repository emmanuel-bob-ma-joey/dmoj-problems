class Solution(object):
    def maxProfit(self, prices):
        p1 = prices[0]
        p2 = prices[0]
        max_diff = 0
        for i in range(len(prices)):
            p2 = prices[i]
            if p2 < p1:
                p1 = p2
            if p2-p1 > max_diff:
                max_diff = p2-p1
        return max_diff