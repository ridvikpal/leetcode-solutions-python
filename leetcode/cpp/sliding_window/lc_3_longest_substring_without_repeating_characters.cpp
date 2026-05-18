#include <string>
#include <unordered_set>

/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * Time complexity: O(n) where n = length of s
 * Space complexity: O(n) where n = length of s
 */
class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        // first handle the edge case if we are given
        // a string with less than 2 chars
        // simply return it's size
        if (s.size() < 2) {
            return s.size();
        }

        // create our seen set to keep track of the unique
        // chars in the substring (our sliding window)
        std::unordered_set<char> seen;

        // init the max length we found so ar
        int maxLength = 0;
        // init the start index i of our sliding window
        int i = 0;

        // loop through all the chars in the string
        for (const char& chr: s) {
            // as long as we have seen this char before
            // keep removing it from our seen set
            // and increment the start of our sliding window
            // until we no longer have this char in our seen set
            while (seen.contains(chr)){
                seen.erase(s[i]);
                ++i;
            }
            // finally, insert the current char into our seen set
            seen.insert(chr);

            // keep track of the max length of our seen set
            // which is our substring
            maxLength = std::max(static_cast<int>(seen.size()), maxLength);
        }

        // finally, return the max length we have stored so far.
        return maxLength;
    }
};
