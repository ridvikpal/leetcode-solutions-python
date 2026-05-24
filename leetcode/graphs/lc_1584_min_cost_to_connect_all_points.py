import heapq
from typing import List


'''
https://leetcode.com/problems/min-cost-to-connect-all-points/description/
'''
class Solution:
    # we will use (greedy) Prim's algorithm since this is effectively
    # a minimum spanning tree problem with distances as weights
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # init the total cost for the graph
        cost = 0

        # init our min heap for Prim's algorithm
        # it will contain tuples of the following form:
        # (distance, x, y)
        heap = [(0, points[0][0], points[0][1])]

        # init our visited set to keep track of
        # the nodes we have visited
        # we can use a set because we are guarenteed
        # that all points are distinct
        # otherwise we would have to use a visited array
        visited = set()

        # loop as long as we have not visited all
        # points in the graph
        while len(visited) < len(points):
            # get the point with the least distance to reach
            distance, x1, y1 = heapq.heappop(heap)

            # if we have already visited this point, skip it
            # this fixes duplicate target points in the heap with
            # different distances from different source points
            if (x1,y1) in visited:
                continue
            
            # add the current point to our visited set
            visited.add((x1, y1))
            # update the cost with this minimum distance
            cost += distance

            # loop through all points
            for x2, y2 in points:
                # skip looking at points that:
                # 1) are the same as our current point
                # 2) we have alrady visited
                if (x2 == x1 and y2 == y1) or ((x2, y2) in visited):
                    continue
                    
                # calculate the manhatten distance for them
                manhatten_distance = abs(x1-x2) + abs(y1-y2)
                # add them to the heap with priority being distance
                heapq.heappush(heap, (manhatten_distance, x2, y2))

        # finally return the total cost
        return cost
