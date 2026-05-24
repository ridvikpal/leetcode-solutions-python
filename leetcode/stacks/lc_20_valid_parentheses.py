'''
https://leetcode.com/problems/valid-parentheses/description/
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # create a dict that maps
        # close bracket to open bracket
        close_to_open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # create our bracket stack
        # this stack will be used to
        # add open brackets to
        bracket_stack = []

        # loop through all characters in s
        for char in s:
            # if the character is an open bracket
            if char not in close_to_open:
                # then append to the bracket stack
                bracket_stack.append(char)
            # else the character is a close bracket
            else:
                # if the bracket stack is empty
                # meaning there is no open bracket
                # left to close, then we have an error
                if not bracket_stack:
                    # so return False
                    return False

                # so get the top bracket from the stack
                top_bracket = bracket_stack.pop()

                # if the top bracket does not match this
                # close bracket, then we have an error
                if top_bracket != close_to_open[char]:
                    # so return False
                    return False
        
        # at the very end, we want the bracket stack
        # to be empty, so only return True if it's empty
        return not bracket_stack
