class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                w = j - i
                h = min(height[i], height[j])
                prod = h * w
                area = max(area, prod)
        return area