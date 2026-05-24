from collections import defaultdict


'''
https://leetcode.com/problems/time-based-key-value-store/description/
'''
class TimeMap:

    def __init__(self):
        # we will use a dictionary as our primary data structure
        # where keys are the TimeMap keys
        # and values are a list of (timestamp, value) tuples
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # we can simply append to the list of values for a key
        # with the (timestamp, value) tuple
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # first we can get a list of all values we
        # have stored for this key
        all_values = self.dictionary[key]

        # if the list is empty, then
        # we have no values stored for this key
        if not all_values:
            # so return an empty string
            return ""

        # otherwise, we have values stored
        # and will use binary search to find the
        # correct value in log(n) time
        # init our left pointer
        l = 0
        # init our right pointer
        r = len(all_values)-1

        # standard binary search while loop
        while l <= r:
            # compute the middle index
            m = (l+r) // 2

            # if the timestamp of the middle tuple
            # is the same as our desired timestamp
            if all_values[m][0] == timestamp:
                # we have an exact hit and can return the
                # value stored at that timestamp
                return all_values[m][1]

            # else if the timestamp is greater
            # than the middle index timestamp
            if timestamp > all_values[m][0]:
                # so we need to move our left
                # pointer above the middle index
                # because we need larger values
                l = m + 1
            # else the timestamp is less than
            # the middle index timestamp
            else:
                # so we need to move the right
                # pointer below the middle index
                # because we need smaller values
                r = m - 1

        # if we get to this point, we have not found
        # an exact match for a value stored at the given timestamp
        # so we can check if the middle index timestamp is
        # larger than the given timestamp
        if all_values[m][0] > timestamp:
            # if so, we need to decrease our middle index by 1
            # so we are gaurenteed to have a middle index timestamp
            # less than the given timestamp
            m -= 1

        # if the middle index is still in bounds
        if m >= 0:
            # then return the middle index value
            # which is the value <= given timestamp
            return all_values[m][1]

        # else now our middle index is out of bounds
        # meaning all values we have stored for this key
        # are larger than the given timestamp
        # so return an empty string
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
