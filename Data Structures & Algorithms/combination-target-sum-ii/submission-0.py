class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Sort to allow skippig of same values easily
        candidates.sort()

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= len(candidates):
                return


            # Include current index candidate in the combination, but skip it over when passing index as we can't reuse the same candidate
            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])

            # Exclude current candidate, and skip over same value elements
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)

        return res