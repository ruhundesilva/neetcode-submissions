class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxVol = 0
        while left < right:
            vol = min(heights[left], heights[right]) * (right - left)
            if vol > maxVol:
                maxVol = vol
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1
        return maxVol