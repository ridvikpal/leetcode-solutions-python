from collections import deque
from typing import Optional


'''
https://leetcode.com/problems/clone-graph/description/
'''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # handle the edge case where we are given an empty graph
        if not node:
            # simply return, since there is nothing to clone
            return

        # we will use a dictionary that
        # maps an old node -> new (deep clone) node
        oldToNew = dict()

        # we will use an iterative bfs solution
        # so we will init our stack with our first node
        queue = deque([node])
        # we will init our visited set with our first node
        visited = set([node])

        # standard iterative bfs while loop
        # as long as the stack is not empty
        while queue:
            # pop the last oldNode from the stack
            oldNode = queue.popleft()

            # if the oldNode is not in the oldToNew dict
            # that means we have not cloned it yet
            if oldNode not in oldToNew:
                # so create a deep copy clone of oldNode
                newNode = Node(oldNode.val)
                # and add it to the oldToNew dictionary
                oldToNew[oldNode] = newNode

            # loop through all the oldNode's neighbours
            for oldNeighbour in oldNode.neighbors:
                # if the oldNeighbour is not in the oldToNew dict
                # that means we have not cloned it yet
                if oldNeighbour not in oldToNew:
                    # so create a deep copy clone of oldNeighbour
                    newNeighbour = Node(oldNeighbour.val)
                    # add it to the oldToNew dictionary
                    oldToNew[oldNeighbour] = newNeighbour

                # now, we can add the deep cloned neighbour to the
                # neighbour adjacency list of our deep cloned new node
                oldToNew[oldNode].neighbors.append(oldToNew[oldNeighbour])

                # check if we have not already visited the oldNeighbour
                if oldNeighbour not in visited:
                    # in this case, add it to our stack
                    queue.append(oldNeighbour)
                    # and mark it as visited
                    visited.add(oldNeighbour)

        # finally, after deep cloning the whole graph
        # return the new node we created first
        return oldToNew[node]
