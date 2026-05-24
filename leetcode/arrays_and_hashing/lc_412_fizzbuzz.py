from typing import List


'''
https://leetcode.com/problems/fizz-buzz/description/
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # setup our final result array to return
        result = []
        
        # loop through all numbers [0, n)
        for i in range(n):
            # the numbers are 1-indexed
            # so increment the 0-index by 1
            # and store it in our num variable
            num = i+1

            # check if the num is not divisible
            # by 3 or 5
            if num % 3 != 0 and num % 5 != 0:
                # if so we just add the string
                # version of the num
                result.append(str(num))
                # and go to the next number
                continue

            # otherwise, we know the number is
            # at least divisible by either 3 or 5
            # init our string variable
            string = ''
            # check if number is divisible by 3
            if num % 3 == 0:
                # if it is, add Fizz to the string
                string += "Fizz"
            # check if the number is divisible by 5
            if num % 5 == 0:
                # if it is, add Buzz to the string
                string += "Buzz"
            # finally add the string to the result array
            result.append(string)

        # return the result array
        return result
