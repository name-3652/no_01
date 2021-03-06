'''
7. 整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
    输入: 123
    输出: 321

示例 2:
    输入: -123
    输出: -321

示例 3:
    输入: 120
    输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            res = int(("-" + str(x).rstrip("0")[::-1]).rstrip("-"))
        elif x == 0:
            res = 0
        else:
            res = int(str(x).rstrip("0")[::-1])

        if -2147483648 < res < 2147483647:
            return res
        else:
            return 0


try:
    test = Solution()
    assert test.reverse(x=1534236469) == 0, "1534236469 reverse 9646324351"
    assert test.reverse(x=123) == 321, "123 reverse 321"
    assert test.reverse(x=-123) == -321, "-123 reverse -321"
    assert test.reverse(x=120) == 21, "120 reverse 21"
except AssertionError as e:
    print(e)