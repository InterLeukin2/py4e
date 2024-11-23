#283 移动零
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow]=nums[fast]
                slow+=1
        for i in range(slow, len(nums)):
            nums[i]=0
        return nums

nums=[0,2,3,0,5]
solution=Solution()
a=solution.moveZeroes(nums)
print(a)

#11.盛最多水的容器
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            h = min(height[left],height[right])
            w = right - left
            area = h * w
            res = max(res,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res

#15.三数之和
class Solution:
    def threeSum(self, nums: list[int]) -> list[List[int]]:
        abc=[]
        if not list or len(nums) < 3:
            return abc
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                sum=nums[i]+nums[left]+nums[right]
                if sum == 0:
                    abc.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left]==nums[left+1]:
                        left+=1
                    while left < right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sum > 0:
                    right -= 1
                else :
                    sum < 0
                    left += 1
        return abc

#42 接雨水
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()  # 栈用于存储高度的索引
        result = 0  # 最终的存水量

        for i, h in enumerate(height):
            # 当当前高度大于栈顶高度时
            while stack and height[i] > height[stack[-1]]:
                # 获取底部索引并弹出栈顶
                bottom = stack.pop()

                # 如果弹出后栈为空，说明没有左边界，无法形成水池
                if not stack:
                    break

                # 计算当前的高度差和宽度差
                h = min(height[stack[-1]], height[i]) - height[bottom]
                w = i - stack[-1] - 1

                # 累加水量
                result += h * w

            # 把当前索引压入栈
            stack.append(i)

        return result