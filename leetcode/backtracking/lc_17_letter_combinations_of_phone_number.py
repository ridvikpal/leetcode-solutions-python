from typing import List


'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # handle edge case where digits is an empty string
        if not digits:
            return []
        
        # initialize our dictionary that maps
        # each digit to a tuple of possible characters
        dictionary = {
            '2': ('a', 'b' , 'c'),
            '3': ('d', 'e' , 'f'),
            '4': ('g', 'h' , 'i'),
            '5': ('j', 'k' , 'l'),
            '6': ('m', 'n' , 'o'),
            '7': ('p', 'q' , 'r', 's'),
            '8': ('t' , 'u', 'v'),
            '9': ('w', 'x' , 'y', 'z'),
        }

        # create our results list to hold final result
        result = []
        # create our subset list to hold each possible
        # character combination
        subset = []

        # create our dfs search function to search through 
        # all possible character combinations
        def search(index):
            # our base case is when our index is out of bounds
            if index >= len(digits):
                # in this case, we append the string of 
                # character combinations to the results list
                result.append("".join(subset))
                # and return immeidately
                return

            # loop through all posssible characters in the
            # dictionary lookup for this digit
            for char in dictionary[digits[index]]:
                # first test with adding that character
                subset.append(char)
                # recursively search on next number (at next index)
                search(index+1)
                # remove the character for cleanup
                # so we can try the next character
                # on the next iteration
                subset.pop()

        # begin searching at index 0 (first digit)
        search(0)

        # return the result list
        return result
