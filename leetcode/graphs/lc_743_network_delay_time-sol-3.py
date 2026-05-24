from collections import defaultdict
import heapq
from typing import List

'''
https://leetcode.com/problems/network-delay-time/description/
'''
class Solution:
    # We will use a lazy version of the Dijkstra's algorithm for this
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # init our adjacency list
        adjacency_list = defaultdict(list)

        # loop through all edges given to us
        for u, v, t in times:
            # and populate the adjacency list
            adjacency_list[u].append((v, t))

        # init our heap (priority queue) we will use for
        # lazy dijkstra's algorithm
        heap = [(0, k)]
        # init our visited set to ensure we don't visit
        # the same nodes again
        visited = set()

        # init our stored time, which is the total
        # minimum time needed to visit all nodes
        stored_time = 0

        # loop as long as there are elements in the heap
        while heap:
            # pop the node with the smallest time from the heap
            time, node = heapq.heappop(heap)

            # if we've already visited this node
            if node in visited:
                # then skip it because the first time we visit a node
                # that is the quickest time to visit that node
                continue

            # add the current node to the visited set
            visited.add(node)
            # update the stored time to the current time
            stored_time = time

            # loop through all adjacent nodes and their times
            for adjacent_node, adjacent_node_time in adjacency_list[node]:
                # if we have not visited them, then add them to the heap
                # it's not necessary to check this since we continue anyway above
                # but it speeds up the execution a bit by skipping unnecessary iterations
                if adjacent_node not in visited:
                    # add the adjacent node with the new time to the heap
                    # new time is current time + time it takes to reach the adjacent node
                    heapq.heappush(heap, (time+adjacent_node_time, adjacent_node))

        # finally, we return the stored time if we have visited all nodes,
        # otherwise we return -1
        return stored_time if len(visited) == n else -1
