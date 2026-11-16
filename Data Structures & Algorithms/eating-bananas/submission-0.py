import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # order of piles doesnt matter ,only thing matters is which k to use

        l,r = 1,max(piles)

        res = r

        #find k for which no of hrs is < than k
        # do a binary search to get value for which 
        while(l <= r):
            k = (l+r)//2
            # calculate hours for each k value
            hours = 0
            for p in piles:
                hours+= math.ceil(p/k)

            if hours<=h:
                res = min(res,k)
                r = k -1
            else:
                l = k + 1

        
        return res

        