class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot = {}
        ttos = {}
        i=0
        for char in t:
            if char in ttos and s[i] != ttos[char]:
                return False
            elif s[i] in stot and char != stot[s[i]]:
                return False
            
            ttos[char] = s[i]
            stot[s[i]] = char
            i+=1
        return True