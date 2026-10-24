class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
we cans slidign window apprahc under which 
we have 2 pointers
the right pointer isoperated thorugh a for loop and keeps gogn forward
the left is operated through a while loop until best not beaten 

        '''
        # lo = prices[0]
        # profit = 0 
        # left=0
        # right=0
        # for right in range(len(prices)):
        #     while prices[left]<lo:
        #         lo=prices[left]
        #         left+=1
        #     profit=max(profit, prices[right]-prices[left])
        # return profit

        left=0
        profit=0
        for right in range(len(prices)):
            while prices[left]>prices[right]:
                left+=1
            profit=max(profit, prices[right]-prices[left])
        return profit