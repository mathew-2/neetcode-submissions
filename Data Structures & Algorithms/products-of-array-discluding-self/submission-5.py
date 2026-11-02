class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n) and space complexity (n)
        prefix = 1
        postfix = 1
        arr = [1]*len(nums)

        for i in range(len(nums)):
            arr[i]*=prefix
            prefix*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            arr[i] *= postfix
            postfix *=nums[i]

        return arr
        

            
        
        