class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = {}
        h2 = {}

        for i in range(len(s)):
            h1[s[i]] = h1.get(s[i],0) + 1
            h2[t[i]] = h2.get(t[i],0) + 1

        for c in h1:
            if h1[c] != h2.get(c,0):
                return False

        return True
        