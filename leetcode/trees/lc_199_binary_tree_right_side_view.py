from collections import deque
from typing import List, Optional


'''
https://leetcode.com/problems/binary-tree-right-side-view/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # this is a standard bfs level by level tree traversal,
    # but we need to only need to add the final element in the level
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if we are given an empty tree
        if not root:
            # return an empty list
            return []

        # setup our standard bfs queue
        queue = deque([root])

        # init our path array we will return
        path = []

        # standard bfs queue while loop
        while queue:
            # store the number of nodes on this level
            num_nodes_on_level = len(queue)

            # loop through all nodes on this level
            for i in range(num_nodes_on_level):
                # get the current node on this level
                current = queue.popleft()

                # if this is the last node on this level
                if i == num_nodes_on_level-1:
                    # then add it to the path because
                    # it is the rightmost node
                    path.append(current.val)

                # if there is a left node
                if current.left:
                    # add it to the bfs queue
                    queue.append(current.left)
                # if there is a right node
                if current.right:
                    # add it to the bfs queue
                    queue.append(current.right)

        # finally return the path variable
        return path
