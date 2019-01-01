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
        left_index = 0
        right_index = len(height) - 1
        max_container = 0
        
        while left_index < right_index:
        
            width = right_index - left_index
            
            if height[left_index] > height[right_index]:
                max_container = max(max_container, height[right_index] * width)
                right_index -= 1
            else:
                max_container = max(max_container, height[left_index] * width)
                left_index += 1
        
        return max_container


if __name__ == "__main__":
    input_list = [1,8,6,2,5,4,8,3,7]
    res = Solution().maxArea(height=input_list)
    print("res:", res)
    pass
    
    
