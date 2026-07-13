class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l, r = 0, 1
        max_count = 1
        mapS={}
        mapS[s[l]] = l
        while r < len(s):
            if s[r] in mapS:
                l = max(l, mapS[s[r]] + 1)
            mapS[s[r]] = r
            max_count = max(max_count, r - l + 1)
            r+=1
        return max_count