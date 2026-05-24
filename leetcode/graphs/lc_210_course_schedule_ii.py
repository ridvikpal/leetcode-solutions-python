from collections import defaultdict
from typing import List


'''
https://leetcode.com/problems/course-schedule-ii/description/
'''
class Solution:
    # we will use topological sort with post-order dfs
    # to solve this problem since we are essentially sorting
    # the courses from last (no dependencies) to first (has dependencies)
    # this is a dependency resolution problem where dependencies are prereq courses
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first we will create our adjacency list
        # to represent the courses as a graph
        # we can init our adjacency list
        adjacency_list = defaultdict(list)
        # loop over all courses and prereqs in
        # the prerequisites array
        for course, prereq in prerequisites:
            # add the corresponding prereq
            # to the courses' 
            adjacency_list[course].append(prereq)

        # init the array holding the order
        # we will take the courses in
        courseOrder = []

        # init our visited array
        # that will map each course (as index) in our graph
        # to a value to indicate whether it was visited or not
        # if value = 0: it's not visited
        # if value = 1: it is currently being visited
        #               but it has not backtracked yet
        # if value = 2: it has been visited and backtracked
        visited = [0]*numCourses

        # our recursive dfs function that will be used
        # to detect a cycle in the course graph
        # if there is a cycle that means a course 
        # cannot be taken because there are
        # circular preq dependencies
        # it will also add the course to our courseOrder
        # in post-order fashion, standard for dfs topological sort
        def dfsCycleDetection(course):
            # check if we are currently visiting this course
            # and have not backtracked yet 
            if visited[course] == 1:
                # in this case, there is a cycle
                # so return true
                return True

            # check if we have visited this course before
            # checked all paths from it and backtracked
            # without finding any cycles
            if visited[course] == 2:
                # in this case, this course is safe
                # no cycles exist from it
                # we can safely return false
                return False
            
            # set the current course to being visited state
            visited[course] = 1

            # loop through all prereqs for this course
            for prereq in adjacency_list[course]:
                # run dfs on those prereqs
                if dfsCycleDetection(prereq):
                    # if the prereqs backtrack with true
                    # then a cycle exists from one of these paths
                    # so continue to return true down the recursion stack
                    return True

            # set the current course to being fully visited
            # backtracked and safe as no cycle exists from this course
            visited[course] = 2

            # now that we have finished taking all prereqs for
            # this course via recursing on all prereqs, we can
            # add it to our courseOrder array and take it
            courseOrder.append(course)

            # by this point, we know there are no cycles from
            # this course, so return False
            return False

        # loop through all courses in our adjacency list
        for course in range(numCourses):
            # run dfs on each of them
            if dfsCycleDetection(course):
                # and if any of them contains a cycle
                # then return false, the course schedule
                # cannot be taken, so return empty array
                return []
        # if we get to this part, then
        # no course contains a cycle,
        # the course schedule can be taken
        # return the courseOrder array
        return courseOrder
