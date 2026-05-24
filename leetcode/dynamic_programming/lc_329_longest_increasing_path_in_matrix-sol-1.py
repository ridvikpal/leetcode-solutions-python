from functools import cache
from typing import List


'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
'''
class Solution:
    # we will use dynamic programming with a top-down approach
    # to memoize a recursive graph dfs function
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # first get the dimensions of the matrix
        row_len = len(matrix)
        col_len = len(matrix[0])

        # setup the directions we can search in
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # create our recursive dfs function that
        # will find the longest increasing path in
        # the matrix for a given (row, col) cell
        # we can memoize the result of this function
        # with @cache because the longest increasing path
        # will always be the same from every cell
        # also, we don't need a visited set because
        # there is only 1 longest increasing path
        # from each cell, and memoizing will automatically
        # return that result preventing us from visiting the
        # same paths again
        @cache
        def dfs(row, col) -> int:
            # init the path length from the
            # adjacent cells to 0
            adjacent_path_length = 0
            # init the maximum path length from the
            # adjacent cells to 0 as well
            max_adjacent_path_length = 0

            # loop through all directions
            for dx, dy in directions:
                # get the adjacent cell coordinates
                adj_row, adj_col = row+dx, col+dy

                # only explore adjacent cells if:
                # 1) adjacent cells are within matrix bounds
                # 2) the adjacent cell's value is >
                #    current cell's value
                if (0 <= adj_row < row_len and
                    0 <= adj_col < col_len and
                    matrix[adj_row][adj_col] > matrix[row][col]):

                    # recursively calculate the adjacent path length
                    # by calling dfs on the adjacent cell and store it
                    adjacent_path_length = dfs(adj_row, adj_col)
                    # update the max path length if we find a longer path
                    # from the adjacent cell
                    max_adjacent_path_length = max(adjacent_path_length, max_adjacent_path_length)

            # finally at each function call we simply return 
            # 1 (because we visited this cell) + the max
            # path length of the adjacent cells fro this cell
            return 1 + max_adjacent_path_length

        # we can init our max path length that 
        # we have found
        max_path_len = 0

        # loop through all rows
        for row in range(row_len):
            # loop through all columns
            for col in range(col_len):
                # run dfs to find the path length
                # from this row or col
                path_len = dfs(row, col)
                # and update the max path length accordingly
                max_path_len = max(path_len, max_path_len)

        # finally we can return the max path length
        # we have found
        return max_path_len
