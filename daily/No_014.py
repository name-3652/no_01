'''
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        ss = list(map(set, zip(*strs)))
        for i in ss:
            x = list(i)
            if len(x) > 1:
                break
            res += x[0]
        return res
try:
    test = Solution()
    assert test.longestCommonPrefix(["flower","flow","flight"]) == "fl", '["flower","flow","flight"] is "fl"'
    assert test.longestCommonPrefix(["dog","racecar","car"]) == "", '["dog","racecar","car"] is ""'
except AssertionError as e:
    print(e)