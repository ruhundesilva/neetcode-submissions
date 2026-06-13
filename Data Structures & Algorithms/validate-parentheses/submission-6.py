class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposites = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for string in s:
            if string == "(" or string == "{" or string == "[":
                stack.append(opposites[string])
                continue
            if len(stack) == 0:
                return False
            last = stack.pop()
            if string != last:
                return False
        return len(stack) == 0
            