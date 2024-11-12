"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数
用了2种方法，动态规划不是最优解
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        for i in nums:
            if len(nums) == 1 and nums[0] == 0:
                return 0
        m_one = 0
        result= 0
        for i in nums:
            #if nums[i] == 1:  不对
            # for i in nums 循环中的 nums[i] == 1:
            # 你应该直接使用 i（即 nums 中的元素），而不是 nums[i]。
            # 因为 i 已经是 nums 中的值，不需要通过 nums[i] 再次访问。
            if i == 1:
                m_one = m_one + 1
            #if m_one != 0:
                #result = m_one
            else:
                result = max(result, m_one)
                m_one = 0
       # result = max(result, m_one)
       #   处理最后的连续
        #1：如果数组的最后部分是连续的
        #1，循环结束后没有机会更新
        #result，所以你需要在循环结束后，再执行一次
        #result = max(result, m_one)
        #来确保结果的正确性。
            result = max(result, m_one) #最后还要更新一下
            return result
nums=[0,0,1,0,1,1,1]

#a=findMaxConsecutiveOnes(nums) 错误原因：没有指定类，而且有大小写

# 创建 Solution 类的实例
Solution=Solution()
a = Solution.findMaxConsecutiveOnes(nums)
print(a)

#优化的写法 chatgpt写的
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0

        return max(max_count, current_count)

#动态规划
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # 初始化 dp 数组，用来记录每个位置的连续1的长度
        dp = [0] * len(nums)
        dp[0] = nums[0]  # 如果 nums[0] 是 1，那么 dp[0] = 1，否则为 0

        max_count = dp[0]  # 初始化最大连续1的数量，初始为 dp[0] 这一步好几次都没考虑到，
                            #如果没有这一步，会导致【1，0】，这样的例子不通过
        # 从第二个元素开始遍历 nums 数组
        for i in range(1, len(nums)):#len的长度就是比索引大1，所以不用加
            if nums[i] == 1:
                dp[i] = dp[i - 1] + 1  # 如果是 1，连续1的数量加 1
            else:
                dp[i] = 0  # 如果是 0，连续1的数量重置为 0
            # 更新最大连续1的数量
            max_count = max(max_count, dp[i])
        return max_count
