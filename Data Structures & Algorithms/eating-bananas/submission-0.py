class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = l + ((r - l) // 2)
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(float(pile) / mid)
            if timeTaken <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

