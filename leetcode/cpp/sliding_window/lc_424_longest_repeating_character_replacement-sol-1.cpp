#include <string>
#include <array>
#include <algorithm>

/**
 * https://leetcode.com/problems/longest-repeating-character-replacement/description/
 *
 * Time complexity: O(n) where n = length of s
 * Space complexity: O(1)
 */
class Solution {
public:
    int characterReplacement(std::string s, int k) {
        // init our seen array
        // index = character as int beginning with 'A' = 0
        // value = count of character in our sliding substring window
        std::array<int, 26> seen{};

        // our max length is init as 1, because in the worst case scenario
        // our largest substring is of length 1
        int maxLength = 1;

        // our start pointer for the sliding window, init to 0
        int i = 0;
        // increment the first char's count to our seen array
        ++seen[static_cast<int>(s[i])-static_cast<int>('A')];

        // loop through all chars in string s except for the first one
        // incrementing our sliding window to the right each time
        // j is the end pointer for our sliding window
        for (int j = 1; j < s.size(); ++j) {
            // increment the seen array with the next char's count
            ++seen[static_cast<int>(s[j])-static_cast<int>('A')];

            // get the length of our substring (sliding window)
            int length = j-i+1;

            // get the max char count from our seen array
            int maxCharCount = *std::max_element(seen.begin(), seen.end());

            // as long as we cannot replace more than k other chars in our window
            // then we don't have an optimal substring, so then we need to shrink our
            // substring (sliding window) from the start
            while (length - maxCharCount > k) {
                // decrement the char count for the start of our sliding window
                // since we will be moving our sliding window forwards
                --seen[static_cast<int>(s[i])-static_cast<int>('A')];
                // move the sliding window forward
                ++i;
                // decrement the length of our substring
                --length;

                // get the new max char count
                maxCharCount = *std::max_element(seen.begin(), seen.end());
            }

            // update the max length we have stored
            maxLength = std::max(length, maxLength);
        }

        // finally, return the max length we found
        return maxLength;
    }
};
