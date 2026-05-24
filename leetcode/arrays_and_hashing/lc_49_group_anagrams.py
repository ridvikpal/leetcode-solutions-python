from collections import defaultdict
from typing import List


'''
https://leetcode.com/problems/group-anagrams/description/
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary to hold each of our anagrams
        # key is count_array (each anagram has same count of characters)
        # value is list of anagrams
        anagrams_dict = defaultdict(list)
        
        # loop through all strings
        for string in strs:
            # create a count array instead of count dict
            # because count arrays can be converted to tuple
            # and used as keys for amagrams_dict
            count_array = [0] * 26
            
            # loop through all characters in the string
            for char in string:
                # for each character, increment the correct
                # index in the count array
                # note that ord(char) - ord('a') will always
                # give us a value between 0 and 25 because
                # we know the string is all lowercase
                count_array[ord(char) - ord('a')] += 1
            
            # convert the count_array into a tuple, set it as key
            # in the anagrams_dict, and append the string to the correct
            # dict key value
            anagrams_dict[tuple(count_array)].append(string)

        # simply return the values of the anagrams dict converted to list
        return list(anagrams_dict.values())
