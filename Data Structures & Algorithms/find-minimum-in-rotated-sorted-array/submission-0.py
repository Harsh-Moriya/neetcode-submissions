class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            # If the current window is already sorted, the leftmost element is definitely the minimum.
            if nums[l] < nums[r]:
                return nums[l]
                
            mid = (l + r) // 2

            # If left half is sorted, the min MUST be in the right half
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                # If left half is not sorted, the min is in the left half
                r = mid

        return nums[l]