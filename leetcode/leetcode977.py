"""class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in nums:#这里也不对
            i=i*i # 修改点：对 nums[i] 求平方并直接赋值回 nums[i]
            for j in range(len(nums)-1):
                while j <= len(nums)-1:
                    if nums[j]>nums[j+1]:
                        nums[j+1]=nums[j]
                        j=j+1
            return nums
"""
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]  # 修改点：对 nums[i] 求平方并直接赋值回 nums[i]

        # 使用排序算法对平方后的数组进行非递减排序
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):# 比较相邻元素，如果前面的元素比后面的元素大，就交换它们

                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]  # 修改点：交换顺序确保非递减排序
        return nums  # 返回排序后的数组

# 测试代码
nums = [-2, 0, 4, 7]
solution = Solution()
a = solution.sortedSquares(nums)
print(a)  # 输出 [0, 4, 16, 49]



nums=[-2,0,4,7]
Solution=Solution()
a = Solution.sortedSquares(nums)
print(a)

#版本一）双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [float('inf')] * len(nums) # 需要提前定义列表，存放结果
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: # 左右边界进行对比，找出最大值
                res[i] = nums[r] ** 2
                r -= 1 # 右指针往左移动
            else:
                res[i] = nums[l] ** 2
                l += 1 # 左指针往右移动
            i -= 1 # 存放结果的指针需要往前平移一位
        return res


#（版本三）暴力排序法+列表推导法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)
#(版本四) 双指针+ 反转列表
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #根据list的先进排序在先原则
        #将nums的平方按从大到小的顺序添加进新的list
        #最后反转list
        new_list = []
        left, right = 0 , len(nums) -1
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                new_list.append(nums[right] ** 2)
                right -= 1
            else:
                new_list.append(nums[left] ** 2)
                left += 1
        return new_list[::-1]