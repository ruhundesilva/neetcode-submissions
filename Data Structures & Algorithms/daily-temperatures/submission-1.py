class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack:
                while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                    prevtemp, index = stack.pop()
                    res[index] = i - index
            stack.append((temperatures[i], i))
        return res