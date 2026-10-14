class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s)

        for i in range(n):
            l = i
            r = i
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        i = 0
        for i in range(n-1):
            l = i
            r = i + 1
            while l >= 0 and r < n:
                if s [l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else:
                    break

        return ans













