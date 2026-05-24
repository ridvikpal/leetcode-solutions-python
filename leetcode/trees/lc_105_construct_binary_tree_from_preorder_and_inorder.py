from typing import List, Optional


'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # our base case is if we don't have any elements in our lists
        if not preorder or not inorder:
            # just return None here
            return None

        # create the root element of the binary tree
        # we know the root is always the starting of the preorder array
        root = TreeNode(preorder[0])

        '''
        Example of pivot selection
        preorder: [8, 2, 7, 1, 9, 3, 6]
        inorder: [7, 2, 1, 8, 3, 9, 6]
        
        preorder root: [8] index 0
        inorder root: [8] index 3
        
        inorder left subtree: [7, 2, 1] indexes 0-2
        inorder right subtree: [3, 9, 6] indexes 4-6

        preorder left subtree: [2, 7, 1] indexes 1-3
        preorder right subtree: [9, 3, 6] indexes 4-6
        '''

        # find the location (index) of the root (aka pivot)
        # in the inorder array
        # anything to the left is left subtree
        # anything to the right is right subree
        inorder_pivot = inorder.index(preorder[0])

        # for inorder array, left subtree is to left of pivot
        # excluding the pivot
        inorder_left_subtree = inorder[:inorder_pivot]
        # and right subtree is to right of pivot
        # excluding the pivot
        inorder_right_subtree = inorder[inorder_pivot+1:]

        # for preorder array, left subtree is to left of pivot
        # after skipping root at start of array
        # including the pivot
        preorder_left_subtree = preorder[1:inorder_pivot+1]
        # and right subtree is to right of pivot
        # excluding the pivot
        preorder_right_subtree = preorder[inorder_pivot+1:]

        # create the left subtree recursively
        root.left = self.buildTree(preorder_left_subtree, inorder_left_subtree)
        # create the right subtree recursively
        root.right = self.buildTree(preorder_right_subtree, inorder_right_subtree)

        # return the root after it's subtrees have been created
        return root
