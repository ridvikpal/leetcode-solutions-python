from collections import defaultdict
from typing import List


'''
https://leetcode.com/problems/valid-sudoku/description/
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create ditionary mapping row index -> set of numbers in row
        row_dictionary = defaultdict(set)
        # create dictionary mapping col index -> set of numbers in col
        col_dictionary = defaultdict(set)
        # create dictionary mapping 
        # (sub_box_row, sub_box_col) -> set of numbers in sub_box
        # note that 0 <= sub_box_row, sub_box_col < 2
        sub_box_dictionary = defaultdict(set)

        # store the row and col length of the grid
        # this is always going to be 9x9 for a sudoku grid
        row_len = 9
        col_len = 9

        # loop through all rows in the sudoku board
        for row in range(row_len):
            # loop through all cols in the sudoku board
            for col in range(col_len):
                # get the current cell
                current_cell = board[row][col]

                # we only want to proceed if there is a number
                # in the current cell, it can't be '.'
                if current_cell != '.':
                    # check if the current cell exists in our row already
                    if current_cell in row_dictionary[row]:
                        # if it does, return False
                        return False
                    # else it doesn't exist
                    else:
                        # so add it our row dictionary
                        row_dictionary[row].add(current_cell)

                    # check if the current cell exists in our col dictionary
                    if current_cell in col_dictionary[col]:
                        # if it does, return False
                        return False
                    # else it doesn't exist
                    else:
                        # so add it to our col dictionary
                        col_dictionary[col].add(current_cell)

                    # map the current row to the appropriate sub_box_row
                    # between [0, 3)
                    sub_box_row = row // 3
                    # map the current col to the appropriate sub_box_col
                    # between [0, 3)
                    sub_box_col = col // 3

                    # check if the current cell exists in our sub_box already
                    if current_cell in sub_box_dictionary[(sub_box_row, sub_box_col)]:
                        # if it does, return False
                        return False
                    # else it doesn't exist
                    else:
                        # so add it our sub_box_dictionary
                        sub_box_dictionary[(sub_box_row, sub_box_col)].add(current_cell)

        # if we loop through the entire grid without
        # detecting any duplicates, the grid is valid
        # so return true
        return True
