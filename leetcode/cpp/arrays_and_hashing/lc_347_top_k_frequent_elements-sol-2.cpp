#include <vector>
#include <unordered_map>

/**
 * https://leetcode.com/problems/top-k-frequent-elements/description/
 *
 * Time complexity: O(n) where n = length of nums
 * Space complexity: O(n) where n = length of nums
 */
class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        // init our hashmap to store the counts of each number
        std::unordered_map<int, int> counter;

        // create a 2d array to use the bucket sorting method
        // index = frequency the number shows up
        // value = array of the numbers with this frequency
        // the size of this array is nums.size() + 1 because
        // at most the array only contains a single number
        std::vector<std::vector<int>> frequencyToNums(nums.size()+1);

        // init our results array
        std::vector<int> result;

        // loop through all numbers
        for (const int& num : nums) {
            // increment the count of each number in our counter
            counter[num] += 1;
        }

        // loop through all elements in the counter hashmap
        for (const std::pair<int, int>& element : counter) {
            // add each number to the correct array in frequencyToNums
            // based on it's frequency
            frequencyToNums[element.second].push_back(element.first);
        }

        // loop through the frequencyToNums array backwards
        // since largest number frequencies will be the largest indices
        for (int i{static_cast<int>(frequencyToNums.size()) - 1}; i >= 0; --i) {
            // if we already have k elements in the results array
            // stop populating it and break out the loop
            if (result.size() == k) {
                break;
            }

            // populate the results array with all the numnbers in each frequencyToNums array
            // for the frequency at index i
            result.insert(result.end(), frequencyToNums[i].begin(), frequencyToNums[i].end());
        }

        // finally return the results array
        return result;
    }
};
