class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # make a dictionary of the numbers and their count
        # compare according to that

        dictt = {}

        for v in nums:
            if v in dictt:
                dictt[v] +=1
            else:
                dictt[v] =1

        key_list = list(dictt.keys())

        revv = sorted(key_list,key =lambda x : dictt[x],reverse = True)

        return revv[:k]
        