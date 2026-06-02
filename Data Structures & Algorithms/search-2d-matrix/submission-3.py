class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows*cols) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            # Division by cols gives us the row number
            # Modulo by cols gives us the index position in that specific row
            num = matrix[mid // cols][mid % cols]

            if num < target:
                l = mid + 1
            elif num > target:
                r = mid - 1
            else:
                return True

        return False