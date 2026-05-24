from collections import defaultdict, deque
from typing import List


'''
https://leetcode.com/problems/word-ladder/description/
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # first handle the edge case where
        # the word is not in our wordList
        if endWord not in wordList:
            # simply return 0 because it's not possible
            # to end up at this end word that easily
            return 0

        # all words are the same length
        # we can store this word length for convenience
        word_len = len(beginWord)

        # we will use a dictionary where keys are
        # wildcard matching patterns and values
        # are a list of words that match that wildcard pattern
        # this is effectively our adjacency list
        patterns = defaultdict(list)

        # loop through all words in wordList and beginWord
        for word in (wordList + [beginWord]):
            # loop through each index of a word
            for i in range(word_len):
                # create a wildcard pattern where the '*'
                # char is at incrementing indices for the word
                # ex. a*other, an*ther, ano*her, ...
                pattern = word[:i] + '*' + word[i+1:word_len]
                # add the word to it's wildcard patterns
                patterns[pattern].append(word)

        # init our standard bfs queue
        queue = deque([beginWord])
        # init our standard bfs visited set
        visited = set([beginWord])

        # init the num of words
        # we have to go through to
        # reach the endWord
        count = 0

        # standard bfs loop until queue is empty
        while queue:
            # increment the count on each iteration
            count += 1

            # we are doing layer by layer bfs queue
            # so loop through each layer 1 by 1
            for _ in range(len(queue)):
                # get the leftmost word in the queue
                word = queue.popleft()
                # if the word is the endWord
                if word == endWord:
                    # return the count
                    return count

                # otherwise, loop through each index of a word
                for i in range(word_len):
                    # create a wildcard pattern where the '*'
                    # char is at incrementing indices for the word
                    # ex. a*other, an*ther, ano*her, ...
                    pattern = word[:i] + '*' + word[i+1:word_len]
                    # check for adjacent words that match this pattern
                    for adjacent_word in patterns[pattern]:
                        # if this adjacent word is not visited
                        if adjacent_word not in visited:
                            # then add it to right of the queue
                            queue.append(adjacent_word)
                            # and add it to the visited set
                            visited.add(adjacent_word)

        # if we cannot reach the endWord via bfs,
        # then return 0 at the very end
        return 0
