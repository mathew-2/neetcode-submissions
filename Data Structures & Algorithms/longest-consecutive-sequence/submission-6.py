class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        numset = set(nums)

        for n in nums:
            # see if a number is a start of a sequence
            if (n-1) not in numset:
                length = 0
                while ((n+length) in numset):
                    length+=1
                    maxlen = max(length,maxlen)

        return maxlen

        