from typing import List


'''
https://leetcode.com/problems/search-a-2d-matrix/description/
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first get the dimensions of the matrix
        row_len = len(matrix)
        col_len = len(matrix[0])

        # VERTICAL BINARY SEARCH ACROSS ROWS
        # we will start with a binary search across rows
        # to find the row the number should be in
        # init our top pointer to point to the first row
        top = 0
        # init our bottom pointer to point to the last row
        bottom = row_len-1

        # our standard binary search while loop
        # we loop as long as the top row is
        # above or equal to the bottom row
        while top <= bottom:
            # we calculate the vertical middle
            # index -> aka. the middle row index
            v_middle = (top+bottom) // 2

            # check if the target is > the last
            # element of the middle row
            if target > matrix[v_middle][-1]:
                # if so, then we know our element
                # is in the next rows after the middle row
                # aka. below the middle row
                # so move the top pointer to v_middle + 1
                top = v_middle + 1
            # check if the target is < the first
            # element of the middle row
            elif target < matrix[v_middle][0]:
                # if so, then we know our element is
                # in the previous rows before the middle row
                # aka. above the middle row
                # so move the bottom ponter to v_middle - 1
                bottom = v_middle - 1
            # else we know our target is in the current
            # middle row
            else:
                # we have found the row the value should be in
                # which is v_middle, so break
                break


        # HORIZONTAL BINARY SEARCH ACROSS COLUMNS
        # once we know the row the number should be in
        # we need to find the column, and for this
        # we will do a horizontal binary search
        # across all columns in the row
        # init the left pointer to point to the first column
        left = 0
        # init the right pointer to point to the last column
        right = col_len-1

        # our standard binary search while loop
        # we loop as long as the left col is
        # before or equal to the to the right column
        while left <= right:
            # we calculate the horizontal middle index
            # -> aka. the middle column index
            h_middle = (left+right) // 2
            
            # check if the target equals the value
            # in the middle of the row
            if target == matrix[v_middle][h_middle]:
                # if it does, we return True
                return True

            # else check if the target is smaller
            # than the value in the middle of the row
            if target < matrix[v_middle][h_middle]:
                # if so, the target is to the left of
                # the middle column, so move the right
                # pointer to h_middle - 1
                right = h_middle - 1
            # else the target is greater than the value
            # in the middle of the row
            else:
                # so the target is to the right of the
                # middle column, so move the left pointer
                # to h_middle + 1
                left = h_middle + 1

        # if we make it here, then we have searched
        # the entire matrix and not found the target
        # so return False
        return False
