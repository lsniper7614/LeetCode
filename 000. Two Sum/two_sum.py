#!python3

"""
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a_index, a in enumerate(nums):
            for b_index, b in enumerate(nums[a_index + 1:]):
                if a + b == target:
                    return [a_index, a_index + b_index + 1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = Solution().twoSum(nums, target)
    print(res)

