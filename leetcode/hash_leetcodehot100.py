'''

哈希表数 leetcodehot100总结
两数之和，字母异位词分组，最长连续序列

'''
from leetcode.leetcode704 import target


#49. 两数之和

class Solution:
    breakpoint()
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        records = dict()

        for index, value in enumerate(nums):
            if target - value in records:   # 遍历当前元素，并在map中寻找是否有匹配的key
                return [records[target- value], index]
            records[value] = index    # 如果没找到匹配对，就把访问过的元素和下标加入到map中
        return []

nums=[2,7,11,15]
target=9
solution=Solution()
a=solution.twoSum(nums,target)
print(a)


