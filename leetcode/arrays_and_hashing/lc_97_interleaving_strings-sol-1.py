from functools import cache


'''
https://leetcode.com/problems/interleaving-string/description/
'''
class Solution:
    # we will use a top down dynamic programming solution
    # by memoizing a recursive function
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # create our recursive (backtracking) search function
        # it will return true if s3 can be created by
        # interleaving s1 and s2
        # it takes index1 as the current index of s1 char to check
        # and index2 as the current index of s2 char to check
        # we will use @cache to automatically memoize 
        # the output of the function
        @cache
        def search(index1, index2) -> bool:
            # index3 is the index of s3 char to check
            # it will always be index1 + index2 as long
            # as s3 is made by interleaving s1 and s2
            index3 = index1 + index2

            # our base case is once our index3 is fully
            # out of bounds
            if index3 >= len(s3):
                # if index1 and index2 are also out of bounds
                # that means we have created s3 by interlaving
                # s1 and s2 together
                if index1 >= len(s1) and index2 >= len(s2):
                    # so we can return true
                    return True
                # else that means we have iterated through s3
                # but not iterated through s1 and s2 both
                # so we cannot create s3 by interleaving s1 and s2
                else:
                    # so return false
                    return False

            # init the results of our two decisions
            # to be false to begin with
            choose_first_char = False
            choose_second_char = False

            # if index1 is within bounds of s1
            # and the s1 char at index1 = s3 char at index3 then
            # we can pick this char to use to create s3 and move forward
            # this is our first decision
            if index1 < len(s1) and s1[index1] == s3[index3]:
                # we can set the output of choose first char
                # to be the result of this decision
                choose_first_char = search(index1+1, index2)
            
            # if index2 is within bounds of s2
            # and the s3 char at index2 = s3 char at index3 then
            # we can pick this char to use to create s3 and move forward
            # this is our second decision
            if index2 < len(s2) and s2[index2] == s3[index3]:
                # we can set the output of choose second char
                # to be the result of this decision
                choose_second_char = search(index1, index2+1)

            # finally we will return true if we found a valid
            # path to construct s3 by interleaving s1 and s2
            # from either decision
            return choose_first_char or choose_second_char

        # we will begin our search with index1 and index2 at 0
        return search(0, 0)
