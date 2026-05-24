import heapq
from typing import List


'''
https://leetcode.com/problems/swim-in-rising-water/description/
'''
class Solution:
    # we will use a modified version of Dijkstra's algorithm
    # here without a cost array because we have a fixed cost
    # in the form of the grid values
    # basically it is a greedy approach: choose closest adjacent
    # cell with the smallest value until we reach the bottom right cell
    def swimInWater(self, grid: List[List[int]]) -> int:
        # first get the dimensions of our grid
        row_len = len(grid)
        col_len = len(grid[0])
        
        # setup the directions we can travel in
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        # init our heap (priority queue) for Dijkstra's algorithm
        # with the top left grid coordinates and value
        # this heap will hold tuples of the form:
        # (grid_elevation, row, coord)
        heap = [(grid[0][0], 0, 0)]
        # setup our visited set to prevent visiting cells again
        # with our top left coordinate since that's where we start
        visited = {(0, 0)}
    
        # init our max time to reach the bottom right square
        # as the current top left grid elevation since that's our starting point
        max_time = grid[0][0]

        # standard Dijkstra algorithm loop as long as there are
        # elements in the queue
        while heap:
            # pop the element from the heap with the least elevation
            current_elevation, row, col = heapq.heappop(heap)

            # set the max time as the max of the current elevation
            # or the saved time since we can swim to any cell with elevation
            # <= the max time 
            max_time = max(current_elevation, max_time)

            # check if we have reached the bottom right cell
            if row == row_len-1 and col == col_len-1:
                # if we have, just return the max time
                return max_time

            # otherwise loop through all directions we can search in
            for dx, dy in directions:
                # get the adjacent cell
                adj_row, adj_col = row+dx, col+dy

                # only add to the heap if:
                # 1) the adjacent cell is within grid bounds
                # 2) we have not visited this adjacent cell before
                if (0 <= adj_row < row_len and
                    0 <= adj_col < col_len and
                    (adj_row, adj_col) not in visited):
                    # add the adjacent cell to the heap with the weight
                    # being the value of the adjacent cell grid elevation
                    heapq.heappush(heap, (grid[adj_row][adj_col], adj_row, adj_col))
                    # mark the adjacent cell as visited
                    visited.add((adj_row, adj_col))
