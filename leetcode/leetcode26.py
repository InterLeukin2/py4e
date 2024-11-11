"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在
 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
"""

'''
def insert():#一开始要把参数传进来
    n=len(lst[]) #为什么这样不行
    #
    while i in range(1:n) #for好像可以这样写
        if num[i]==num[i+1]:
            remove(num[i+1]) #人家用pop，害
            i+=1
          return num[i]
#你也没调用函数，后面怎么输出
'''

import timeit

def remove_duplicates(nums):
    # 获取数组长度
    n = len(nums)

    # 外层循环从前往后遍历每个元素
    i = 0
    while i < n - 1:

            if nums[i] == nums[i+1]:
                # 如果找到重复元素，删除它，并更新数组长度
                nums.pop(i+1)
                n -= 1  # 更新长度
            else:
                # 如果没有重复，检查下一个元素
                i += 1


    # 最终返回数组长度
    return len(nums)

# 示例数组
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# 调用函数
new_length = remove_duplicates(nums)

# 输出结果
print("新长度:", new_length)
print("去重后的数组:", nums[:new_length]) #切片


def remove_d(nums):#list是动态数组，所以可以原地修改，不改变原数组长度
    if not nums:#if not nums: 可以用来判断任何类型的容器（如列表、字符串、字典等）是否为空。
        return 0

    # 慢指针，用来存储不重复的元素位置
    i = 0#为啥不用初始化j呢，因为在for初始化了，就像前面那个num直接传到参数里了

    # 快指针遍历数组
    for j in range(1, len(nums)):
        # 当发现一个新元素时
        if nums[j] != nums[i]:
            i += 1  # 移动慢指针
            nums[i] = nums[j]  # 将新元素放到慢指针的位置

    # 去重后数组长度为 i + 1
    return i + 1




nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_le = remove_d(nums)

print("新长度2:", new_le)
print("去重后的数组2:", nums[:new_le])

#leetcode提交第一次
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):#这里用“，”分开，不是“：”
            if nums[i] != nums[j]:#这里不要忘了写 if
                i += 1
                nums[i] = nums[j]

        return i + 1

#官方题解
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow



