from collections import defaultdict
from typing import List


'''
https://leetcode.com/problems/reconstruct-itinerary/description/
'''
class Solution:
    # to solve this problem, we will use the Hierholzer algorithm
    # which is a modified dfs that appends to path in post-order
    # and removes edges from the adjacency_list as it visits them
    # the goal of Hierholzer algorithm is to create a Eulerian path
    # that visits all edges, whereas regular dfs aims to visit all vertices
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # first we will create our adjacency list to model the graph
        # init our adjacency list object
        adjacency_list = defaultdict(list)

        # loop through all edges (tickets)
        for from_city, to_city in tickets:
            # add the edges to the corresponding adjacency list
            adjacency_list[from_city].append(to_city)

        # loop through all cities
        for city in adjacency_list:
            # and sort their adjacency list because we
            # want to visit cities in lexicographical order
            # we sort in reverse because then we can pop
            # from a city's adjacency list in constant time
            adjacency_list[city].sort(reverse=True)

        # init our final flight path
        path = []

        # create our recursive dfs function
        # that will go along each flight path (edge)
        # once using Hierholzer algorithm,
        # not like regular dfs which only visits all edges once
        # notice the lack of a visited set
        def dfs(city):
            # as long as there are flight paths from this city
            while adjacency_list[city]:
                # get the next city to visit
                # and pop it from the adjacency list
                # aka use up the flight ticket
                next_city = adjacency_list[city].pop()
                # perform dfs recursively on this next city
                # aka fly to the next city from this city
                # with the flight ticket you just got
                dfs(next_city)

            # finally add the city to the path after
            # no more flights exist from it (all flights
            # from this city have been taken)
            path.append(city)

        # we always begin our dfs from JFK airport
        dfs("JFK")

        # Hierholzer algorithm is a post order dfs traversal
        # so we have to reverse it to get the path from
        # the starting point JFK
        path.reverse()

        # finally just return the path
        return path
