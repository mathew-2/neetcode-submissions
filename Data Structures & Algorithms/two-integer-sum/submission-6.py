class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i,v in enumerate(nums):
            if v not in h:
                h[v] = [i]
            else:
                h[v].append(i)
        
        for i, v in enumerate(nums):
            if target - v in h and target-v != v:
                res = [i, h[target - v][0]]
                # res.sort()
                return res
            elif target -v == v and len(h[v]) > 1:
                return [h[v][0],h[v][1]]