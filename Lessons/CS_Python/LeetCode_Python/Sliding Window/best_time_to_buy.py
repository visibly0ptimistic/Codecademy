class Solution:
    def maxProfit(self, prices) -> int:
        left_pointer , right_pointer = 0,1
        maximum_profit = 0
        
        while right_pointer < len(prices):
            if prices[left_pointer] < prices[right_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                maximum_profit = max(maximum_profit, profit)
            else:
                left_pointer = right_pointer
                right_pointer += 1
            return maximum_profit
