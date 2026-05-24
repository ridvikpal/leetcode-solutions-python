from collections import defaultdict


'''
https://leetcode.com/problems/valid-anagram/description/
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two strings don't have the same lengths
        # they cannot be anagrams so return False
        if len(s) != len(t):
            return False

        # use a dictionary
        # that maps char -> frequency of char
        # for both counts_s and counts_t
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)

        # loop through all characters in both strings
        # and update their associated dictionary char frequencies
        for i in range(len(s)):
            counts_s[s[i]] += 1
            counts_t[t[i]] += 1

        # if the dicts (char frequencies)
        # are the same, then return true
        return counts_s == counts_t
