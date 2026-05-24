#include <stack>
#include <string>

/**
 * https://leetcode.com/problems/valid-parentheses/description/
 *
 * Time complexity: O(n) where n = length of s
 * Space complexity: O(n) where n = length of s
 */
class Solution {
public:
    bool isValid(std::string s) {
        // if there are less than 2 chars in s
        // automatically valid parentheses cannot be possible
        // so return false
        if (s.size() < 2) {
            return false;
        }

        // setup our stack
        std::stack<char> stringStack;

        // loop through all characters in s
        for (const char& chr: s) {
            // for every closing bracket, return false if any of the following:
            // 1) the correct closing bracket doesn't exist at the top of the stack
            // 2) the stack is empty
            // otherwise continue and add every opening bracket to the stack
            switch(chr) {
                case ')':
                    if (stringStack.empty() || stringStack.top() != '(') {
                        return false;
                    }
                    stringStack.pop();
                    break;
                case ']':
                    if (stringStack.empty() || stringStack.top() != '[') {
                        return false;
                    }
                    stringStack.pop();
                    break;
                case '}':
                    if (stringStack.empty() || stringStack.top() != '{') {
                        return false;
                    }
                    stringStack.pop();
                    break;
                default:
                    stringStack.push(chr);
                    break;
            }
        }

        // at the end, make sure that the stack is empty
        // so all opening brackets have been closed
        // and then return true else false
        return stringStack.empty();
    }
};
