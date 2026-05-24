import heapq
from typing import List


'''
https://leetcode.com/problems/k-closest-points-to-origin/description/
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first we will create a helper function calculate
        # the distance of a point from the origin
        def getDistanceFromOrigin(point):
            return ((point[0])**2 + (point[1])**2)**0.5

        # create an array that holds
        # 1) the distance of the points from the origin
        #    this will be our priority in our heap
        # 2) the points themselves
        distance_points = [
            (getDistanceFromOrigin(point), point[0], point[1])
            for point in points
        ]

        # turn the distance_points into a min heap
        # where priority is the distance
        heapq.heapify(distance_points)

        # return the 10 smallest points using the nsmallest
        # heapq method
        return [
            (point_data[1], point_data[2])
            for point_data in heapq.nsmallest(k, distance_points)
        ]
