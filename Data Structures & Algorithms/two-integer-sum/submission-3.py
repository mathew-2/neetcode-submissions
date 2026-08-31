class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i,v in enumerate(nums):

            diff = target - v
            if diff in h:
                return [h[diff],i]
            h[v] = i

        return 
        #     else:
        #         h[v].append(i)
        
        # for v in nums:
        #     if target - v in h and target-v != v:
        #         return [h[v][0],h[target - v][0]]
        #     elif target -v == v:
        #         return [h[v][0],h[v][1]]
