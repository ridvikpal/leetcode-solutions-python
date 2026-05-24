from collections import Counter


'''
https://leetcode.com/problems/valid-anagram/description/
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two strings don't have the same lengths
        # they cannot be anagrams so return False
        if len(s) != len(t):
            return False

        # use a counter to create a dict
        # that maps char -> frequency of char
        # for both counts_s and counts_t
        # note we could also create the counter
        # manually, but python provides an easy
        # implementation
        counts_s = Counter(s)
        counts_t = Counter(t)

        # if the dicts (char frequencies)
        # are the same, then return true
        return counts_s == counts_t
