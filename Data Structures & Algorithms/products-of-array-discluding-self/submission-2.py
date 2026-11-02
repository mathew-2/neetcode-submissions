class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        no_of_zeros=0
        arr = [1]*len(nums)
        for n in nums:
            if n!=0:
                prod*=n
            else:
                no_of_zeros+=1
        
        for i,n in enumerate(nums):
            if n!=0 and no_of_zeros==0:
                arr[i]=int(prod/n)
            elif n==0 and no_of_zeros==1:
                arr[i]=int(prod)
            else:
                arr[i]= 0


        return arr
        

            
        
        