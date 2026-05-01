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
    // create a helper bfs function
    void bfs(
        const std::pair<int, int>& coords,
        std::vector<std::vector<char>>& grid,
        const int& ROW_LEN,
        const int& COL_LEN
    ) {
        // setup our bfs queue
        std::queue<std::pair<int, int>> bfsQueue;
        // add the current coordinate to the bfs queue
        bfsQueue.push(coords);
        // overwrite this cell with '0' to mark it as visited
        grid[coords.first][coords.second] = '0';

        // setup our directions to search in
        const std::array<std::pair<int, int>, 4> directions{{
            {-1, 0},
            {1, 0},
            {0, 1},
            {0, -1}
        }};

        // standard bfs loop until empty
        while (!bfsQueue.empty()) {
            // get the first element from the bfs queue
            const auto [row, col] = bfsQueue.front();
            // remove the first element from the bfs queue
            bfsQueue.pop();

            // loop through all the directions
            for (const auto& [dx, dy]: directions) {
                // get the adjacent cell coordinates
                int adjRow = row+dx, adjCol = col+dy;

                // if:
                // 1) the adjacent cell is within grid bounds
                // 3) the adjacent cell contains a 1
                // then add it to the bfs queue
                // and overwrite with '0' to mark it as visited
                if (
                    (0 <= adjRow && adjRow < ROW_LEN) &&
                    (0 <= adjCol && adjCol < COL_LEN) &&
                    (grid[adjRow][adjCol] == '1')
                ) {
                    bfsQueue.push(std::make_pair(adjRow, adjCol));
                    grid[adjRow][adjCol] = '0';
                }
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
                // run bfs on it and increment the count
                if (grid[row][col] == '1') {
                    bfs(std::make_pair(row, col), grid, ROW_LEN, COL_LEN);
                    ++count;
                }
            }
        }

        // finally return the count
        return count;
    }
};
