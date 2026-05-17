#include <vector>
#include <algorithm>

/**
 * https://leetcode.com/problems/3sum/description/
 *
 * Time complexity: O(n^2) where n = length of nums
 * Space complexity: O(n^2) where n = length of nums
 */
class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        // first sort the nums array
        // this will allows us to use two pointer sorted 2sum technique
        // and place duplicates right next to each other
        // so we can skip the duplicates easily
        std::sort(nums.begin(), nums.end());

        // init our results array
        std::vector<std::vector<int>> result;

        // loop through all the nums indices except for the last two
        // this index i will point to our first number
        for (int i = 0; i < nums.size()-2; ++i) {
            // skip duplicates for the first number at index i
            if (i > 0 && nums[i-1] == nums[i]) {
                continue;
            }

            // setup our left and right pointers
            // as we did for sorted 2sum technique
            int left = i+1;
            int right = nums.size()-1;

            // standard while loop as long as the two pointers don't overlap
            while (left < right) {
                // compute the sum of the three numbers
                int sum = nums[i] + nums[left] + nums[right];

                // if the sum is 0, we have a valid combination
                if (sum == 0) {
                    // create our triplet vector and add all numbers to it
                    std::vector<int> triplet;
                    triplet.push_back(nums[i]);
                    triplet.push_back(nums[left]);
                    triplet.push_back(nums[right]);
                    result.push_back(triplet);

                    // update left and right pointers
                    // because we want to try out new combinations now
                    ++left;
                    --right;

                    // skip duplicates for the second number at the left pointer
                    // we don't need to skip duplicates for the right pointer
                    // because as long as 2 out of 3 numbers are unique, the triplet is unique
                    while (left < right && nums[left-1] == nums[left]) {
                        ++left;
                    }

                }
                // else check if our sum is too big
                // so decrease the right pointer and make it smaller
                else if (sum > 0) {
                    --right;
                }
                // else our sum is too small
                // so increase the left pointer and make it larger
                else {
                    ++left;
                }
            }
        }

        // finally return the result vector
        return result;
    }
};
