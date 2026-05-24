# create a TrieNode class to represent
# a character (node) of the Trie graph
class TrieNode:
    def __init__(self):
        # it will hold a dictionary mapping
        # a child character to a child TrieNode
        self.children: dict[str, TrieNode] = dict()
        # add a flag to determine if this TrieNode
        # is the end of a word
        self.endOfWord = False

    # string representation of the class for debugging
    def __str__(self):
        return f"""TrieNode(
            children={self.children}
            endOfWord={self.endOfWord}
        )"""

'''
https://leetcode.com/problems/implement-trie-prefix-tree/description/
'''
class Trie:

    def __init__(self):
        # initialize our trie graph
        # with an empty root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # begin iterating through the trie at the root
        current = self.root

        # loop through every character in the word
        for char in word:
            # check if the character is not in the 
            # current TrieNode's children
            if char not in current.children:
                # if it's not, create a TrieNode
                # for the character
                # and add it to the current node's children dict
                current.children[char] = TrieNode()
            # set the current TrieNode to the
            # current character's TrieNode
            # this could be preexisting, or newly created above
            current = current.children[char]

        # once we're done, current is pointing to the last
        # character for the word in the TrieNode,
        # so set it as the end of a word
        current.endOfWord = True

    def search(self, word: str) -> bool:
        # begin iterating through the trie at the root
        current = self.root

        # loop through every character in the word
        for char in word:
            # check if the character is not in the
            # current TrieNode's children
            if char not in current.children:
                # if it's not, the word doesn't exist
                # in the Trie graph, so return false
                return False
            # otherwise, the character exists in
            # the Trie graph so set the current TrieNode
            # to the current character's TrieNode
            current = current.children[char]
        
        # after looping through all characters,
        # if the last character's TrieNode is marked
        # as the end of a word, only then return true
        # because search() searches for a full word
        return current.endOfWord == True

    def startsWith(self, prefix: str) -> bool:
        # begin iterating through the trie at the root
        current = self.root

        # loop through every character in the word
        for char in prefix:
            # check if the character is not in the
            # current TrieNode's children
            if char not in current.children:
                # if it's not, the word doesn't exist
                # in the Trie graph, so return false
                return False
            # otherwise, the character exists in
            # the Trie graph so set the current TrieNode
            # to the current character's TrieNode
            current = current.children[char]
        
        # after looping through all characters,
        # we know that the prefix exists, so return True
        # no need to check if it's the end of a word
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
