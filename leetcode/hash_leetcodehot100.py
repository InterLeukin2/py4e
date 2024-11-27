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

#128 最长连续序列
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0     # 记录最长连续序列的长度
        num_set = set(nums)     # 记录nums中的所有数值
        for num in num_set:
            # 如果当前的数是一个连续序列的起点，统计这个连续序列的长度
            if (num - 1) not in num_set:
                seq_len = 1     # 连续序列的长度，初始为1
                while (num + 1) in num_set:
                    seq_len += 1
                    num += 1    # 不断查找连续序列，直到num的下一个数不存在于数组中
                res = max(res, seq_len)     # 更新最长连续序列长度
        return res

#45 字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)  # sorted(s) 相同的字符串分到同一组
        return list(d.values())


