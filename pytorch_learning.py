class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):  # 遍历数组
            min_index = i  # 假设当前元素为最小值
            for j in range(i + 1, n):  # 找到从 i 到 n 的最小值
                if nums[j] < nums[min_index]:
                    min_index = j  # 更新最小值索引

            # 交换元素位置
            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums


'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        min = i
        for j in range(n):
            if a[j] < a[min]:
                min = j
        a[i],a[min]= a[min],a[i]
        print(nums)
sortArray(nums)


'''