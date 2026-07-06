class Solution:
    def minAnagramLength(self, s: str) -> int:
        # What defines a concatenation?
        # A string that cannot be reproduced without a certain # of digits
        # abba = 2, aabb = 4, cdef = 4
        for i in range(len(s)):
            if i == 0:
                continue
            if len(s) % i != 0:
                continue
            map1 = {}
            temp1 = s[0:i]
            for c in temp1:
                map1[c] = map1.get(c, 0) + 1
            t = 2
            count = 0
            while t*i <= len(s):
                map2 = {}
                temp2 = s[(t-1)*i:t*i]
                for c in temp2:
                    map2[c] = map2.get(c, 0) + 1
                if map1 != map2:
                    count+=1
                    break
                t+=1
            if count == 0:
                return i
        return len(s)
            

        