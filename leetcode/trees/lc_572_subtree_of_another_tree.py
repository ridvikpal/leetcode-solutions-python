from collections import deque
from typing import Optional


'''
https://leetcode.com/problems/subtree-of-another-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we can create a dfs function that checks if two
        # trees are the same
        def dfsSameCheck(node1, node2):
            # if the two nodes are None
            # we have two same empty leaf nodes
            if not node1 and not node2:
                # so return True
                return True

            # if one of the nodes is None but the other isn't
            if (not node1 and node2) or (node1 and not node2):
                # then return False the two trees aren't the same
                return False

            # check the left subtree for similarity
            left_check = dfsSameCheck(node1.left, node2.left)
            # check the right subtree for similarity
            right_check = dfsSameCheck(node1.right, node2.right)

            # if either the left or right subtrees are not the same
            if not left_check or not right_check:
                # then return false
                return False

            # finally, check if the values of
            # the current two nodes are the same
            # and return the result
            return node1.val == node2.val

        # we will use a bfs level by level traversal
        # of the original root tree
        # so init our standard bfs queue
        queue = deque([root])

        # standard bfs loop as long as we have a queue
        while queue:
            # get the current node
            current = queue.popleft()

            # run the dfs check on the same node
            # to see if the subtree from current node
            # is the same as the subRoot subtree
            if dfsSameCheck(current, subRoot):
                # if it is true, then return True
                return True

            # if there is a left node
            if current.left:
                # add the left node to the queue
                queue.append(current.left)
            # if there is a right node
            if current.right:
                # add the right node to the queue
                queue.append(current.right)

        # if we check every node in root and it doesn't match
        # subRoot, then we can return False
        return False
