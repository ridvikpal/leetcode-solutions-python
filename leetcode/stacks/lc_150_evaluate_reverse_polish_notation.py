from typing import List


'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a set of the operands 
        # that can be in the tokens array
        operands = {'+', '-', '*', '/'}
        
        # init our stack
        stack = []

        # loop through all tokens
        for token in tokens:
            # check if the token is an operand
            if (token in operands):
                # get the second number from the stack
                second_num = stack.pop()
                # get the first number from the stack
                first_num = stack.pop()

                # create the math expression we want to evaluate
                math_expression = f"{first_num} {token} {second_num}"
                # calculate the math expression using eval()
                calculation = eval(math_expression)
                
                # add the calculation back to the stack
                # use int() to truncate towards 0
                stack.append(int(calculation))

            # else the token must be a number
            else:
                # add the number to the stack
                # use int() to handle the edge case
                # where we are given a single number
                # and don't want to return a string number
                stack.append(int(token))
        
        # return the final number in the stack
        # after all calculations are complete
        return stack[-1]
