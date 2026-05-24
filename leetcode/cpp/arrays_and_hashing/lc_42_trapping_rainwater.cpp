#include <vector>

/**
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * Time complexity: O(n) where n = length of height
 * Space complexity: O(n) where n = length of height
 */
class Solution {
public:
    int trap(std::vector<int>& height) {
        // init our max left and right height arrays
        // the max left height array holds the maximum height
        // to the left of each index i in the height array
        std::vector<int> maxLeftHeight(height.size(), 0);
        // the max right height array holds the maximum height
        // to the right of each index i in the height array
        std::vector<int> maxRightHeight(height.size(), 0);

        // first we will populate the max left height array
        // init the first left height to be the same as the height
        // at that location
        maxLeftHeight[0] = height[0];
        // we loop through all max left heights except the first one
        // because water cannot be contained at the left edge (first index)
        for (int i = 1; i < maxLeftHeight.size(); ++i) {
            // populate the max left height as the larger of either
            // the previous max left height or the current left height
            // for each index i
            maxLeftHeight[i] = std::max(height[i-1], maxLeftHeight[i-1]);
        }

        // first we will populate the max right height array
        // init the last right height to be the same as the height
        // at that location
        maxRightHeight[maxRightHeight.size()-1] = height[height.size()-1];
        // we will loop through all max right heights except the last one
        // in reverse because water cannot be contained at the right edge (last index)
        for (int i = height.size()-2; i > 0; --i) {
            // populate the max right height as the larger of either
            // the previous max right height or the current right height
            // for each index i
            maxRightHeight[i] = std::max(height[i+1], maxRightHeight[i+1]);
        }

        // init the totalArea
        int totalArea = 0;
        // loop through all heights except the first and last ones
        // because water cannot be stored at the edges (first and last indices)
        for (int i = 1; i < height.size()-1; ++i) {
            // compute the area as the difference between the smallest max left/right height
            // and the current height at that index
            int area = std::min(maxLeftHeight[i], maxRightHeight[i]) - height[i];

            // if the area is positive, then water can be contained
            // so add it to the total area
            if (area > 0) {
                totalArea += area;
            }
        }

        // finally, return the total area
        return totalArea;
    }
};
