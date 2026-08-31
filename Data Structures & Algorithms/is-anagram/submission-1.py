class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = {}
        h2 = {}

        for v in s:
            h1[v] = h1.get(v,0) + 1

        for v in t:
            h2[v] = h2.get(v,0) + 1

        return h1 == h2
        