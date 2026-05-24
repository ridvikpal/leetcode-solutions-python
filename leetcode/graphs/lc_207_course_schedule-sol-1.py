from collections import defaultdict
from typing import List


'''
https://leetcode.com/problems/course-schedule/description/
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first we can convert the prerequisites list
        # into an adjacency list to create a graph
        # so init our adjacency list
        adjacency_list = defaultdict(list)

        # loop through each course and prereq
        for course, prereq in prerequisites:
            # and add the prereq to the list of all prereqs (value)
            # for the course (key)
            adjacency_list[course].append(prereq)

        # we will create a visited dictionary
        # that will map each course in our graph
        # to a value to indicate whether it was visited or not
        # if value = 0: it's not visited
        # if value = 1: it is currently being visited
        #               but it has not backtracked yet
        # if value = 2: it has been visited and backtracked
        visited =  defaultdict(int)

        # our recursive dfs function that will be used
        # to detect a cycle in the course graph
        # if there is a cycle then there is a circular dependency
        # meaning that a course cannot be taken because there are
        # circular preq dependencies
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
                    # so contine to return true down the recursion stack
                    return True

            # set the current course to being fully visited
            # backtracked and safe as no cycle exists from this course
            visited[course] = 2

            # so return false, no cycle existed from this course
            return False

        # loop through all courses in our adjacency list
        for course in list(adjacency_list.keys()):
            # run dfs on each of them
            if dfsCycleDetection(course):
                # and if any of them contains a cycle
                # then return false, the course schedule
                # cannot be taken
                return False

        # if we get to this part, then
        # no course contains a cycle,
        # the course schedule can be taken
        # return true
        return True
