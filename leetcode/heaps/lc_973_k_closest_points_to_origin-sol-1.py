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

        # then we will initialize a max heap array
        # that will be of size k
        # this heap array will hold the k closest
        # points to the origin
        k_closest_points = []

        # loop through all points
        for point in points:
            # calculate the point distance
            point_distance = getDistanceFromOrigin(point)

            # check if we don't have k points in our k heap
            if len(k_closest_points) < k:
                # if we don't, then we can just push directly
                # onto the heap, the negative points distance
                # since we want our k heap to be a max heap
                heapq.heappush(k_closest_points, (-point_distance, point[0], point[1]))
            # else we already have k points in our k heap
            else:
                # so in this case we need to push onto the heap
                # but also pop the point with the largest distance
                # from the origin -> This is why we used a max heap
                heapq.heappushpop(k_closest_points, (-point_distance, point[0], point[1]))

        # finally, we can use list comprehension
        # to return the actual (x,y) pairs from our heap
        return [(point_data[1], point_data[2]) for point_data in k_closest_points]
