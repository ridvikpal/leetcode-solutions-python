from typing import List


'''
https://leetcode.com/problems/delete-columns-to-make-sorted/description/
'''
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # first get the dimensions of our string grid
        row_len = len(strs)
        col_len = len(strs[0])

        # init our count variable
        count = 0

        # loop through all columns first
        for col in range(col_len):
            # then loop thorugh all rows
            for row in range(1, row_len):
                # we want to check each column
                # row by row to see if each row in the column
                # is sorted in ascending lexicographic order
                # so check if the next element is smaller than
                # the previous one (i.e., check if it's not sorted)
                if strs[row][col] < strs[row-1][col]:
                    # if it is not, increment the count
                    count += 1
                    # and break immediately
                    # no need to check the rest of the rows
                    # in the column
                    break

        # finally, return the count
        return count
