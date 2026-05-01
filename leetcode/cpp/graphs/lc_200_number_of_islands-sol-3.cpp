#include <vector>
#include <queue>
#include <array>

/**
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * Time complexity: O(n * m) where n = grid row length, m = grid col length
 * Space complexity: O(n * m) where n = grid row length, m = grid col length
 */
class Solution {
public:
    // create a helper recursive dfs function
    void dfs(
        const std::pair<int, int>& coords,
        std::vector<std::vector<char>>& grid,
        const int& ROW_LEN,
        const int& COL_LEN
    ) {
        // mark this cell as visited by overwriting it with 0
        grid[coords.first][coords.second] = '0';

        // setup the directions we can search in
        const std::array<std::pair<int, int>, 4> directions{{
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1}
        }};

        // loop through all directions
        for (const auto& [dx, dy]: directions) {
            // get the adjacent cell coordinates
            const int adjRow = coords.first+dx, adjCol = coords.second+dy;

            // if
            // 1) the adjacent cell is in grid bounds
            // 2) the adjacent cell contains a 1
            // run dfs recursively on the adjacent cell to visit it
            if (
                (0 <= adjRow && adjRow < ROW_LEN) &&
                (0 <= adjCol && adjCol < COL_LEN) &&
                (grid[adjRow][adjCol] == '1')
            ) {
                dfs(std::make_pair(adjRow, adjCol), grid, ROW_LEN, COL_LEN);
            }
        }
    }

    int numIslands(std::vector<std::vector<char>>& grid) {
        // get the row and column lengths of the grid
        const int ROW_LEN = grid.size();
        const int COL_LEN = grid[0].size();

        // init our count
        int count = 0;

        // loop through all rows
        for (int row{0}; row < ROW_LEN; ++row) {
            // loop through all cols
            for (int col{0}; col < COL_LEN; ++col) {
                // if the cell is 1
                // run dfs on it and increment the count
                if (grid[row][col] == '1') {
                    dfs(std::make_pair(row, col), grid, ROW_LEN, COL_LEN);
                    ++count;
                }
            }
        }

        // finally return the count
        return count;
    }
};
