class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowI = None

        for i, row in enumerate(matrix):
            if row and (target >= row[0]) and (target <= row[-1]):
                rowI = i

            if rowI != None:
                break

        if rowI == None:
            return False

        row = matrix[rowI]
        l, r = 0, len(row) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True

        return False