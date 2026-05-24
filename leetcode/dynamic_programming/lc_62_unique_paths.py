'''
https://leetcode.com/problems/unique-paths/description/
'''
class Solution:
    # we will use a bottom up dynamic programming approach
    def uniquePaths(self, m: int, n: int) -> int:
        # init our dynamic programming 2d array
        # which is a clone of the graph with all cells 0
        # this unique paths array will hold the total number
        # of unique paths to reach any cell
        unique_paths = [[0 for _ in range(n)] for _ in range(m)]
        
        # our first base case is every column in the first row
        # because the robot can only go to the right and not left
        # the only way to reach these cells is 1 way:
        # the robot going right
        # for the initial starting point, we assume the only way
        # to reach that starting point is 1 because the robot is placed there
        for col in range(n):
            unique_paths[0][col] = 1

        # our second base case is every row in the first column
        # because the robot can only go to the down and not up
        # the only way to reach these cells is 1 way:
        # the robot going down
        # for the initial starting point, we assume the only way
        # to reach that starting point is 1 because the robot is placed there
        for row in range(m):
            unique_paths[row][0] = 1
        
        # now we can loop through all rows
        # skipping the first row
        for row in range(1, m):
            # and loop through all columns
            # skipping the first col
            for col in range(1, n):
                # and update the unique paths for that (row, col) as being
                # the sum of the unique paths above it and to the left of it
                # these are the only two directions the robot cannot travel in
                unique_paths[row][col] = unique_paths[row-1][col] + unique_paths[row][col-1]

        # finally, we will return the number of unique paths
        # to reach the final bottom right cell
        return unique_paths[-1][-1]
