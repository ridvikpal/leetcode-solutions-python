from collections import deque
from typing import List


'''
https://leetcode.com/problems/rotting-oranges/description/
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first get the dimensions of the grid
        row_len = len(grid)
        col_len = len(grid[0])
        
        # create a count for the total
        # number of each type of fruit
        rotten_count = 0
        fresh_count = 0

        # we will be using multi-source bfs
        # so we need to init our queue
        queue = deque()

        # loop through all rows
        for row in range(row_len):
            # and all columns
            for col in range(col_len):
                # check if the cell is a fresh fruit
                if grid[row][col] == 1:
                    # if it is, increment
                    # the fresh fruit count
                    fresh_count += 1
                # else check if the cell is a rotten fruit
                elif grid[row][col] == 2:
                    # if it is, increment
                    # the rotten fruit count
                    rotten_count += 1
                    # and add it to our queue
                    # since we will do multi-source bfs
                    # starting from the rotten fruit
                    queue.append((row, col))
        
        # first check if there are no fresh fruit
        # but some or no rotten fruit
        if fresh_count == 0 and rotten_count >= 0:
            # in this edge case, return 0
            # since all fruit is rotten if it exists
            return 0

        # second check if there are fresh fruit
        # but no rotten fruit
        if fresh_count > 0 and rotten_count == 0:
            # in this edge case, return -1
            # because all fruit will stay fresh
            # and cannot go rotten
            return -1

        # setup our directions we can search
        # for adjacent fruits in
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # init our time to 0
        time = 0

        # standard bfs while loop as long as there are
        # elements in the queue
        while queue:
            # setup a flag used to track
            # whether a fresh fruit was changed or not
            fresh_fruit_changed = False

            # loop through all elements in the queue
            # since we are doing layer-by-layer
            # multi-source bfs
            for _ in range(len(queue)):
                # get the first cell in the queue
                r, c = queue.popleft()

                # loop through all adjacent directions
                for dx, dy in directions:
                    # calculate the adjacent row and adjacent col
                    adjacent_row, adjacent_col = r+dx, c+dy


                    # only add the adjacent cell to the queue if
                    # 1) the adjacent cell is within the bounds of the grid
                    # 2) the adjacent cell contains a fresh fruit
                    if (0 <= adjacent_row < row_len and
                        0 <= adjacent_col < col_len and
                        grid[adjacent_row][adjacent_col] == 1):

                        # change the adjacent fresh fruit to a rotten fruit
                        grid[adjacent_row][adjacent_col] = 2
                        # toggle our fresh_fruit_changed flag to True
                        fresh_fruit_changed = True
                        # decrement our fresh fruit count
                        fresh_count -= 1
                        # increment our rotten fruit count
                        rotten_count += 1
                        # add the adjacent cell the queue
                        # since the adjacent cell is now a rotten fruit
                        queue.append((adjacent_row, adjacent_col))
            
            # if the fresh fruit has changed,
            if fresh_fruit_changed:
                # only then increment the time
                time += 1

        # finally return the time only if there
        # are no fresh fruit otherwise return -1
        # because all fresh fruit was not converted
        # to rotten fruit
        return time if fresh_count == 0 else -1
