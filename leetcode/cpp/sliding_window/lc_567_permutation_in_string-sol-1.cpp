#include <string>
#include <array>

/**
 * https://leetcode.com/problems/permutation-in-string/description/
 *
 * Time complexity: O(n) where n = length of string s
 * Space complexity: O(1)
 *
 */
class Solution {
public:
    bool checkInclusion(std::string s1, std::string s2) {
        // first handle the edge case where the length of s1
        // is greater than the length of s2
        // automatically, a substring is not possible so return false
        if (s1.size() > s2.size()) {
            return false;
        }

        // init our counter array for the first s1 string
        std::array<int, 26> s1Counter{};

        // count the frequency of all characters for the first s1 string
        for (const char& chr: s1) {
            ++s1Counter[static_cast<int>(chr)-static_cast<int>('a')];
        }

        // init our counter array for the second s2 string
        std::array<int, 26> s2SlidingCounter{};

        // init our left side pointer for the sliding window
        int i = 0;

        // loop through all characters
        // the right side of our sliding window will keep increasing
        for (const char& chr: s2) {
            // increment the s2 sliding counter char count for the right of the sliding window
            ++s2SlidingCounter[static_cast<int>(chr)-static_cast<int>('a')];

            // if the s2 sliding counter array equals the s1 counter array
            // then we can return true because we found a permutation
            if (s2SlidingCounter == s1Counter) {
                return true;
            }

            // if the s2 sliding window count for a specific character is larger than the count
            // for the same character in the s1 counter, then we have to move the left
            // side of the sliding window forward
            while (
                s2SlidingCounter[static_cast<int>(chr)-static_cast<int>('a')] > s1Counter[static_cast<int>(chr)-static_cast<int>('a')]
            ) {
                // decrement the s2 sliding counter char for the left side pointer of the sliding window
                --s2SlidingCounter[static_cast<int>(s2[i])-static_cast<int>('a')];
                // move the left side pointer forwards
                ++i;
            }
        }

        // finally, if we have checked all chars in both strings and not found a permutation
        // then we can return false
        return false;
    }
};
