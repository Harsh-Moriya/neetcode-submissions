class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Process first and last rows
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        # Process first and last cols
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        # Now whetever 'Os' are left flip them to 'X' and 'Ts' to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"