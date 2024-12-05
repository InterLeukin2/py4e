#53 最大数组和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

#56 合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:  # 可以合并，ans[-1][1]:嵌套结构最后一个值里的第2个数
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
            else:  # 不相交，无法合并
                ans.append(p)  # 新的合并区间
        return ans
#189 轮转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #这个反转的辅助函数完全可以直接记下来
        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n  # 轮转 k 次等于轮转 k%n 次
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
#这道题的做法就是这3个reverse，先反转整个数组，再反转前k个，再反转后n-k个

#238.除自身以外数组的乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n  # 初始化了一个长度是n的数组，之所以用1是为了变成这样【1，1，1】
        suf = [1] * n
        for i in range(1, n):  # 不包括n所以到n
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):  # 循环到索引 0 为止（stop 是开区间，不包含 -1）。，开头是n-1，但suf是n-2
            suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, suf)]

#41.缺失的第一个正数
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: 将每个数字放到正确的位置
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 交换 nums[i] 和 nums[nums[i]-1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: 找出第一个错误位置
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: 所有数字都在正确位置
        return n + 1

        # gpt写的，比市面上的答案都简单易懂