class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt = {}

        for n in nums:
            if n not in dictt:
                dictt[n] = 1
            else :
                dictt[n] +=1
                return True
        
        return False
        
        
        