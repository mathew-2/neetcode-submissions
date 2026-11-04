class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = {}

        for i in range(len(numbers)):
            if target - numbers[i] in arr.keys():
                return sorted([i + 1,arr[target-numbers[i]] + 1])
            else:
                arr[numbers[i]] = i



        