#include <vector>
#include <unordered_set>
#include <unordered_map>

/**
 * https://leetcode.com/problems/valid-sudoku/description/
 *
 * Time complexity: O(1) because sudoku is fixed size board
 * Space complexity: O(1) because sudoku is fixed size board
 */
class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        // setup our rowMap to keep track of which numbers exist in rows
        // key = row index, value = set of numbers in that row
        std::unordered_map<int, std::unordered_set<int>> rowMap;
        // setup our colMap to keep track of which numbers exist in cols
        // key = col index, value = set of numbers in that col
        std::unordered_map<int, std::unordered_set<int>> colMap;
        // setup our boxMap to keep track of which numbers exist in each 3x3 box
        // key = flattened (box row, box col) index, value = set of numbers in that 3x3 box
        std::unordered_map<int, std::unordered_set<int>> boxMap;

        // get the row and col lengths
        const int ROW_LEN = board.size();
        const int COL_LEN = board[0].size();

        // loop through all rows
        for (int row{0}; row < ROW_LEN; ++row) {
            // loop through all cols
            for (int col{0}; col < COL_LEN; ++col) {
                // if the board is not occupied by a number, skip it
                if (board[row][col] == '.') {
                    continue;
                }

                // if the rowMap set contains this number
                // we found a duplicate so return false
                if (rowMap[row].contains(board[row][col])) {
                    return false;
                }

                // if the colMap set contains this number
                // we found a duplicate so return false
                if (colMap[col].contains(board[row][col])) {
                    return false;
                }

                // compute the 3x3 box row and box col
                const int boxRow = row / 3;
                const int boxCol = col / 3;

                // compute row major indexing for the box row and box col
                // formula is index = i * total_num_columns + j
                // so we can use an int as our key for boxMap
                const int boxMapKey = boxRow * 3 + boxCol;

                // if the boxMap contains this number
                // we found a duplicate so return false
                if (boxMap[boxMapKey].contains(board[row][col])) {
                    return false;
                }

                // finally, insert the number into each map on each iteration
                rowMap[row].insert(board[row][col]);
                colMap[col].insert(board[row][col]);
                boxMap[boxMapKey].insert(board[row][col]);
            }
        }

        // after checking all numbers and finding no duplicates
        // we can return true
        return true;
    }
};
