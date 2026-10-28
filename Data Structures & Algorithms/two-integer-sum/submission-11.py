class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(n,i) for i,n in enumerate(nums)]
        left = 0
        right = len(arr) - 1
        arr = sorted(arr)
        while(left <= right) :
            summ = arr[left][0] + arr[right][0]

            if (summ < target):
                left +=1
            elif (summ > target):
                right -=1
            else:
                return sorted([arr[left][1],arr[right][1]])

