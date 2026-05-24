from typing import List


'''
https://leetcode.com/problems/richest-customer-wealth/description/
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # get the number of rows
        # which is also the number of customers
        row_len = len(accounts)

        # init our max wealth variable to 0
        max_wealth = 0

        # loop through all rows
        # aka. loop through all customers
        for row in range(row_len):
            # the wealth is the sum of each customer's
            # account balances
            wealth = sum(accounts[row])
            # update the max_wealth variable accordingly
            max_wealth = max(wealth, max_wealth)

        # finally, return the max wealth
        return max_wealth
