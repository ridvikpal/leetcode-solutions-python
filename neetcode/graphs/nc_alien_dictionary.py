from typing import List


'''
https://neetcode.io/problems/foreign-dictionary/question
'''
class Solution:
    # we will use topological sort with post-order dfs
    # and then path reversal to solve this problem
    def foreignDictionary(self, words: List[str]) -> str:
        # first we must construct a graph using the chars
        # in the words given to us
        # we can init an adjacency set for all the chars
        # note we use an adjacency set instead of an adjacency list
        # because as we add chars to the adjacency list, there could be
        # duplicate chars, and we want to avoid adding them
        adjacency_set = {char: set() for word in words for char in word}

        # loop through all indices for words except for the last one
        # because we will be looking at two words at a time
        for i in range(len(words)-1):
            # get the first and second words
            first_word, second_word = words[i], words[i+1]
            # get the minimum length of each of the words
            min_word_len = min(len(first_word), len(second_word))

            # check if the first word is longer than the second word
            # and the second word is a prefix of the first word
            if len(first_word) > len(second_word) and first_word[:min_word_len] == second_word[:min_word_len]:
                # this is an invalid edge case since the words given
                # are not sorted lexicographically as explained in the problem
                # so return ""
                return ""

            # loop through all indices up to the min word length
            for j in range(min_word_len):
                # get the characters to compare from each word
                first_char, second_char = first_word[j], second_word[j]

                # if the first and second chars are not the same
                # this explains why the words are sorted lexicographically
                if first_char != second_char:
                    # the first char comes before the second char
                    # so add the second char to the adjacency set of the first char
                    adjacency_set[first_char].add(second_char)
                    # and break because we don't know if the chars after this
                    # are truly in order. Lexicographic order only sorts on the first
                    # differing character between two words, not on all the chars
                    # ex: ZA then YB
                    # we know Z->Y is a valid order, but we can't say A->B is valid
                    break

        # create a visited dict that maps
        # a char to either 0, 1, or 2
        # 0 means the char has not been visited by dfs
        # 1 means the char is currently being visited by dfs
        #   along the recursion path
        # 2 means the char has been fully visited and backtracked by dfs
        visited = {char: 0 for char in adjacency_set}
        
        # setup our result string for the order of the words
        self.result = ""

        # our recursive post-order dfs function to perform
        # topological sort and detect cycles
        def dfsCycleDetection(char) -> bool:
            # standard dfs cycle detection
            # if have already visited this char
            # on the recursive stack path
            # this is our first base case
            if visited[char] == 1:
                # then return True, we have found a cycle
                return True

            # if we have already visited all paths from this
            # char in a previous dfs recursion path
            # we know all nodes from here are safe
            if visited[char] == 2:
                # we can immediately return False
                # no cycles exist from here
                return False

            # otherwise, set this char's
            # visited status to 1
            visited[char] = 1

            # loop through all adjacent chars to this char
            for adjacent_char in adjacency_set[char]:
                # run dfs cycle detection on the adjacent char
                # and check if it returns True for a cycle
                if dfsCycleDetection(adjacent_char):
                    # if it does return true, immediately
                    # return True down the recursion stack
                    return True

            # finally, in post-order fashion
            # add the char to the result string
            # only after we traverse all it's adjacent chars
            self.result += char

            # set this char to visited and fully backtracked
            visited[char] = 2

            # return False by this point, no cycle detected so far
            return False

        # loop through all chars in out adjacency set
        for char in adjacency_set:
            # and run dfs cycle detection on them
            if dfsCycleDetection(char):
                # if a cycle is detected, return ""
                # because it's impossible to detect the
                # order of letters in the language from these words
                return ""

        # finally return the result string but in reverse
        # because we ran post-order dfs
        return self.result[::-1]
