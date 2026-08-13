class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, curr):
            # Base case: Current path has alphabets equal to the digits count
            if i == len(digits):
                res.append("".join(curr))
                return

            # Get the characters for the current digit
            chars = digitToChars[digits[i]]

            # Iterate over the characters
            for c in chars:
                # Add the char to the current path
                curr.append(c)
                # Explore the next digit
                backtrack(i + 1, curr)
                # Backtrack: Remove the newly added char so as to not contaminate the path
                curr.pop()

        backtrack(0, [])

        return res