from collections import deque
from collections import Counter

#56
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_count = defaultdict(int)  # 用 defaultdict 来避免键不存在的情况
        prefix_sum_count[0] = 1  # 初始情况下，前缀和为 0 出现过一次（表示从头开始）
        count = 0

        for num in nums:
            prefix_sum += num  # 计算当前的前缀和

            # 检查是否存在前缀和为 prefix_sum - k
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]  # 找到符合条件的子数组

            # 更新 prefix_sum_count，记录当前前缀和出现的次数
            prefix_sum_count[prefix_sum] += 1

        return count



#209
class Solution:
    breakpoint()
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        q = deque()  # 双端队列
        for i, x in enumerate(nums):
            # 1. 入
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            q.append(i)  # 入队
            # 2. 出
            if i - q[0] >= k:  # 队首已经离开窗口了
                q.popleft()
            # 3. 记录答案
            if i >= k - 1:
                # 由于队首到队尾单调递减，所以窗口最大值就是队首
                ans.append(nums[q[0]])
        return ans

nums=[1,3,-1,-3,5,3,6,7]
k=3
Solution=Solution()
a = Solution.maxSlidingWindow(nums,k)
print(a)

#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        cnt_s = Counter()  # s 子串字母的出现次数
        cnt_t = Counter(t)  # t 中字母的出现次数

        left = 0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt_s[c] += 1  # 右端点字母移入子串
            while cnt_s >= cnt_t:  # 涵盖
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                cnt_s[s[left]] -= 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


