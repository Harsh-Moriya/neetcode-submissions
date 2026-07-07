class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            length = len(res)

            for i in range(length):
                subset = res[i] + [num]
                res.append(subset)

        return res