#include <stack>

/**
 * https://leetcode.com/problems/min-stack/description/
 *
 * Time complexity: O(1) for all functions
 * Space complexity: O(n) where n = number of variables inserted into MinStack
 */
class MinStack {
public:
    // first define our stacks
    // the first is a regular stack
    std::stack<int> regularStack;
    // the second is a monotonic decreasing stack
    // so the top element is the smallest value out
    // of all elements defined in the regularStack
    std::stack<int> minStack;

    MinStack() {

    }

    void push(int val) {
        // we can directly push onto the regular stack
        regularStack.push(val);

        // if we don't have any values in our min stack
        // or the value we are adding is smaller than the
        // current smallest value, then we will also directly
        // push onto the min stack
        if (minStack.size() == 0 || val < minStack.top()) {
            minStack.push(val);
        // otherwise, we will continue to use the previous min value
        // and push that onto the min stack
        } else {
            minStack.push(minStack.top());
        }
    }

    // for both regular and min stacks, we can pop from them
    // normally, as long as they have an element in them
    void pop() {
        if (regularStack.size() > 0) {
            regularStack.pop();
        }
        if (minStack.size() > 0) {
            minStack.pop();
        }
    }

    // we can simply return the top value of ther regular stack
    int top() {
        return regularStack.top();
    }

    // we can simply return the top value of the min stack
    int getMin() {
        return minStack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
