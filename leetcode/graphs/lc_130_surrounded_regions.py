from typing import List


'''
https://leetcode.com/problems/surrounded-regions/description/
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # first get the dimensions of the board
        row_len = len(board)
        col_len = len(board[0])

        # setup the directions we can travel in
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # our recursive dfs function, which will
        # look for adjacent 'O' cells to (row, col) and
        # mark them as '1' instead
        # we will use it to find all adjacent 'O' cells to
        # the 'O' cells at the borders of the board and
        # flip them to '1', so they we know which 'O' cells
        # we CANNOT mark as surrounded and flip to 'X"
        def dfs(row, col):
            # set the current (row, col) to '1'
            board[row][col] = '1'

            # loop through all directions we can search for
            for dx, dy in directions:
                # calculate the adjacent cell
                adjacent_row, adjacent_col = row+dx, col+dy

                # only run recursive dfs on the adjacent cell if
                # 1) the adjacent cell is within bounds
                # 2) the adjacent cell contains a 'O'
                if (0 <= adjacent_row < row_len and
                    0 <= adjacent_col < col_len and
                    board[adjacent_row][adjacent_col] == 'O'):
                    # run recursive dfs on the adjacent cell
                    dfs(adjacent_row, adjacent_col)

        # loop throgh all rows
        for row in range(row_len):
            # check the left border for 'O' cells
            if board[row][0] == 'O':
                # and run dfs on them if they exist
                dfs(row, 0)
            # check the right border for 'O' cells
            if board[row][col_len-1] == 'O':
                # and run dfs on them if they exist
                dfs(row, col_len-1)

        # loop through all cols
        for col in range(col_len):
            # check the top border for 'O' cells
            if board[0][col] == 'O':
                # and run dfs on them if they exist
                dfs(0, col)
            # check the bottom border for 'O' cells
            if board[row_len-1][col] == 'O':
                # and run dfs on them if they exist
                dfs(row_len-1, col)

        # loop through all rows
        for row in range(row_len):
            # loop through all cols
            for col in range(col_len):
                # check if the cell is an 'O'
                if board[row][col] == 'O':
                    # if it is, flip it to make it an 'X"
                    board[row][col] = 'X'
                # check if the cell is a '1' from our dfs function
                elif board[row][col] == '1':
                    # if it is, set it back to a 'O'
                    # these were groups of 'O' cells touching the border
                    # that are not surrounded
                    board[row][col] = 'O'
