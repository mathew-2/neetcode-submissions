class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictt = {}

        for i,val in enumerate(numbers):
            if target - val in dictt:
                return sorted([dictt[target - val] + 1,i + 1])
            else : 
                dictt[val] = i

        