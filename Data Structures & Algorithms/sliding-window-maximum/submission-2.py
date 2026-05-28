class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []

        for r in range(len(nums)):
            # Pop until all smaller elements are removed
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Check if index at the front is in window
            l = r - k + 1
            if q[0] < l:
                q.popleft()
            
            # k is count r is index that's why -1
            if r >= k - 1:
                res.append(nums[q[0]])

        return res