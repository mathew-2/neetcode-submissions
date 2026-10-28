class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # value : index
        for i ,n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return sorted([i,prevmap[diff]])
            prevmap[n] = i

