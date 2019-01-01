#!/bin/python3

"""
This is the my own 2th edition and it's accepted.

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
        sorted_nums = sorted(nums)
        lengthOfnums = len(nums)
        abs_error = float('inf')
        for i in range(lengthOfnums-2):
            j, k = i+1, lengthOfnums - 1
            while j < k:
                temp_target = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if temp_target == target:
                    return temp_target
                elif abs(target - temp_target) < abs_error:
                    abs_error = abs(target - temp_target)
                    closet_target = temp_target
                
                if temp_target < target:
                    j += 1
                else:
                    k -= 1
        
        return closet_target
 
 

if __name__ == "__main__":
    nums = [-1,2, 1, -4]
    target = 1
    res = Solution().threeSumClosest(nums, target)
    print("res:", res)
    pass
 
 
