# start off by creating a TrieNode class
# because we will be using Tries
# as our base data structure
class TrieNode:
    def __init__(self):
        # each TrieNode holds a dictionary mapping
        # it's children characters to their children TrieNode
        self.children: dict[str, TrieNode] = dict()
        # store an end of word flag so we know if this
        # TrieNode is the end of a word.
        self.endOfWord = False

'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
'''
class WordDictionary:

    def __init__(self):
        # our initialization will init an empty root TrieNode
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # begin searching at the root TrieNode
        current = self.root

        # loop through all characters in the word
        for char in word:
            # if the character is not in the current
            # TrieNode's children, we must start a new
            # tree branch in the Trie
            if char not in current.children:
                # start a new branch by creating a new TrieNode
                current.children[char] = TrieNode()
            # set the current pointer to the TrieNode
            # mapped to this character
            # this may be newly created above
            # or prexisting
            current = current.children[char]

        # after looping through the entire word and creating
        # the TrieNode branch, we can set the final TrieNode
        # for the word as the end of a word
        current.endOfWord = True

    def search(self, word: str) -> bool:
        # we will use recursive depth first search
        # to search through the entire Trie
        # this takes in a root node in the Trie
        # and an index to start searching from
        def dfs(root, index):
            # begin searching at the current root
            current = root
            
            # loop through the range starting 
            # at index to end of word
            for i in range(index, len(word)):
                # get the character at this index
                char = word[i]
                # first check if the character is a wildcard
                if char == '.':
                    # if it's a wildcard, we want to check all
                    # possible paths from all possible children characters
                    # so loop through all children TrieNodes
                    for child in current.children.values():
                        # run dfs recursively on them, with the next
                        # character index as starting point
                        if dfs(child, i+1):
                            # if there is a valid path from any one of them
                            # immediately return true
                            return True
                    # if there is no possible path found across all children
                    # from the wildcard character, then return False immediately
                    # no point in trying to repeat searching
                    return False
                # else we have a regular alphanumeric character
                # and can do regular Trie search
                else:
                    # if the character is not in the current TrieNode's children, 
                    if char not in current.children:
                        # just return False, because no path exists
                        # with this character
                        return False
                    # otherwise, update the current pointer to the next 
                    # character's TrieNode for next iteration
                    current = current.children[char]
            
            # at the very end, ensure that the last character
            # pointed to by the current keyword is set to True
            # only then we know the whole word has been found,
            #  and not a prefix
            return current.endOfWord == True

        # run the dfs from the Trie graph root and starting index 0
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
