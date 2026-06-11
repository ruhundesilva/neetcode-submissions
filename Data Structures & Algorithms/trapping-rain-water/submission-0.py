class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        maxVal = 0
        for i in range(n):
            maxLeft[i] = maxVal
            maxVal = max(maxVal, height[i])
        
        maxVal = 0
        for i in range(n - 1, -1, -1):
            maxRight[i] = maxVal
            maxVal = max(maxVal, height[i])
        
        rain = 0
        
        for i in range(n):
            if min(maxLeft[i], maxRight[i]) - height[i] > 0:
                rain += min(maxLeft[i], maxRight[i]) - height[i]
        
        return rain