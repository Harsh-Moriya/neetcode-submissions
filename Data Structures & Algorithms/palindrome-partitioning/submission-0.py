class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy()) # Copy because we are using a global list which will keep changing
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    sub = s[i:j + 1]
                    part.append(sub)
                    dfs(j + 1)
                    part.pop()

        dfs(0)

        return res

        
    def isPalindrome(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True