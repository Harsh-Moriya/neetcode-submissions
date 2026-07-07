class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, subset):
            if index == len(nums):
                res.append(list(subset))
                return

            # Include path
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Exclude path
            subset.pop()
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res