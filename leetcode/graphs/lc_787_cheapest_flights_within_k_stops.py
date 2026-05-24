import math
from typing import List


'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
'''
class Solution:
    # we will use a modified version of the bellman-ford algorithm
    # where we only iterate k+1 times and use a temp cost array
    # so we only relax weights with the previous cost array
    # rather than the real-time cost array
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # init our min prices (cost) array
        min_prices = [math.inf] * n
        # set the source node's min price (min cost) to 0
        min_prices[src] = 0
        
        # loop k+1 times
        for _ in range(k+1):
            # make a copy of our min prices array
            # called temp prices
            # this will hold the modified min prices
            # as we loop through all edges in the flights graph
            temp_prices = min_prices.copy()
            
            # loop through all edges in the flights graph
            for from_city, to_city, price in flights:
                # if the min price to get to the from city is
                # infinite, so far we cannot reach the from city
                # and so skip this iteration, no point in checking
                # for relaxation
                if min_prices[from_city] == math.inf:
                    continue

                # otherwise, perform the relaxation step
                # check if the previous min price for from city + edge price
                # is less than the current temp price for to city we have 
                # calculated on this iteration
                # note we use min price to update temp price, instead of regular
                # bellman-ford where we would do everything in min price
                if min_prices[from_city] + price < temp_prices[to_city]:
                    # if it is less, then update the temp price for to city
                    temp_prices[to_city] = min_prices[from_city] + price
            
            # at the very end, set min prices to be the temp prices
            min_prices = temp_prices

        # finally, return the minimum price of the destination
        # if we have reached it, otherwise we have not reached it
        # the price is infinite and so return -1
        return min_prices[dst] if min_prices[dst] != math.inf else -1
