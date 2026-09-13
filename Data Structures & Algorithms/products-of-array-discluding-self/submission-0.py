class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no of zeros
        # then calculate total product
        # if no of zeros = 0 --> divide / that certain value thats all
        # else zero


        no_of_zeros = 0
        tot_prod = 1


        for val in nums:
            if val == 0:
                no_of_zeros +=1

            else:
                tot_prod *= val

        res = [0]*len(nums)
        i = 0
        while(i < len(nums)):
            if (nums[i]==0 and  no_of_zeros -1 == 0):
                res[i] = tot_prod
            elif(nums[i]==0 and no_of_zeros -1 !=0):
                res[i] = 0
            elif(nums[i]!=0 and no_of_zeros !=0):
                res[i] = 0
            else:
                res[i] = int(tot_prod/nums[i])

            i+=1


        return res

            
        
        