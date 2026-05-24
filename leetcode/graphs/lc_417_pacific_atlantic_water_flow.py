from typing import List


'''
https://leetcode.com/problems/pacific-atlantic-water-flow/description/
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # first get the dimensions of the heights grid
        row_len = len(heights)
        col_len = len(heights[0])

        # then we can setup the 4 directions we can look in for
        # adjacent cells
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # our recursive dfs function that will try to
        # search for paths from each of the borders of
        # the grid to each adjacent cell that has heights
        # >= the previous cell's height
        def dfs(row, col, visited_set):
            # our base case is when we have already visited this
            # cell before
            if (row, col) in visited_set:
                # simply return in this case since we have
                # already visited the cell
                return

            # otherwise we have not visited this cell,
            # so add it to the visited set
            visited_set.add((row, col))

            # loop through all the directions
            # we can search for adjacent cells in
            for dx, dy in directions:
                # calculate the adjacent cell dimensions
                adjacent_row, adjacent_col = row+dx, col+dy

                # only perform recursive dfs on the adjacent cell if:
                # 1) the adjacent cell is in the bounds of the grid
                # 2) the adjacent cell height >= base cell height
                #    we do >= instead of <= because we are searching from
                #    the ocean to the cell, not the other way around
                if (0 <= adjacent_row < row_len and
                    0 <= adjacent_col < col_len and
                    heights[adjacent_row][adjacent_col] >= heights[row][col]):
                    # perform recursive dfs on the adjacent cell
                    dfs(adjacent_row, adjacent_col, visited_set)

        # setup our visited set that tracks
        # all cells that can be visited from the pacific ocean
        pacific_visited_set = set()
        # setup our visited set that tracks
        # all cells that can be visited from the atlantic ocean
        atlantic_visited_set = set()

        # loop through all rows
        for row in range(row_len):
            # perform dfs for each cell bordering the left pacific ocean
            dfs(row, 0, pacific_visited_set)
            # perform dfs for each cell bordering the right atlantic ocean
            dfs(row, col_len-1, atlantic_visited_set)
        
        # loop through all columns
        for col in range(col_len):
            # perform dfs for each cell bordering the top pacific ocean
            dfs(0, col, pacific_visited_set)
            # perform dfs for each cell bordering the bottom atlantic ocean
            dfs(row_len-1, col, atlantic_visited_set)

        # return a list of the intersection between
        # the cells that can be visited from the pacific ocean
        # and the cells that can be visited from the atlantic ocean
        # these are the cells that can visit both oceans
        return list(pacific_visited_set.intersection(atlantic_visited_set))
