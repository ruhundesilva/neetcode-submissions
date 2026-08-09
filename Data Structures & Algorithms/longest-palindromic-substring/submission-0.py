class Solution:
    def longestPalindrome(self, s: str) -> str:
        starti = 0
        bestLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > bestLen:
                    starti = l
                    bestLen = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > bestLen:
                    starti = l
                    bestLen = r - l + 1
                l -= 1
                r += 1
        return s[starti : starti + bestLen]