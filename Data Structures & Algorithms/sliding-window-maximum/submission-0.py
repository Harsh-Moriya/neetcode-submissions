class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []

        for r in range(k, len(nums) + 1):
            maxNum = -float('inf')

            for i in range(l, r):
                maxNum = max(maxNum, nums[i])

            res.append(maxNum)

            l += 1

        return res