#include <vector>
#include <queue>
#include <array>

/**
 * https://neetcode.io/problems/islands-and-treasure/question
 *
 * Time complexity: O(n * m) where n = grid row length, m = grid col length
 * Space complexity: O(n * m) where n = grid row length, m = grid col length
 */
class Solution {
public:
    void islandsAndTreasure(std::vector<std::vector<int>>& grid) {
        // first define the possible states of a grid cell
        const int TREASURE_CHEST = 0;
        const int WATER = -1;

        // get the row and column length of the grid
        int rowLen = grid.size();
        int colLen = grid[0].size();

        // setup our bfs queue
        std::queue<std::pair<int, int>> bfsQueue;
        // setup our visited 2d array
        // we use the 2d array because cpp doesn't natively support hashing
        // pairs or tuples for an unordered set
        std::vector<std::vector<bool>> visited(rowLen, std::vector<bool>(colLen));

        // loop through all rows
        for (int row{0}; row < rowLen; ++row) {
            // loop through all columns
            for (int col{0}; col < colLen; ++col) {
                // if the cell is a treasure chest
                // then add it to our queue
                if (grid[row][col] == TREASURE_CHEST) {
                    bfsQueue.push(std::make_pair(row, col));
                    visited[row][col] = true;
                }
            }
        }

        // setup the directions we can search in
        std::array<std::pair<int, int>, 4> directions{{
            {-1, 0},
            {1, 0},
            {0, -1},
            {0, 1}
        }};

        // init our distance from neighbouring
        // treasure chests to 0
        int distance = 0;

        // loop as long as the bfs queue is not empty
        while (!bfsQueue.empty()) {
            // increment the distance for each layer
            // of the bfs search
            ++distance;

            // get the number of cells in the bfs queue
            int numCellsInBfsQueue = bfsQueue.size();

            // loop through all cells in the bfs queue
            for (int i{0}; i < numCellsInBfsQueue; ++i) {
                // get the first cell in the bfs queue
                const auto [row, col] = bfsQueue.front();
                // remove the first cell in the bfs queue after getting it
                bfsQueue.pop();

                // loop through all directions
                for (const auto& [dx, dy]: directions) {
                    // compute the adjacent cell coordinates
                    int adjRow = row+dx;
                    int adjCol = col+dy;

                    // if:
                    // 1) the adjacent cell is within the grid bounds
                    // 2) the adjacent cell is a land cell
                    // then add the adjacent cell to the bfs queue
                    // and update the adjacent cell's distance
                    // and mark the cell as visited
                    if ((0 <= adjRow && adjRow < rowLen) &&
                        (0 <= adjCol && adjCol < colLen) &&
                        (grid[adjRow][adjCol] != WATER) &&
                        (!visited[adjRow][adjCol])) {
                            bfsQueue.push(std::make_pair(adjRow, adjCol));
                            visited[adjRow][adjCol] = true;
                            grid[adjRow][adjCol] = distance;
                        }
                }
            }
        }
    }
};
