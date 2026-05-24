from typing import List


'''
https://leetcode.com/problems/word-search/description/
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # first get the dimensions of the board
        row_len = len(board)
        col_len = len(board[0])

        # create our visited set
        # this will be used to ensure we
        # don't keep visiting the same
        # nodes again along a dfs path
        visited = set()

        # setup the directions we can search in
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # our recursive dfs function that will
        # search for paths that match the word
        def dfs(row, col, i) -> bool:
            # our base case is when the function is called
            # with the last character
            if i == len(word)-1:
                # this means the word has been found
                # so return True immediately
                return True

            # add the current (row, col) to the 
            # visited set to prevent it from being visited
            # again in the same path
            visited.add((row, col))

            # loop through all directions to search
            for dx, dy in directions:
                # get the adjacent cell
                adjacent_row = row+dx
                adjacent_col = col+dy

                # only run dfs on adjacent cell if:
                # 1) adjacent cell is within bounds
                # 2) adjacent cell has not been visited before
                #    in the same path
                # 3) adjacent cell contains the next char
                #    in the word
                if (0 <= adjacent_row < row_len and
                    0 <= adjacent_col < col_len and
                    (adjacent_row, adjacent_col) not in visited and
                    board[adjacent_row][adjacent_col] == word[i+1]):
                    # if the dfs function returns true, immediately
                    # return true down the call stack
                    if dfs(adjacent_row, adjacent_col, i+1):
                        return True
                
            # if we get to this part, no valid path
            # from this cell has been found in the word
            # order we were searching
            # but we have to remove this cell from the visited
            # set in case there are words with duplicate chars
            # and we may want to use this cell again in a different
            # order of searching for the word
            visited.remove((row, col))
            # and return False
            return False

        # loop through all rows
        for row in range(row_len):
            # loop through all columns
            for col in range(col_len):
                # only run dfs to search for the word if 
                # the cell contains the first character
                if board[row][col] == word[0]:
                    # run dfs
                    if dfs(row, col, 0):
                        # if dfs returns True
                        # then we can immediately return true
                        return True

        # else if we reach this point
        # we have checked the entire board
        # and not found the word so return False
        return False
