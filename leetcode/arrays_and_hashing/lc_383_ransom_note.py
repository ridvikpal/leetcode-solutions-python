from collections import Counter


'''
https://leetcode.com/problems/ransom-note/description/
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a dict that maps
        # char -> count of chars for magazine
        # using the Counter class in python
        magazine_counter = Counter(magazine)

        # create a dict that maps
        # char -> count of chars for ransomNote
        # using the Counter class in python
        ransomNote_counter = Counter(ransomNote)

        # only return true if all the chars
        # in the magazine counter are availible
        # in counts >= the required count for the 
        # ransomNote using list comprehension with all()
        return all(
            magazine_counter[char] >= count 
            for char, count in ransomNote_counter.items()
        )
