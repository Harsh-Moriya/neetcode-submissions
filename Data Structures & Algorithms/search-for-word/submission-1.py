class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            # If the path has reach an index same as word length thenit means that all characters in the current path matched the word
            if i == len(word):
                return True

            # Out of bounds or character mismatch, also handes already visited as # will mismatch
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]:
                return False

            # If we reach this point then character matches

            # Mark the position as visited using #
            temp = board[r][c]
            board[r][c] = '#'

            # Search in all 4 direction for the next character
            j = i + 1 # Next char index
            res = (dfs(r + 1, c, j) or
                  dfs(r - 1, c, j) or
                  dfs(r, c + 1, j) or
                  dfs(r, c - 1, j))

            # Backtrack: restore original char for the next possible iteration
            board[r][c] = temp

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False