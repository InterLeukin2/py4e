"""给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

"""

class solution:
    def fun(self, T: int, nums:list[int])->int:
        l=len(nums)
        L=0
        R=0
        min_len=float('inf')
        cur_sum=0
        while R< l:
            cur_sum+= nums[R]
            while cur_sum >= T:
                #min_len=min(min_len,cur_sum)
                min_len = min(min_len, R - L + 1)
                cur_sum-= nums[L]
                L += 1#！！！之前和上一步写反了难怪不行，感觉这应该是个固定步骤
            R +=1
            #return min_len if min_len!= 0 else 0
        return min_len if min_len != float('inf') else 0


nums=[2,3,1,2,4,3]
solution=solution()
T=7
a=solution.fun(T,nums)
print(a)


