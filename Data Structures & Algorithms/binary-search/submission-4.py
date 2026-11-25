class Solution:
    def search(self, nums: List[int], target: int) -> int:
       l,r = 0 ,len(nums) - 1

       while l<=r :
        midd = (l + r)//2
        if nums[midd] > target:
            r = midd - 1
        elif nums[midd] < target:
            l = midd + 1
        else:
            return midd
        

       return -1
        

        