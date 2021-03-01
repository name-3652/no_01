'''
1480. 一维数组的动态和
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

 

示例 1：
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

示例 2：
输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。

示例 3：
输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
 

提示：
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

'''
class Solution:
    def runningSum(self, nums:list):
        """
        :param nums: list
        :return: list
        """
        sum_list = nums
        for m in range(-1, -len(nums)-1,-1):
            sum_list[m] = sum(nums[m::-1])
        return sum_list

    def runningSum_eg(self, nums: list):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
if __name__ == '__main__':
    try:
        test = Solution()
        assert (test.runningSum([1,2,3,4]) == [1,3,6,10]), "1,3,6,10 False"
        assert test.runningSum([1,1,1,1,1]) == [1,2,3,4,5], "1,2,3,4,5 False"
        assert test.runningSum([3,1,2,10,1]) == [3,4,6,16,17], "3,4,6,16,17 False"
    except AssertionError as e:
        print(e)
