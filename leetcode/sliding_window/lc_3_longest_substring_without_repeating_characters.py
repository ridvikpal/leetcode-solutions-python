'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # handle edge case where 
        # we have an empty string
        if not s:
            return 0

        # init our max_length variable
        # to 1 because at the least
        # we can return a substring of 1 char
        max_length = 1

        # init our first pointer that
        # points to the start of a unique
        # substring
        start = 0

        # we will use a set to keep track 
        # of chars we have seen
        # initially add the first char
        # to it
        seen = set([s[0]])

        # we will loop through all indexes
        # after the first index 0
        for end in range(1, len(s)):
            # check if we have seen this char
            # before (i.e., is it in our seen set)
            # if it is, then loop until it is not
            while s[end] in seen:
                # on each iteration, remove the
                # current char pointed too by start
                # pointer from the seen set
                seen.remove(s[start])
                # and move start one index forward
                # this will remove chars until we
                # remove the duplicate, thus keeping
                # a unique substring
                start += 1
            
            # add the char to our set
            # this will do nothing if it already exists
            seen.add(s[end])

            # calculate the substring length
            length = end-start+1
            # and update our max length with it
            max_length = max(length, max_length)

        # finally we will return the max length
        return max_length
