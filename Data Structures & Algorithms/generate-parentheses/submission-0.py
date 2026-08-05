class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, openN, closeN):
            # Base case, if pairs equal n
            if openN == closeN == n:
                s = "".join(curr)
                res.append(s)
                return

            # If count of opening brackets is less than n then a opening bracket can be added
            if openN < n:
                curr.append("(")
                backtrack(curr, openN + 1, closeN)
                # Backtrack
                curr.pop()

            # If count of closing brackets is less than opened ones than a closing bracket can be added
            if closeN < openN:
                curr.append(")")
                backtrack(curr, openN, closeN + 1)
                # Backtrack
                curr.pop()

        backtrack([], 0, 0)

        return res