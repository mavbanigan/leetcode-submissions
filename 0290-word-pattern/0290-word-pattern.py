class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapP = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(words)):
            if words[i] not in mapP:
                if pattern[i] in mapP.values():
                    return False
                mapP[words[i]] = pattern[i]
            elif mapP[words[i]] != pattern[i]:
                return False
        return True