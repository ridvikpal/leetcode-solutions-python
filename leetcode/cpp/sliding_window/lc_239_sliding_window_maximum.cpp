#include <deque>
#include <vector>

/**
 * https://leetcode.com/problems/sliding-window-maximum/description/
 *
 * Time complexity: O(n) where n = length of nums
 * Space complexity: O(n) where n = length of nums
 */
class Solution {
public:
    std::vector<int> maxSlidingWindow(std::vector<int>& nums, int k) {
        // init our result array
        std::vector<int> result;

        // init our queue holding indices
        // this will be a monotonically decreasing queue
        // whose size will never exceed k
        // start of the queue -> largest number index in the sliding window
        // end of the queue -> smallest number index in the sliding window
        std::deque<int> indexQueue;

        // since this is a sliding window problem
        // we will setup our start pointer
        int start = 0;
        // and our end pointer will be automatically incremented
        // so loop through all end pointers
        for (int end = 0; end < nums.size(); ++end) {
            // on each iteration, first we will insert into the monotonic queue
            // since we want the queue to be decreasing, as long as
            // the number we are inserting is larger than the number at the back of the queue
            // we will remove the number at the back of the queue
            while (indexQueue.size() > 0 && nums[end] > nums[indexQueue.back()]) {
                indexQueue.pop_back();
            }
            // and then insert our current number at the back of the queue
            indexQueue.push_back(end);

            // next, we will determine if we need to remove the current largest number index
            // because that index is now out of bounds of our sliding window
            // this happens when the start pointer is greater than the largest number index
            // since we are moving left to right
            if (indexQueue.size() > 0 && start > indexQueue.front()) {
                indexQueue.pop_front();
            }

            // finally, as long as we have a sliding window of the correct size (k)
            // we can keep adding the largest number in our monotonic queue (the front)
            // to our result array
            // and incrementing the start pointer (our end pointer automatically gets incremented)
            // to keep the sliding window size the same
            if (end+1 >= k) {
                result.push_back(nums[indexQueue.front()]);
                ++start;
            }
        }

        // finally, we will return the result array
        return result;
    }
};
