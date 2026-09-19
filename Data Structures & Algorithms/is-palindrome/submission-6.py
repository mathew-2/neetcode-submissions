class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.replace(" ","")
        t=t.lower()
        t= "".join(c for c in t if ((ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z'))) or (ord(c) >= ord('0') and ord(c) <= ord('9')))
        i = 0
        j = len(t)-1
        while (i <= j):
            if (t[i]!=t[j]):
                return False
            i+=1
            j-=1
        return True


        