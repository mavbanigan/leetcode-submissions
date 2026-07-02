class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setStr = set()
        l = 0
        r = 0
        res=0
        while r < len(s):
            while s[r] in setStr:
                setStr.remove(s[l])
                l+=1
            setStr.add(s[r])
            counter = r-l+1
            res = max(res, counter)
            r+=1
        return res
            
            
        