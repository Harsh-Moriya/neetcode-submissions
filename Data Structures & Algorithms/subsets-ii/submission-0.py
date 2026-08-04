class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res