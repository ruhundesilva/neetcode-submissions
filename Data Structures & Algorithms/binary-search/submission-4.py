class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = ((r + l) // 2)
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        return -1