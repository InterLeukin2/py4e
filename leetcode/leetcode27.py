"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。
元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的
其余元素和 nums 的大小并不重要。
返回 k。

"""
'''自己写的没通过，
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(0,len(nums)):
            if nums[i] == val:
                i += 1
                nums[i] = nums[i+1]

            return nums
        
'''

# 通过的答案，chatgpt修改版
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0  # 慢指针，指向当前有效的元素位置
        for j in range(len(nums)):  # 快指针，遍历数组
            if nums[j] != val:  # 如果当前元素不等于待删除的元素
                nums[i] = nums[j]  # 将当前元素放到慢指针位置
                i += 1  # 移动慢指针
        return i  # 返回有效元素的个数