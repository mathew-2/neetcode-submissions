class Solution:
    def isPalindrome(self, s: str) -> bool:

        t = s.lower()

        t = "".join(c for c in t if c.isalnum())

        left = 0
        right = len(t) -1

        while(left <= right):
            if t[left]==t[right]:
                left +=1
                right-=1
            else:
                return False
        return True


        