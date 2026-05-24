from typing import List


# we will use the disjoint set union (aka. union find)
# algorithm with path compression and rank to solve this problem
class DSU():
    def __init__(self, n):
        # init our parent list
        self.parent = list(range(n))
        # init our rank (height of subtree) list
        self.rank = [1]*n

    # our find method to find the root parent
    # of a node
    def find(self, node):
        # if the node is it's root parent,
        # then return it
        if node == self.parent[node]:
            return node

        # otherwise recursively find the root parent
        # and apply path compression
        self.parent[node] = self.find(self.parent[node])

        # finally return the root node
        return self.parent[node]
    
    # our union method, which will join two sets
    # by making 1 parent a child to another parent
    # it will also return True if it detects a cycle
    # when both parents are th same
    def union(self, node1, node2) -> bool:
        # find the parent nodes
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        # if the parent nodes are the same
        # we have detected a cycle, so return True
        if parent1 == parent2:
            return True

        # if the rank of parent 2 > rank of parent 1
        # swap them so we always merge into the parent
        # with the higher rank
        if self.rank[parent2] > self.rank[parent1]:
            parent1, parent2 = parent2, parent1

        # merge the two sets by setting parent2
        # as a child of parent1
        self.parent[parent2] = parent1

        # if the ranks of the two parents were the same
        # increment the rank of the parent1
        if self.rank[parent1] == self.rank[parent2]:
            self.rank[parent1] += 1

        # return False because if we get here
        # there are no cycles.
        return False

'''
https://leetcode.com/problems/redundant-connection/description/
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # init our DSU object
        dsu = DSU(len(edges))

        # loop through all the edges
        for start, end in edges:
            # perform dsu union on the start and end nodes
            # but subtract 1 from each node because our array
            # is 0 indexed while the graph is 1 indexed
            if dsu.union(start-1, end-1):
                # if a cycle is detected, return the first edge
                # that created this cycle
                return [start, end]
