class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        dictt = {"(" :")",
        "{" : "}"
        ,"[":"]"}

        for c in s:
            if c in dictt.keys():
                arr.append(c) 
            else:

                if len(arr) == 0:
                    return False
                if c == dictt[arr[-1]]:
                    arr.pop()
                else:
                    return False

        if len(arr) != 0:
            return False
        else:
            return True
            


        
        