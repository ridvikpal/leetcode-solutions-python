'''
https://leetcode.com/problems/min-stack/description/
'''
class MinStack:

    def __init__(self):
        # init our regular stack
        self.stack = []
        # init our min_stack
        # the top of this stack will
        # always contain the smallest value
        # because we will insert only 
        # smaller values than the top into it
        self.min_stack = []

    def push(self, val: int) -> None:
        # add the value to our regular stack
        self.stack.append(val)

        # if we have an empty min stack
        # or if the new value is smaller
        # than the top of the min stack, then append
        # to the min stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        # else the new value > top of min stack
        else:
            # then get the current top value
            top = self.min_stack[-1]
            # and readd the top value
            # to maintain len(min_stack) = len(stack)
            # and the property that the top
            # of the min stack is always the smallest value
            self.min_stack.append(top)

    def pop(self) -> None:
        # remove the top element from main stack
        self.stack.pop()
        # remove the top element from the min stack
        self.min_stack.pop()

    def top(self) -> int:
        # return the top of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return the top of the min stack
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
