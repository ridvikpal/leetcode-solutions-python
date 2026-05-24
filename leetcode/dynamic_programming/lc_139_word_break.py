from typing import List


'''
https://leetcode.com/problems/word-break/description/
'''
class Solution:
    # we will use a bottom up tabular dynamic programming approach
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # first get the maximum length of a word in wordDict
        maxWordLen = max([len(word) for word in wordDict])
        
        # next create a word set from the word dict
        # this will make lookup of a word much faster
        # compared to an array
        wordSet = set(wordDict)

        # create our dynamic programming array
        # this array will tell us if the input string s
        # can be split at a particular index
        # but note that the index in canSplit is +1
        # compared to the index of the string s
        # index -> the index in the string s + 1
        # value -> True if the string s can be split at the index
        # ex: index 3 -> True means string s can be split at index 2
        canSplit = [False]*(len(s)+1)
        # our base case is that for index 0 in canSplit
        # the string s can obviously be split because
        # it makes no change to string s
        # since canSplit index 0 = string s index -1
        canSplit[0] = True

        # loop through all indices in string s
        # these indices will be our end pointer
        # for checking substrings
        for end in range(len(s)):
            # our start pointer will be initialized
            # to be the same as our end pointer
            # essentially we will start by checking
            # a single char where start = end -> point to char
            start = end

            # we expand backwards (leftward) from our end pointer
            # to check substrings up to the max word length 
            # of a word in our word dict
            # so loop as long as start pointer is within bounds
            # and the substring length we are checking is < maxWordLength
            while 0 <= start and end-start < maxWordLen:
                # our substring will be from start to end pointer
                substring = s[start:end+1]

                # check if the substring is a word in the word dict
                # and if the string can be split at the index before
                # the start of the substring
                # remember canSplit is +1 index compared to string s
                # if true we have found a valid word in our wordDict
                # that we can split the string s on
                if substring in wordSet and canSplit[start]:
                    # since we can split the string s here
                    # setup the canSplit value for this index to True
                    # remember again canSplit is +1 index compared to string s
                    canSplit[end+1] = True

                # at each iteration, decrement our start pointer
                # to expand backwards (leftward) from our end pointer
                start -= 1
        
        # finally, we return if the string can be split
        # at it's last index, which is also the last index
        # in the canSplit array
        return canSplit[-1]
