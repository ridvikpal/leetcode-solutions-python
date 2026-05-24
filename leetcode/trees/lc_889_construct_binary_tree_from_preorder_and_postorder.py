from typing import List, Optional


'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # our first base case is if we don't have any elements in our lists
        if not preorder or not postorder:
            # just return None here
            return None
        
        # create the root element of the binary tree
        # we know the root is always the starting of the preorder array
        root = TreeNode(preorder[0])

        # our second base case is if preorder and postorder
        # are of length 1, then just return the root without
        # creating subtrees because there are no subtrees
        if len(preorder) == 1 or len(postorder) == 1:
            return root

        '''
        Example of pivot selection
        preorder = [1,2,4,5,3,6,7]
        postorder = [4,5,2,6,7,3,1]

        preorder root = [1] index 0
        postorder root = [1] index -1

        preorder left = [2,4,5] index 1-3 size = 3
        postorder left = [4,5,2] index 0-2 size = 3

        preorder right = [3,6,7] index 4-6 size = 3
        postorder right = [6,7,3] index 3-5 size = 3
        '''

        # postorder traverses in the opposite direction of preorder
        # even in the left or right subtrees.
        # so first preorder left subtree element
        # is the last postorder left subtree element
        # we can get that last postorder left subtree element index
        postorder_last_left_index = postorder.index(preorder[1])
        # the size is then just that index + 1
        left_subtree_size = postorder_last_left_index+1


        # for preorder array, left subtree is immediately after
        # first element (which is root)
        preorder_left_subtree = preorder[1:1+left_subtree_size]
        # and the right subtree is immediately after the left subtree
        preorder_right_subtree = preorder[1+left_subtree_size:]

        # for postorder array, left subtree is at the start of the array
        postorder_left_subtree = postorder[:left_subtree_size]
        # and the right subtree is after the left subtree
        # up until the last element (which is root)
        postorder_right_subtree = postorder[left_subtree_size:-1]

        # create the left subtree recursively
        root.left = self.constructFromPrePost(preorder_left_subtree, postorder_left_subtree)
        # create the right subtree recursively
        root.right = self.constructFromPrePost(preorder_right_subtree, postorder_right_subtree)

        # return the root after it's subtrees have been created
        return root
