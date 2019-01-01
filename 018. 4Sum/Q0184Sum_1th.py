#!/bin/python3

"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""



class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lengthOfNums = len(nums)
        sorted_nums = sorted(nums)
        solution_set = set()
        for i in range(lengthOfNums-3):
            for j in range(i+1, lengthOfNums-2):
                m, n = j+1, lengthOfNums-1
                while m < n:
                    temp_target = sorted_nums[i] + sorted_nums[j] +\
                                sorted_nums[m] + sorted_nums[n]
                    if temp_target == target:
                        solutionOfTarget = tuple((sorted_nums[i], sorted_nums[j],
                                        sorted_nums[m], sorted_nums[n]))
                        solution_set.add(solutionOfTarget)
                    if temp_target <= target:
                        m += 1
                    else:
                        n -= 1
        solution_list = list(solution_set)

        return solution_list
        

if __name__ == "__main__":
    nums = [-3,-1,0,2,4,5]
    target = 1
    res = Solution().fourSum(nums, target)
    print("res:", res)
    pass

