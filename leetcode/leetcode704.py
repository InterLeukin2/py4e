"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""
"""from unittest.mock import right

from dask.array import left_shift
from docutils.nodes import target

#我写的
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return None
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
"""

#代码随想录解法
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left=0
        right=len(nums)
        while left <= right:
            middle = left + (right - left) // 2 #防止溢出
            if nums[middle] > target:
                right = middle  # target 在左区间，在[left, middle)中
            elif nums[middle] < target:
                left = middle + 1  # target 在右区间，在[middle + 1, right)中
            else:
                return middle  # 数组中找到目标值，直接返回下标
        return -1  # 未找到目标值

nums=[2,3,5,6,8,9]
target=5
Solution=Solution()
a = Solution.search(nums,target)
print(a)
