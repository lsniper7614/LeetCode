#!python3
"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_long_str = ''
        for i, item_i in enumerate(s):
            sub_str = item_i
            for j, item_j in enumerate(s[i + 1:]):
                if item_j not in sub_str:
                    sub_str += item_j
                else:
                    break

            if len(sub_str) > len(sub_long_str):
                sub_long_str = sub_str

        return len(sub_long_str)


if __name__ == '__main__':
    # s = "abcabcbb"
    # s = "bbbbb"
    s = "pwwkew"
    # s = 'c'
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
