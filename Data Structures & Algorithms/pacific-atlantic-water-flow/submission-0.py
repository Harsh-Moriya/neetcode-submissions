class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited):
            visited.add((r, c))  # It's ok to make this cell as visited because we are immediately exploring all its paths so it will never be left out

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                   dfs(nr, nc, visited)

        # Run DFS for Horizontal borders
        for c in range(COLS):
            dfs(0, c, pac)  # First row, pacific
            dfs(ROWS - 1, c, atl)  # Last row, atlantic

        # Run DFS for Vertical borders
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        return list(pac & atl)