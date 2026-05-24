'''
https://leetcode.com/problems/roman-to-integer/description/
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        # first create a dictionary that maps
        # roman numerals to integers
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # we will store the previous character
        # which by default will be the first char in s
        previous_char = s[0]
        # we will init our integer sum with
        # the previous char's int value
        int_sum = roman_dict[previous_char]
        # loop through all indices in s skipping
        # the first one
        for i in range(1, len(s)):
            # get the current char at this index
            char = s[i]

            # first check if the char is V or X
            if char == 'V' or char == 'X':
                # then check if the previous char is also I
                if previous_char == 'I':
                    # in this case, we want to subtract
                    # I's int value twice
                    # once for removing it on the previous iteration
                    # and second for subtracting it's value from V or X
                    int_sum -= 2 * roman_dict['I']
            # second check if the char is L or C
            elif char == 'L' or char == 'C':
                # then check if the previous char is also X
                if previous_char == 'X':
                    # in this case, we want to subtract
                    # X's int value twice
                    # once for removing it on the previous iteration
                    # and second for subtracting it's value from L or C
                    int_sum -= 2 * roman_dict['X']
            # third check if the char is D or M
            elif char == 'D' or char == 'M':
                # then check if the previous char is also C
                if previous_char == 'C':
                    # in this case, we want to subtract
                    # C's int value twice
                    # once for removing it on the previous iteration
                    # and second for subtracting it's value from D or M
                    int_sum -= 2 * roman_dict['C']

            # finally, add the current char's int value to
            # the int sum
            int_sum += roman_dict[char]
            # and update the previous character to this character
            previous_char = char

        # return the final int sum
        return int_sum
