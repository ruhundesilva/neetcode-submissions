class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = right = 0
        longest = 1
        inWindow = set()
        inWindow.add(s[0])

        while right < len(s) - 1:
            right += 1
            while s[right] in inWindow:
                inWindow.remove(s[left])
                left += 1
            inWindow.add(s[right])
            longest = max(right - left + 1, longest)
        return longest