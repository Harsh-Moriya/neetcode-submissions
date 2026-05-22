class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        l = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)

        return length