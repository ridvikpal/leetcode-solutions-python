#include <vector>

/**
 * https://leetcode.com/problems/container-with-most-water/description/
 *
 * Time complexity: O(n) where n = length of height
 * Space complexity: O(1)
 */
class Solution {
public:
    int maxArea(std::vector<int>& height) {
        // init our left and right pointers
        // pointing to opposite ends of the array
        int left = 0;
        int right = height.size() - 1;

        // init the index of the max left height
        // and right height found so far
        int maxLeftHeightIndex = left;
        int maxRightHeightIndex = right;

        // init the max area found so far
        int maxArea = 0;

        // standard two pointer while loop
        // until the two pointers overlap
        while (left < right) {
            // calculate the area as a square described in the problem statement
            int area = (right - left) * std::min(height[left], height[right]);

            // update the max area accordingly
            maxArea = std::max(area, maxArea);

            // if the left height is smaller than the right height
            // then the left height is the bottleneck
            if (height[left] < height[right]) {
                // so update the left height
                left++;
            // else the right height is the bottleneck
            } else {
                // so update the right height
                right--;
            }
        }

        // finally return the max area
        return maxArea;
    }
};
