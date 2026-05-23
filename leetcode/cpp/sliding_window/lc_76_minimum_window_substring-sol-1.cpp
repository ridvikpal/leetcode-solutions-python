#include <unordered_map>
#include <string>
#include <cmath>

/**
 * https://leetcode.com/problems/minimum-window-substring/description/
 *
 * Time complexity: O(n * m) where n = length of s and m = length of t
 * Space complexity: O(1)
 */
class Solution {
public:
    // we will create a helper function to determine if a substing is valid
    // the inner string counter is the hashmap counter for the desired inner string
    // the outer string counter is the hashmap counter for the given outer string
    bool isValidSubstring(
        std::unordered_map<char, int>& innerStringCounter,
        std::unordered_map<char, int>& outerStringCounter
    ) {
        // loop through all chars and their frequencies for the desired inner string
        for (const auto& pair: innerStringCounter) {
            // check if the inner string char is found with insufficient frequency
            // in the outer string, then we have an invalid substring
            // so set the is valid flag to return false
            if (pair.second > outerStringCounter[pair.first]) {
                return false;
            }
        }

        // otherwise the substring is valid, so return true
        return true;
    }

    std::string minWindow(std::string s, std::string t) {
        // handle the edge case where t has more chars than s
        // in which case a valid substring is not possible so
        // we can return "" immediately
        if (t.size() > s.size()) {
            return "";
        }

        // setup the t counter hashmap and populate it
        // with the char frequencies of the t string
        std::unordered_map<char, int> tCounter;
        for (const char& chr: t) {
            ++tCounter[chr];
        }

        // setup the counter hashmap for our sliding window in the s string
        std::unordered_map<char, int> sSlidingCounter;
        // setup the start pointer for our sliding window
        int i = 0;

        // store the optimal start (left) pointer for the sliding window and the minimum length
        // this is so we can create a substring at the end of the function
        // rather than creating and storing a substring every time
        // a new optimal substring is found
        int optimalI = 0;
        int minLength = std::pow(10, 5)+1;

        // loop through all end (right) pointers for our sliding window
        for (int j = 0; j < s.size(); ++j) {
            // increment the end pointer counter
            ++sSlidingCounter[s[j]];

            // determine if a valid substring has been found using our helper function
            bool validSubstringFound = isValidSubstring(tCounter, sSlidingCounter);

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
                // move the start pointer forward
                ++i;
                // check if the new substring is valid or not
                validSubstringFound = isValidSubstring(tCounter, sSlidingCounter);
            }
        }

        // finally, return the minimum window substring only if it was updated
        return minLength == std::pow(10, 5)+1 ? "" : s.substr(optimalI, minLength);
    }
};
