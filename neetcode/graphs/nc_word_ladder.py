from collections import defaultdict, deque
from typing import List


'''
https://neetcode.io/problems/word-ladder/question
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # first perform a sanity check to ensure
        # that if the endWord is not in the wordList,
        # return 0 because we can never reach it if that's the case
        if endWord not in wordList:
            return 0

        # init our adjacency list
        # since we are creating a graph of words
        # where adjacent words differ by 1 char
        adjacency_list = defaultdict(list)

        # loop through all the words in wordList
        for word in wordList:
            # calculate the hamming distance between
            # beginWord and each word in wordList
            hamming_distance = sum(1 for char1, char2 in zip(beginWord, word) if char1 != char2)
            # if the hamming distance is 1
            # the words differ by at most 1 char
            if hamming_distance == 1:
                # so add them to the adjacency list of beginWord
                adjacency_list[beginWord].append(word)

        # loop through all the words in wordList first
        for first_word in wordList:
            # loop through all the words in wordList second
            for second_word in wordList:
                # calculate the hamming distance between the words
                hamming_distance = sum(1 for char1, char2 in zip(first_word, second_word) if char1 != char2)
                # if the hamming distance is 1
                # the words differ by at most 1 char
                if hamming_distance == 1:
                    # so add them to the adjacency list of beginWord
                    adjacency_list[first_word].append(second_word)

        # init our queue for bfs through
        # the graph of words
        queue = deque([beginWord])
        # init our visited set for bfs
        visited = set([beginWord])

        # init our count for the number of
        # adjacent words (layers) we have to traverse
        # to find the endWord
        count = 0

        # standard bfs loop until the queue is empty
        while queue:
            # increment the count on each iteration
            count += 1

            # we will do layer-by-layer bfs
            # so loop through all elements in each layer
            for _ in range(len(queue)):
                # get the word at this layer
                word = queue.popleft()
                # if the word is the end word
                if word == endWord:
                    # return the count and stop iterating
                    return count

                # otherwise, loop through adjacent words
                for adjacent_word in adjacency_list[word]:
                    # if the adjacent word has not been visited before
                    if adjacent_word not in visited:
                        # add it to the queue
                        queue.append(adjacent_word)
                        # mark it as visited
                        visited.add(adjacent_word)
