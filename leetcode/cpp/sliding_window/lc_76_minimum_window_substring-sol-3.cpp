#include <array>
#include <string>
#include <cmath>

/**
 * https://leetcode.com/problems/minimum-window-substring/description/
 *
 * Time complexity: O(n + m) where n = length of s and m = length of t
 * Space complexity: O(1)
 */
class Solution {
public:
    std::string minWindow(std::string s, std::string t) {
        // handle the edge case where t has more chars than s
        // in which case a valid substring is not possible so
        // we can return "" immediately
        if (t.size() > s.size()) {
            return "";
        }

        // keep track of the number of unique characters in t
        // this will be used later on to determine if we have a valid substring
        int uniqueTChars = 0;
        // setup the t counter array and populate it
        // with the char frequencies of the t string
        // we use a size of 128 because most common ascii chars range from 0-127 in cpp
        std::array<int, 128> tCounter{};
        for (const char& chr: t) {
            // increment the unique t chars count if we have not seen this number before
            if (tCounter[chr] == 0) {
                ++uniqueTChars;
            }

            ++tCounter[chr];
        }

        // setup the counter array for our sliding window in the s string
        std::array<int, 128> sSlidingCounter{};
        // setup the start pointer for our sliding window
        int i = 0;

        // store the optimal start (left) pointer for the sliding window and the minimum length
        // this is so we can create a substring at the end of the function
        // rather than creating and storing a substring every time
        // a new optimal substring is found
        int optimalI = 0;
        int minLength = std::pow(10, 5)+1;

        // store the count of unique substring chars found in s
        // from t required to make it valid
        int validSubstringChars = 0;

        // loop through all end (right) pointers for our sliding window
        for (int j = 0; j < s.size(); ++j) {
            // increment the end pointer counter
            ++sSlidingCounter[s[j]];

            // if t contains the char at end pointer
            // and we have the right frequency of the char at end pointer in s
            // then we have a new unique valid substring char
            // so increment the valid substring chars count
            if (tCounter[s[j]] > 0 && sSlidingCounter[s[j]] == tCounter[s[j]]) {
                ++validSubstringChars;
            }

            // determine if a valid substring has been found by checking if we have all the required unique chars at the right frequencies in our sliding window substring
            bool validSubstringFound = validSubstringChars == uniqueTChars;

            // as long as a valid substring keeps being found
            // we will keep reducing the substring from the left (start)
            while (validSubstringFound) {
                // determine the length of the substring
                int length = j-i+1;
                // if the length is better than the stored minimum length
                // then update our optimal start pointer and minimum length accordingly
                if (length < minLength) {
                    optimalI = i;
                    minLength = length;
                }

                // test another smaller substring to see if it is also valid
                // by shrinking the substring
                // decrement the start pointer counter
                --sSlidingCounter[s[i]];

                // if t contains the char at end pointer
                // and we don't have the right frequency (less frequency) of the char at end pointer in s
                // then we don't have a unique valid substring char anymore
                // so decrement the valid substring chars count
                if (tCounter[s[i]] > 0 && sSlidingCounter[s[i]] < tCounter[s[i]]) {
                    --validSubstringChars;
                }

                // move the start pointer forward
                ++i;
                // check if the new substring is valid or not
                validSubstringFound = validSubstringChars == uniqueTChars;
            }
        }

        // finally, return the minimum window substring only if it was updated
        return minLength == std::pow(10, 5)+1 ? "" : s.substr(optimalI, minLength);
    }
};
