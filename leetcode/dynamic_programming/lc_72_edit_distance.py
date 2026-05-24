'''
https://leetcode.com/problems/edit-distance/description/
'''
class Solution:
    # this is essentially computing the Levenshtein Distance
    # we can use a bottom up dynamic programming approach to solve it
    def minDistance(self, word1: str, word2: str) -> int:
        # init our dynamic programming 2d memoization array
        # row indexes -> 1-indexed indices for word1 substring we are comparing
        # col indexes -> 1-indexed indices for word2 substring we are comparing
        # value -> the minimum levenshtein distance for the substring comparision
        #          between word1[:row] and word2[:col]
        # note the row and col have an extra 0 row and 0 col, this is to
        # handle our base case where the levenshtein distance for comparing two
        # empty strings is 0
        edit_distances = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        # fill in our base cases for deletions to convert from word1 -> empty word2
        # when word1 is non-empty, and word2 is empty, we need to delete all chars
        # from word1
        for row in range(len(edit_distances)):
            # so we can set all elements in column 0 to be the row index
            edit_distances[row][0] = row

        # fill in our base cases for insertions is to convert from empty word1 -> word2
        # when word1 is empty, and word2 is non-empty, we need to add all chars
        # from word2
        for col in range(len(edit_distances[0])):
            # so we can set all elements in row 0 to be the col index
            edit_distances[0][col] = col

        # loop through all rows
        for row in range(1, len(edit_distances)):
            # loop through all cols
            for col in range(1, len(edit_distances[row])):
                # compare each new char for each row, col
                # our first case is if the chars are the same
                # we must subtract 1 because the edit distances
                # array is 1-indexed
                if word1[row-1] == word2[col-1]:
                    # if the chars are the same, then the edit distance
                    # must be the same as the edit distance without this
                    # char for both words
                    edit_distances[row][col] = edit_distances[row-1][col-1]
                # else the chars are not the same
                else:
                    # we will choose the previous smallest edit distance
                    # to choose the optimal decision between
                    # inserting (topmost value), 
                    # deleting (leftmost value),
                    # replacing element (topleft diagonal value)
                    # when compared to the last substring comparision
                    # between the two words
                    # and then add 1 to the previous smallest edit
                    # distance because we are making 1 edit
                    edit_distances[row][col] = 1 + min(
                        edit_distances[row-1][col], # inserting
                        edit_distances[row][col-1], # delting
                        edit_distances[row-1][col-1] # replacing
                    )

        # finally, we return the bottom right element
        # from our edit distances matrix, which is the
        # smallest levenshtein distance for comparing
        # the full word1 and full word2
        return edit_distances[-1][-1]
