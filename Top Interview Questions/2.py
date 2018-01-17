# coding=utf-8

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        思路：任何时候先买一个，i记录买的价格，然后j想前走一格，如果发现下一个价格比i的价格高，就在j的地方卖掉，如果发现j的价格比i的价格低 ，则在i的价格卖掉
        j循环到len(prices) - 1 的时候结束
        """
        total = 0

        if not prices:
            return total
        else:
            i, j = prices[0], 1
            while j <= (len(prices) - 1):
                if i < prices[j]:
                    total += (prices[j] - i)
                i = prices[j]
                j += 1
            return total

if __name__ == '__main__':
    print Solution().maxProfit([10,9,8,1,10,1,2])


