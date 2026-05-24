from collections import Counter, deque
import heapq
from typing import List


'''
https://leetcode.com/problems/task-scheduler/description/
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # start off by mapping each char task to a count
        # in a dictionary using a python Counter
        char_count_dict = Counter(tasks)

        # map count to char task in list of tuples
        # that we will use as a max heap based on count
        # because of max heap, we negate the count
        count_char_heap = [(-count, char) for char, count in char_count_dict.items()]
        heapq.heapify(count_char_heap)

        # create a cooldown queue that will be used to contain
        # recently completed char tasks in the following format:
        # (next_availible_time, char_count, char)
        cooldown_queue = deque()

        # init our time to 0
        time = 0

        # keep looping (completing tasks) as long as
        # 1) we still have char tasks in our heap
        #    to complete immediately
        # 2) we still have char tasks in our cooldown queue
        #    to complete in the future
        while count_char_heap or cooldown_queue:
            # always increment our time at each iteration 
            # of the while loop
            time += 1

            # first check if we have char tasks in our heap
            # to complete immediately (at current time)
            if count_char_heap:
                # get the count of the character
                # and the next character
                # technically we don't need to store the next
                # char at all, but it made debugging easier
                # so I left it in
                next_char_count, next_char = heapq.heappop(count_char_heap)
                
                # now decrement the char count because we have
                # processed it at this time
                # we negate next_char_count because our max
                # heap is just a negative min heap
                new_next_char_count = -next_char_count - 1

                # if the new char count after decrementing 
                # is greater than 0, it still has to be processed
                # in the future
                if new_next_char_count > 0:
                    # add the char count and char
                    # to the cooldown queue to be processed
                    # at time n iterations in the future
                    cooldown_queue.append((
                        time+n,
                        new_next_char_count,
                        next_char
                    ))
            
            # second check if we have char tasks in our cooldown queue
            # that have finished cooldown and can be readded to our heap
            # to be processed again at next iteration
            if cooldown_queue and cooldown_queue[0][0] == time:
                # if so, pop their char count and char
                _, next_char_count, next_char = cooldown_queue.popleft()
                # and add the char count and char back to the heap
                heapq.heappush(count_char_heap, (
                    -next_char_count,
                    next_char
                ))

        # finally return the time after all tasks have been processed 
        return time
