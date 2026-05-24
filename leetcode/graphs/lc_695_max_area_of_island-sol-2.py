from collections import deque
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

        # our bfsfunction to store the area
        # of the island found.
        def bfs(row, col) -> int:
            queue = deque([(row, col)])
            # add the row and col to our visited set
            visited_ones.add((row, col))
            # set the area at the start to 1 because
            # at the beginning 1 cell has area of 1
            area = 1

            # loop until the queue is empty
            while queue:
                # get the current cell from the queue
                r, c = queue.popleft()

                # loop through all the directions
                for dx, dy in directions:
                    # get the adjacent cell location
                    adjacent_row, adjacent_col = r+dx, c+dy

                    # only add adjacent cell to bfs queue if
                    # 1) the adjacent cell is in bounds
                    # 2) the adjacent cell has not been visited before
                    # 3) the adjacent cell contains a 1
                    if (0 <= adjacent_row < row_len and
                        0 <= adjacent_col < col_len and
                        (adjacent_row, adjacent_col) not in visited_ones and
                        grid[adjacent_row][adjacent_col] == 1):
                        # add adjacent cell to bfs queue
                        queue.append((adjacent_row, adjacent_col))
                        # add adjacent cell to visited set
                        visited_ones.add((adjacent_row, adjacent_col))
                        # increment the area
                        area += 1

            # return the area of cell and it's neighbours
            return area

        # init our max area
        max_area = 0

        # loop through all rows
        for row in range(row_len):
            # loop through all columns
            for col in range(col_len):
                # use bfs to get the area only if
                # 1) cell contains a 1
                # 2) cell has not been visited before
                if (grid[row][col] == 1 and 
                    (row, col) not in visited_ones):
                    # use bfs to get the area
                    area = bfs(row, col)
                    # update the max area accordingly
                    max_area = max(max_area, area)

        # return the max area
        return max_area
