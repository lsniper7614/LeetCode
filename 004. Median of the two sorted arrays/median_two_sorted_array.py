#!python3
"""
nums1 = [1, 3]
nums2 = [2]

中位数是 2.0

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
"""

"""
Question:
题目中要求的算法时间复杂度为 O(log (m+n))
但是不懂怎么处理
但是提交审核通过了
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined_sorted_array = nums1 + nums2
        combined_sorted_array.sort()
        if len(combined_sorted_array) % 2 == 0:
            # even num
            pre_median_index = int(len(combined_sorted_array) / 2) - 1
            post_median_index = int(len(combined_sorted_array) / 2)
            median = (combined_sorted_array[pre_median_index] + combined_sorted_array[post_median_index]) / 2
        else:
            # Odd num
            median_index = int((len(combined_sorted_array) - 1) / 2)
            median = combined_sorted_array[median_index]

        return median


if __name__ == '__main__':
    # nums1 = [1, 3]
    # nums2 = [2]

    nums1 = [1, 2]
    nums2 = [3, 4]

    res = Solution().findMedianSortedArrays(nums1, nums2)
    print(res)

