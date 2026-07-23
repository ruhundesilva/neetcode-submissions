class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def foo(curr):
            if len(curr) == n:
                res.append(curr.copy())
                return
            
            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                foo(curr)
                curr.pop()
        foo([])
        return res
        