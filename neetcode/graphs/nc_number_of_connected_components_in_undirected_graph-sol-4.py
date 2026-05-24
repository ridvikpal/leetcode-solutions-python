from typing import List


# We will use the disjoint set union 
# (DSU aka. union-find) algorithm
# with path compression and rank (subtree height)
# to solve this problem, so init the class
class DSU():
    def __init__(self, n):
        # we can initialize our parent array
        # this will hold the immediate parent of
        # each node for each of our set trees
        # ex [0, 1, 1, 3]
        # this means that nodes 0 and 3 are their own
        # parents (they are disjoint sets)
        # while nodes 1 and 2 are part of the same set
        # because they have the same parent, node 1
        # we will perform this recursion to find the root
        # parent in our find() function, and then path compression
        # to ensure that each value in the parentArray directly
        # holds the top level root parent, not the immediate root
        self.parent = list(range(n))

        # we can init our rank array
        # this will hold the number of connected nodes
        # for each subtree, for each parent
        # ex [1, 2, 1, 1]
        # this means that node 2 is a parent node
        # for which there are 2 nodes connected in it's subtree
        # which from the parent array we can see are nodes 1 and 2
        # so it's height (rank) is 2
        # however, nodes 0, 2 and 1 only have 1 node connected
        # to their subtrees since they are only parents to themselves
        # or are leaf child nodes for another parent, so their rank is 1
        self.rank = [1]*n

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
        # it's own parent, and set that root parent
        # as the node's parent in the parent array
        # this is path compression
        self.parent[node] = self.find(self.parent[node])
        
        # finally, just return the node's parent
        return self.parent[node]

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

        # if the rank of parent2 is > rank of parent1
        # swap them so we always merge sets where
        # the set with the largest subtree height "consumes" 
        # the set with the smaller subtree height in the lines below
        if self.rank[parent2] > self.rank[parent1]:
            parent1, parent2 = parent2, parent1
        
        # just set the parent2 node to be a child
        # of parent1, thust moving all child nodes in parent2
        # to be child nodes of parent1
        # from above, we guarentee that rank(parent1) > rank(parent2)
        self.parent[parent2] = parent1

        # after merging parent2 into parent1, if the ranks were
        # the same, then we need to increment the rank of parent1
        # because the subtree height of parent1 would also increase by 1
        if self.rank[parent1] == self.rank[parent2]:
            self.rank[parent1] += 1

        # since we merged two sets together, we can decrement
        # the component count, since there is 
        # 1 less connected component (1 less disjoint set)
        self.componentCount -= 1


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
