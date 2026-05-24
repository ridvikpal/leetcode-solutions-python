from typing import List


'''
https://leetcode.com/problems/car-fleet/description/
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first we will create an array that holds
        # tuples of (position, speed) for each car
        # init this position_speed array
        position_speed = []

        # loop through all indices of position
        for i in range(len(position)):
            # append the position and speed to the position_speed array
            position_speed.append((position[i], speed[i]))

        # The main advantage of sorting the position_speed array is
        # that we can order (sort) the cars by their position, from
        # closest to target to farthest to target and keep their speeds
        # bundled together with their positions
        position_speed.sort(reverse=True)

        # init our count for the number of fleets
        count = 0
        
        # we will keep track of the maximum time
        # taken by any car to reach the target
        # as we calculate the time for each car
        # from closest car to target to farthest car
        # to target
        # by initializing max time to 0,
        # we gaurentee that there will be at least 1 fleet
        # since the first car's time is always > 0
        # because no car will ever start at the target
        # (distance) > 0
        max_time = 0

        # loop though each car and get it's position, speed
        for position, speed in position_speed:
            # calculate the distance to the target
            # for this car
            distance = target - position
            # calculate the time it takes to reach the target
            time = distance / speed

            # if the time this car takes to reach the target
            # is > max time of the cars before it
            # then it will reach the target later than the cars
            # before it, and the cars before it will catch up
            # to it to create a fleet
            if time > max_time:
                # thus, whenever this car's time 
                # > max_time of the cars before it
                # a fleet is created, so increment the count
                count += 1
                # and update the max time because now this
                # is the new max time
                max_time = time

        # finally return the fleet count
        return count
            
