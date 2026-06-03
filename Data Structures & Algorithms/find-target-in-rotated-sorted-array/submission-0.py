class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Could be a single value array
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Right is sorted
            if nums[mid] < nums[r]:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1  # Look to the left
                else:
                    l = mid + 1  # Look to the right
            # Left is sorted
            else:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1  # Look to the right
                else:
                    r = mid - 1  # Look to the left

        return -1