class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Chars = [0] * 26
        for c in s1:
            s1Chars[ord(c) - ord("a")] += 1
        
        s2WindowChars = [0] * 26
        n = len(s1)
        for i in range(n):
            s2WindowChars[ord(s2[i]) - ord("a")] += 1

        if s2WindowChars == s1Chars:
            return True
        
        l, r = 0, n - 1
        while r < len(s2) - 1:
            s2WindowChars[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r += 1
            s2WindowChars[ord(s2[r]) - ord("a")] += 1
            if s2WindowChars == s1Chars:
                return True
        return False
            