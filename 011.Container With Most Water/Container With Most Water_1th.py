#!/bin/python3
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
”“”

"""
This is the first edition, and it's timeout

The complexity of time is **？**
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        heightListLength = len(height)
        max_container = 0
        for i in range(heightListLength):
            for j in range(i, heightListLength):
                tempContainerArea = (j - i) * min(height[i], height[j])
                if tempContainerArea > max_container:
                    max_container = tempContainerArea
        
        return max_container


if __name__ == "__main__":
    input_list = [1,8,6,2,5,4,8,3,7]
    res = Solution().maxArea(height=input_list)
    print("res:", res)
    pass
    
    
