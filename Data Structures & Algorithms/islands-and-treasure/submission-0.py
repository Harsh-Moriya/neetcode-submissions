class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return None

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = collections.deque()

        # Collect all gates
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        def evalIsland(r, c, nextVal):
            # Only consider valid and not reached cells
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != INF:
                return

            grid[r][c] = nextVal
            q.append((r, c)) # Add the current cell to ripple out from

        # Ripple outwards from the Treasures or Islands with calculated distances
        while q:
            r, c = q.popleft()

            nextVal = grid[r][c] + 1
            evalIsland(r + 1, c, nextVal)
            evalIsland(r - 1, c, nextVal)
            evalIsland(r, c + 1, nextVal)
            evalIsland(r, c - 1, nextVal)
