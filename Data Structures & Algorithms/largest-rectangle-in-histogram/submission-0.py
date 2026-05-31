class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic Increasing
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            # To track where the current one starts if it extends to the left
            start = i

            while stack and stack[-1][1] > h:
                stackI, stackH = stack.pop()
                width = i - stackI
                max_area = max(max_area, stackH * width)
                start = stackI

            stack.append((start, h))

        # Clear out the entries that never found their right boundary (so right boundary = end index)
        for i, h in stack:
            width = len(heights) - i
            max_area = max(max_area, h * width)

        return max_area