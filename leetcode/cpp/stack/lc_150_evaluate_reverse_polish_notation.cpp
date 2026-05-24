#include <stack>
#include <vector>
#include <string>

/**
 * https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
 *
 * Time complexity: O(n) where n = length of tokens
 * Space complexity: O(n) where n = length of tokens
 */
class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        // init our stack to store our calculations
        std::stack<int> calculations;

        for (const std::string& token: tokens) {
            // if we get an operator token then
            // we can get the first and second nums
            // from our calculations stack
            // perform the operations and put the result
            // back onto the stack
            if (token == "+") {
                int secondNum = calculations.top();
                calculations.pop();
                int firstNum = calculations.top();
                calculations.pop();
                calculations.push(firstNum + secondNum);
            } else if (token == "-") {
                int secondNum = calculations.top();
                calculations.pop();
                int firstNum = calculations.top();
                calculations.pop();
                calculations.push(firstNum - secondNum);
            } else if (token == "*") {
                int secondNum = calculations.top();
                calculations.pop();
                int firstNum = calculations.top();
                calculations.pop();
                calculations.push(firstNum * secondNum);
            } else if (token == "/") {
                int secondNum = calculations.top();
                calculations.pop();
                int firstNum = calculations.top();
                calculations.pop();
                calculations.push(firstNum / secondNum);
            // else if we get a number we can simply add it
            // to the calculations stack
            } else {
                calculations.push(std::stoi(token));
            }
        }

        // finally, we return the last number in our calculations stack
        return calculations.top();
    }
};
