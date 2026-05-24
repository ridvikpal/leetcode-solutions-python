from functools import cache


'''
https://leetcode.com/problems/decode-ways/description/
'''
class Solution:
    # we will use top down dynamic programming
    # to memoize a recursive function to solve this problem
    def numDecodings(self, s: str) -> int:
        # setup our recrusive function that searches all possible
        # combinations of mappings
        # note we don't actually need to perform the decoding
        # we just need to count the possible ways to decode
        # we will also use @cache for automatic memoization
        @cache
        def search(index) -> int:
            # setup our recrusive base cases
            # the first is when our index is out of bounds
            if index >= len(s):
                # in this case, we have completed a full
                # decoding, so return 1 because we have found
                # one new combination
                return 1
            # the second base case is if we have a 0
            # for the char at this index
            if s[index] == '0':
                # in that case, we return 0 because this
                # is an invalid mapping -> we can't decode 0
                return 0

            # otherwise, we are visiting this index for the first time
            # so start off by checking two chars if they exist
            # this index + next index
            # if they are between 10 and 26, because that means two mappings exist
            # Ex. 12 can be '1' or '12'
            if index < len(s)-1 and 10 <= int(s[index:index+2]) <= 26:
                # in this case, we have two possible mappings, so branch out
                # recursively 2 times:
                # first time: go normally to next index (+1), selecting 1 digit out of 2
                # second time: skip next index (+2), selecting 2 digits fully
                return search(index+1) + search(index+2)

            # else we know that the char < 10 so only 1 mapping exists
            # go normally to the next index recrusively
            return search(index+1)

        # finally begin searching at index 0 and return the value
        return search(0)
