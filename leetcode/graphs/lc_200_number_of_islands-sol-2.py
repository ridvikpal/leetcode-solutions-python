from collections import deque
from typing import List


'''
https://leetcode.com/problems/number-of-islands/description/
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # get the dimensions of the grid        
        row_len = len(grid)
        col_len = len(grid[0])

        # setup the directions we can search in
        # for adjacent 1s to connect land forming an island
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # create a set to keep track of (row, col) pairs
        # we have already visited to form an island
        visited_ones = set()

        # our breadth first search function
        # used to explore all adjacent connected 1s
        # and mark them as visited, discovering an island
        def bfs(row, col):
            # first initialize our bfs queue with
            # the input cell
            queue = deque([(row, col)])

            # then add the initial cell to our visited set
            visited_ones.add((row, col))

            # keep looping until the queue is empty
            while queue:
                # pop the current cell from the queue
                current_row, current_col = queue.popleft()

                # loop through all adjacent directions
                for dx, dy in directions:
                    # get the adjacent cell
                    adjacent_row = current_row+dx
                    adjacent_col = current_col+dy

                    # only add adjacent cell to bfs queue if
                    # 1) adjacent cell is in grid bounds
                    # 2) adjacent cell contains a '1'
                    # 3) we have not visited this adjacent cell before
                    if (0 <= adjacent_row < row_len and
                        0 <= adjacent_col < col_len and
                        grid[adjacent_row][adjacent_col] == '1' and
                        (adjacent_row, adjacent_col) not in visited_ones):
                        # add the adjacent cell to the bfs queue
                        queue.append((adjacent_row, adjacent_col))
                        # add the adjacent cell to our visited set
                        visited_ones.add((adjacent_row, adjacent_col))

        # setup our variable to hold the count of the number of islands
        island_count = 0
        # loop through all rows in the grid
        for row in range(row_len):
            # loop through all cols in the grid
            for col in range(col_len):
                # only explore for an island if
                # 1) the cell contains a '1'
                # 2) we have not visited this cell before
                if (grid[row][col] == '1' and
                    (row, col) not in visited_ones):
                    # run our recursive dfs function to explore
                    # the island and mark it as visited
                    bfs(row, col)
                    # increment the island count
                    island_count += 1

        # finally return the total island count
        return island_count
