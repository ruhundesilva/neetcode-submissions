class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        seenSet = set()
        maxLength = 0
        for num in nums:
            currLength = 1
            if num in seenSet:
                continue

            k = num - 1
            while k in numsSet:
                currLength += 1
                seenSet.add(k)
                k -=1
            
            k = num + 1
            while k in numsSet:
                currLength += 1
                seenSet.add(k)
                k += 1
            
            maxLength = max(currLength, maxLength)
        return maxLength