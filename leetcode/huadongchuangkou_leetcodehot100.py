
#滑动窗口 3，438
#3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        start=0
        hash=set()
        for end in range(len(s)):
            while s[end] in hash:
                hash.remove(s[start])
                start+=1
            hash.add(s[end])
            maxlen=max(maxlen,end-start+1)
        return maxlen






from pyflakes.checker import counter



#438
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = 0
        cnt_p = counter(p)
        cnt_s =  counter()
        for right, c in enumerate(p):
            cnt_s[c]+=1
            left = right - len(p) + 1
            if left < 0:
                continue
            if cnt_s == cnt_p:
                result.append(left)
            cnt_s[s[left]] -=1
        return result

