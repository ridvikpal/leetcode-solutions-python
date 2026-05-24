from collections import deque
from typing import List


'''
https://neetcode.io/problems/islands-and-treasure/question
'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # first get the dimensions of the grid
        row_len = len(grid)
        col_len = len(grid[0])

        # we will use bfs so setup our bfs queue
        queue = deque()
        # setup our visited set for bfs
        visited = set()

        # setup the directions we can travel in
        # left, right, up, down
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # first we will find all the cells that
        # contain treasure and store them in our queue
        # loop through all rows
        for row in range(row_len):
            # loop through all cols
            for col in range(col_len):
                # if the cell contains treasure
                if grid[row][col] == 0:
                    # add it to our queue
                    queue.append((row, col))
                    # mark it as visited so we don't
                    # visit it again
                    visited.add((row, col))

        # our multi-source bfs function where the goal is to
        # expand outward from each treasure cell, marking
        # distance to adjacent cells on each iteration
        def multi_source_bfs():
            # init our distance to 0
            distance = 0

            # loop as long as there are cells in our queue
            # to loop thorugh
            while queue:
                # increment our distance at each iteration
                distance += 1

                # loop through all cells in our queue
                # since we want to mark the distance for all
                # adjacent cells before incrementing distance
                # on next while loop
                for _ in range(len(queue)):
                    # get the current cell in the queue
                    row, col = queue.popleft()

                    # loop through all possible directions
                    for dx, dy in directions:
                        # get the adjacent cell
                        adjacent_row = row+dx
                        adjacent_col = col+dy

                        # only set the distance for adjacent cell
                        # and add it to the queue, mark as visited if:
                        # 1) the adjacent cell is in grid bounds
                        # 2) the adjacent cell has not been visited before
                        # 3) the adjacent cell does not contain a water cell (-1)
                        if (0 <= adjacent_row < row_len and
                            0 <= adjacent_col < col_len and
                            (adjacent_row, adjacent_col) not in visited and
                            grid[adjacent_row][adjacent_col] != -1):
                            # set the distance for the adjacent cell
                            grid[adjacent_row][adjacent_col] = distance
                            # mark the adjacent cell as visited
                            visited.add((adjacent_row, adjacent_col))
                            # add the adjacent cell to our queue
                            queue.append((adjacent_row, adjacent_col))

        # run our multi source bfs function
        multi_source_bfs()
