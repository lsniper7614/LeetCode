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
        for item_a in nums:
            for item_b in nums:
                if item_a + item_b == target:
                    item_a_index = nums.index(item_a)
                    item_b_index = nums.index(item_b)

                    return [item_a_index, item_b_index]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = Solution().twoSum(nums, target)
    print(res)

