import heapq
import math
from collections import defaultdict
from typing import List


'''
https://leetcode.com/problems/network-delay-time/description/
'''
class Solution:
    # we will use Dijkstra's algorithm to find
    # the shortest path (minimum time) to all nodes
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # init our adjacency list to build
        # a graph of the nodes
        adjacency_list = defaultdict(list)

        # loop through all the times list
        for source, target, time in times:
            # add to our adjacency list
            # key = source
            # values = tuple of (target and time to reach target)
            adjacency_list[source].append((target, time))

        # init our minimum time dict, to hold the minimum time
        # to reach every node using Disjkstra's algorithm
        # key = node
        # value = minimum time to reach that node
        min_times = {i: math.inf for i in range(1, n+1)}

        # init our minimum time for our starting node k to 0
        min_times[k] = 0

        # setup our heap (priority queue) for Dijkstra's algorithm
        # it will hold tuple of (time to reach node, node)
        # init it with tuple of (0, k)
        heap = [(0, k)]

        # loop until the heap is empty
        while heap:
            # get the time it takes to reach the node (current_time)
            # and the node itself from the heap
            current_time, node = heapq.heappop(heap)

            # if the minimum time to reach this node we have saved
            # is < than the current time on this iteration
            if min_times[node] < current_time:
                # skip it, this handles edge case where
                # we add entries to the heap for shorter times
                # that get subsequently overwritten with even shorter
                # times later on
                # it also saves us from having to use a visted set
                continue

            # loop through all adjacent nodes and time to reach them
            for adjacent_node, time in adjacency_list[node]:
                # perform Dijkstra algorithm relaxation
                # if the current time + time to reach node <
                # our saved minimum time to reach this node
                if current_time + time < min_times[adjacent_node]:
                    # update the min time to be that calculated time
                    min_times[adjacent_node] = current_time + time
                    # and add that time and node to the heap to process later
                    # don't worry about adding shorter times for the same node
                    # later on, because we will skip it if our saved min time
                    # is less than any updated time we add here
                    heapq.heappush(heap, (min_times[adjacent_node], adjacent_node))

        # get the longest time it takes to reach any node
        # from our source node k
        longest_time = max(min_times.values())
        
        # if the longest time == math.inf, return -1
        # because it means a node was not visited
        # otherwise, just return the longest_time
        return longest_time if longest_time != math.inf else -1
