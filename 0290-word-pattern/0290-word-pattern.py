class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        index = 0
        start = 0
        mapP = {} # map subString : pattern[index] aka "dog : a"
        for i, char in enumerate(s):
            if index > len(pattern)-1:
                return False
            if char == " " or i == (len(s)-1):
                if i == len(s)-1:
                    subString = s[start:i+1]
                else:
                    subString = s[start:i]
                if subString in mapP and mapP[subString] == pattern[index]:
                    index+=1
                    start = i+1
                    continue
                elif subString not in mapP and pattern[index] not in mapP.values():
                    mapP[subString] = pattern[index]
                else:
                    return False
                index+=1
                start = i+1
        if index == len(pattern):
            return True
        return False

        #if subString not in mapP and pattern[index] in mapP.values():
                    # return False