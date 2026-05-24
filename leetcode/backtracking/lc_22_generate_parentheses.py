from typing import List


'''
https://leetcode.com/problems/generate-parentheses/description/
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # init our result array
        # this will hold all parentheses combinations
        result = []
        # init our parentheses combination
        # this will hold a single possible
        # parentheses combination
        parentheses = []

        # our recursive backtracking search funciton
        # that will make a decision on each iteration to either
        # 1) add an OPEN parentheses
        # 2) add a CLOSE parentheses
        # it takes in the limit of possible open
        # parentheses to add and the limit of possible 
        # close parentheses to add
        def search(open_limit, close_limit):
            # if our open limit and close limit is 0
            # then we can't add anymore parentheses
            # so this is our base case
            if open_limit == close_limit == 0:
                # so add the string version of
                # parentheses array to the results array
                result.append("".join(parentheses))
                # and return
                return

            # check if we can add open parentheses first
            # since open parentheses always come before close parentheses
            if open_limit > 0:
                # first test with adding an open parentheses
                parentheses.append('(')
                # and recurse with 1 less open parentheses limit
                search(open_limit-1, close_limit)
                # after backtracking, pop the open parentheses we had added
                parentheses.pop()
            
            # check if we can add close parentheses
            # we can only add close parentheses if the limit
            # for close parentheseses is > limit for open parentheses
            # otherwise the parentheses would not be valid
            # ex: invalid parentheses "((())" -> 3 "(" and 2 ")"
            if close_limit > open_limit:
                # second test with adding a close parentheses
                parentheses.append(')')
                # and recurse with 1 less close parenthese limit
                search(open_limit, close_limit-1)
                # after backtracking, pop the close parenthese we had added
                # this is because we want to have 2n parentheses
                # and if we don't do this we will have more than 2n parentheses
                parentheses.pop()

        # begin our search with n as limit for both open
        # and close brackets
        search(n, n)

        # finally return the results array
        return result
