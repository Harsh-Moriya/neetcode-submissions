class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            length = max(length, r - l + 1)

        return length