from typing import List, Optional


'''
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # our base case is if we don't have any elements in our lists
        if not inorder or not postorder:
            # just return None here
            return None
        
        # create the root element of the binary tree
        # we know the root is always the ending of the postorder array
        root = TreeNode(postorder[-1])

        '''
        Example of pivot selection
        postorder: [9, 15, 7, 20, 3]
        inorder: [9, 3, 15, 20, 7]

        postorder root: [3] index 4
        inorder root: [3] index 1

        postorder right: [15, 7, 20] index 1-3
        inorder right: [15, 20, 7] index 2-4

        postorder left: [9] index 0
        inorder left: [9] index 0
        '''

        # find the location (index) of the root (aka pivot)
        # in the inorder array
        # anything to the left is left subtree
        # anything to the right is right subree
        inorder_pivot = inorder.index(root.val)

        # for inorder array, left subtree is to left of pivot
        # excluding the pivot
        inorder_left_subtree = inorder[0:inorder_pivot]
        # and right subtree is to right of pivot
        # excluding the pivot
        inorder_right_subtree = inorder[inorder_pivot+1:]


        # for postorder array, left subtree is to left of pivot
        # excluding the pivot
        postorder_left_subtree = postorder[0:inorder_pivot]
        # and right subtree is to right of pivot,
        # after skipping the root at the end of the array
        # including the pivot
        postorder_right_subtree = postorder[inorder_pivot:-1]

        # create the left subtree recursively
        root.left = self.buildTree(inorder_left_subtree, postorder_left_subtree)
        # create the right subtree recursively
        root.right = self.buildTree(inorder_right_subtree, postorder_right_subtree)

        # return the root after it's subtrees have been created
        return root
