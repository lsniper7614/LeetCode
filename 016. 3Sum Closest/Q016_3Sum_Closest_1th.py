#!/bin/python3

"""
This is the my own first edition and it's timeout

The time-complexity of the program is **?**
"""


"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lengthOfnums = len(nums)
        abs_err = float('inf')
        closet_target = 0
        for i in range(lengthOfnums):
            for j in range(i+1, lengthOfnums):
                for k in range(j+1, lengthOfnums):
                    temp_target = nums[i] + nums[j] + nums[k]
                    if abs(target - temp_target) < abs_err:
                        abs_err = abs(target - temp_target)
                        closet_target = temp_target
        
        return closet_target
 
 

if __name__ == "__main__":
    nums = [-1,2, 1, -4]
    target = 1
    res = Solution().threeSumClosest(nums, target)
    print("res:", res)
    pass
 
 
