from collections import defaultdict
from typing import List


'''
https://neetcode.io/problems/valid-tree/question
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # first we can check if the number of edges
        # in the graph is n-1, which is a requirement for trees
        # this must be the case since we are not given duplicate edges
        if len(edges) != n-1:
            return False

        # then we can create our adjacency list
        # to easily represent the graph
        # init our adjacency list as a dict of lists
        adjacency_list = defaultdict(list)
        # loop through all start and end nodes in the edges
        for start, end in edges:
            # because we are given an undirected graph
            # and order of nodes in an edge pair is unknown
            # add start and end nodes to each other's corresponding
            # adjacency list
            adjacency_list[start].append(end)
            adjacency_list[end].append(start)

        # create our visited set to keep track of
        # the nodes we have visited
        visited = set()

        # our standard recursive dfs function
        # to visit all nodes once
        def dfs(node):
            # add the current node to our visited set
            visited.add(node)

            # loop through all adjacent nodes
            for adjacent_node in adjacency_list[node]:
                # if we have not visited them before
                if adjacent_node not in visited:
                    # then dfs on them recursively 
                    dfs(adjacent_node)

        # run dfs from the first node
        # in a tree, we want to be able to reach
        # all nodes from any other node, so no need
        # for a for loop running dfs from all nodes
        dfs(0)

        # only return True if we were able to visit all
        # nodes from the first node (i.e., the graph is connected)
        return len(visited) == n
