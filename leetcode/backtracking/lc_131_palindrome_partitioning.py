from typing import List


'''
https://leetcode.com/problems/palindrome-partitioning/description/
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # define a helper function to help us check 
        # if a string list is a palindrome or not
        # we will use a standard two pointer approach
        def isPalindrome(input_list: list[str]) -> bool:
            # init first pointer i
            # to point to the start of the list
            i = 0
            # init second pointer j
            # to point to the end of the list
            j = len(input_list)-1

            # loop until the two pointers cross
            while i < j:
                # if the 2 pointers on opposite ends
                # do not point to the same char
                if input_list[i] != input_list[j]:
                    # then return false because the 
                    # string is not a palindrome
                    return False
                
                # increment pointer i
                i += 1
                # decrement pointer j
                j -= 1

            # if we can iterate through the entire list
            # then we know this is a palindrome so return True
            return True


        # create our result list to hold our final result
        result = []
        # create our partition list to hold the valid palindrome
        # partitions of our input string
        partition = []

        def search(index):
            # our base case is when we are out of bounds
            # and have gone through the entire input string
            if index >= len(s):
                # in this case, we know that we have a valid
                # partition, so add it to the result
                result.append(partition.copy())
                # and return
                return

            # loop through all indices after and including 
            # the starting index passed into search()
            # to test out different end indexes
            for end_index in range(index, len(s)):
                # Get the first partition to test
                # from starting index to the end index
                test_partition = s[index:end_index+1]
                
                # if this partition is a palindrome
                # only then do we search for other palindromes
                # after it
                if isPalindrome(test_partition):
                    # then we add it to our result list
                    partition.append(test_partition)
                    # search on the next index afer this valid partition
                    search(end_index+1)
                    # after backtracking, pop the partition just tested
                    # so we can run a new parititon on the next iteration
                    partition.pop()

        # begin searching at index 0
        search(0)

        # return the result list, populated by our search() function
        return result
