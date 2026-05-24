from typing import List


# We will use the basic form of disjoint set union 
# (DSU aka. union-find) algorithm
# to solve this problem, so init the class
class DSU():
    def __init__(self, n):
        # we can initialize our parent array
        # this will hold the immediate parent of
        # each node for each of our set trees
        # ex [0, 0, 1, 1]
        # this means that nodes 0 and 1 have parent node 0
        # and node 2 and 3 have parent node 1
        # but they are all in 1 connected set because
        # parent of node 1 is node 0
        # we will perform this recursion to find the root
        # parent 0 in our find() function
        self.parent = list(range(n))
        # we can initialize our component count.
        # at the start, each node is it's own disjoint set
        # and the component count is therefore n for n nodes
        self.componentCount = n

    # our find function that finds the root parent
    # for a given node, recursing up the parent array
    def find(self, node):
        # if the current node is it's own parent
        # then return it
        if node == self.parent[node]:
            return node
        # otherwise, recurse up the parent array
        # until we find the root parent that is 
        # it's own parent
        return self.find(self.parent[node])

    # our union function that joins two subsets
    # (two subtrees) together if the input two nodes
    # are from different subsets
    def union(self, node1, node2):
        # first find the parents of each node
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        # if the parents of each node are the same
        # we have detected a cycle and so we can't
        # combine the same sets together
        if parent1 == parent2:
            # just return without combining
            return
        
        # just set the parent2 node to be a child
        # of parent1, thust moving all child nodes in parent2
        # to be child nodes of parent1
        self.parent[parent2] = parent1
        # since we merged two sets together, we can decrement
        # the component count, since there is 
        # 1 less connected component (1 less disjoint set)
        self.componentCount -= 1

'''
https://neetcode.io/problems/count-connected-components/question
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # we will init our dsu object
        dsu = DSU(n)

        # loop through all edges
        for start, end in edges:
            # perform union on each node in each edge
            dsu.union(start, end)

        # finally, just return the component count
        return dsu.componentCount
