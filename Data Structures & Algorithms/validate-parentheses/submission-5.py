class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        dictt = {"}" : "{",
        "]" : "[",
        ")" : "("}

        for c in s:
            if c in dictt.keys():
                if len(arr) == 0 :
                    return False
                if arr[-1] == dictt[c]:
                    arr.pop()
                else:
                    return False

            else:
                arr.append(c)

        if len(arr) == 0:
            return True
        else:
            return False
            


        
        