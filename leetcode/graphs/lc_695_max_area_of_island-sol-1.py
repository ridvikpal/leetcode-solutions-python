from typing import List


'''
https://leetcode.com/problems/max-area-of-island/description/
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get the row and col lengths
        row_len = len(grid)
        col_len = len(grid[0])

        # create our visited set to
        # keep track of the 1s we have visited 
        visited_ones = set()

        # setup the directions we can search for adjacent cells in
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # our recursive dfs function to store the area
        # of the island found.
        def dfs(row, col) -> int:
            # add the row and col to our visited set
            visited_ones.add((row, col))
            # set the area at the start to 1 because
            # at the beginning 1 cell has area of 1
            area = 1

            # loop through all the directions
            for dx, dy in directions:
                # get the adjacent cell location
                adjacent_row, adjacent_col = row+dx, col+dy

                # only perform dfs on adjacent cells if
                # 1) the adjacent cell is in bounds
                # 2) the adjacent cell has not been visited before
                # 3) the adjacent cell contains a 1
                if (0 <= adjacent_row < row_len and
                    0 <= adjacent_col < col_len and
                    (adjacent_row, adjacent_col) not in visited_ones and
                    grid[adjacent_row][adjacent_col] == 1):
                    # perform dfs recursively and add neighouring cell's area
                    # to the current area
                    area += dfs(adjacent_row, adjacent_col)

            # return the area of cell and it's neighbours
            return area

        # init our max area
        max_area = 0

        # loop through all rows
        for row in range(row_len):
            # loop through all columns
            for col in range(col_len):
                # use dfs to get the area only if
                # 1) cell contains a 1
                # 2) cell has not been visited before
                if (grid[row][col] == 1 and 
                    (row, col) not in visited_ones):
                    # use dfs to get the area
                    area = dfs(row, col)
                    # update the max area accordingly
                    max_area = max(max_area, area)

        # return the max area
        return max_area
