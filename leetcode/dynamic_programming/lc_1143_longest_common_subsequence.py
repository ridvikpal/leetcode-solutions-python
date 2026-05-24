'''
https://leetcode.com/problems/longest-common-subsequence/description/
'''
class Solution:
    # we will use a bottom up dynamic programming approach
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create our dynamic programming 2d array which will
        # hold the longest common subsequence (lcs) for selcted
        # substrings up to text1 index in row and up to text2 index in col
        # we have an extra row index 0 and col index 0 filled with 0 to handle
        # base case where we select no chars from either substring
        # row index -> index from text1 where we are creating a substring from
        #              note text1 index + 1 = lcs index
        # col index -> index from text2 where we are creating a substring from
        #              note text2 index + 1 = lcs index
        # value -> longest common substrings for that combination of
        #          text1 and text2 substrings
        lcs = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        # loop through all indices in text1
        for i in range(len(text1)):
            # loop through all indices in text2
            for j in range(len(text2)):
                # first check if the chars at this index
                # are the same for both strings
                if text1[i] == text2[j]:
                    # if they are, then we can take the lcs of
                    # the text1 and text2 substrings without this char
                    # at this index and add 1 to it to get the new lcs
                    # at this index, because we found a new common char
                    # lcs[i][j] -> lcs of text1 and text2 substrings that are
                    #              the exact same but without this char at this index
                    # lcs[i+1][j+1] -> new lcs of text1 and text2 substrings with 
                    #                  this new char
                    lcs[i+1][j+1] = lcs[i][j] + 1
                # else the chars at this index are not the same
                # for both strings
                else:
                    # in this case, we just take the max of whichever
                    # text1 and text2 substring combo did not have their last char
                    # lcs[i+1][j] -> lcs of same text1 substring but text2 
                    #                substring without last char
                    # lcs[i][j+1] -> lcs of same text2 substring but text1
                    #                substring without last char
                    # lcs[i+1][j+1] -> new lcs of text1 and text2 substrings
                    #                  both with their new char
                    lcs[i+1][j+1] = max(lcs[i+1][j], lcs[i][j+1])

        # finally, return the lcs we found for the entire text1
        # and entire text2, the bottom right corner of lcs 2d array
        return lcs[-1][-1]
