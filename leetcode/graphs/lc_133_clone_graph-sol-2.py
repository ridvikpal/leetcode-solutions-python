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

        # we can use a recursive dfs function
        # to clone our graph
        def dfsClone(oldNode: Node) -> Node:
            # check if we have already cloned this node before
            # this is our base case
            if oldNode in oldToNew:
                # in this case, simply return
                # the already cloned node
                return oldToNew[oldNode]

            # otherwise we have not cloned this old node
            # before yet, so create a clone
            newNode = Node(oldNode.val)
            # and add it to the oldToNew dict mapping
            oldToNew[oldNode] = newNode

            # loop through all the oldNode's neighbours
            for oldNeighbour in oldNode.neighbors:
                # run dfs clone recursively on old neighbours
                # to create new copies of the neighbours
                newNeighbour = dfsClone(oldNeighbour)
                # and add the new neighbours to the neighbours
                # of the new node we created
                oldToNew[oldNode].neighbors.append(newNeighbour)

            # finally, return the node we created
            return newNode

        # run our dfs clone function with the starting node
        dfsClone(node)

        # finally, after deep cloning the whole graph
        # return the new node we created first
        return oldToNew[node]
