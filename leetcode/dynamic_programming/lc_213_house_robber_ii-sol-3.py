from typing import List


'''
https://leetcode.com/problems/house-robber-ii/description/
'''
class Solution:
    # we will use a dynamic programming with bottom-up
    # tabular memoization method to solve this problem
    def rob(self, nums: List[int]) -> int:
        # our base case is if there are at most 3 houses
        # 1 house -> only rob that 1 house
        # 2 houses -> rob the max of those 2 houses
        # 3 houses -> rob the max of those 3 houses
        if len(nums) <= 3:
            # so simply return the max of those houses
            return max(nums)

        # we will reuse our previous house robber solution
        # so we can recreate that function
        def houseRobber1(input_nums):
            # our base case is if there are at most 2 houses
            # 1 house -> only rob that 1 house
            # 2 houses -> rob the max of those 2 houses
            if len(input_nums) <= 2:
                # so simply return the max of those houses
                return max(input_nums)

            # otherwise, setup our money array where
            # index -> number of houses we will consider robbing
            # value -> max money we can rob with that many houses
            # remember arrays are 0 indexed, so
            # index 0 means robbing 1 house
            # index 1 means robbing 2 houses
            # and so on
            money = [0]*len(input_nums)

            # init our bases cases for our array
            # if we have 1 house, we must rob it
            money[0] = input_nums[0]
            # if we have 2 houses, we must rob the max house
            money[1] = max(input_nums[0], input_nums[1])

            # now loop through all indices 2 to last index in money array
            for i in range(2, len(money)):
                # the max money we can earn by robbing a i houses
                # is equal to the max of
                # 1) the max money for robbing 1 less house (index-1)
                #    since we can't rob adjacent houses and skip this house
                # 2) the max money for robbing 2 less houses (index-2)
                #    along with this house because we skipped the last house
                money[i] = max(money[i-2] + input_nums[i], money[i-1])

            # finally we will return the max money we can get
            # for robbing all the houses, which is last index in money array
            return money[-1]

        # the key to this problem is understanding it is the same
        # as house robber 1, but you have to choose whether to rob
        # the first or last house, you can't rob both
        # if you rob the first house, skip the last house
        # store the associated nums in a new array
        choose_first = nums[:len(nums)-1]
        # if you rob the last house, skip the first house
        # store the associated nums in a new array
        choose_last = nums[1:]

        # just return the max money from either decision,
        # robbing the first or last house, never both
        return max(houseRobber1(choose_first), houseRobber1(choose_last))
