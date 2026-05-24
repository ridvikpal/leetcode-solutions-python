from collections import defaultdict
from typing import List


'''
https://neetcode.io/problems/count-connected-components/question
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        # init our connected component count
        count = 0

        # loop through all nodes
        for node in range(n):
            # if we have not visited this node before
            if node not in visited:
                # then run dfs to visit
                # this node and all connected nodes
                dfs(node)
                # increment the count
                count += 1

        # finally, return the count of all connected components
        return count
