class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        time, fresh = 0, 0

        # Enqueue all the rotten oranges and count the fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        # Run a level by level BFS, each level contitutes one minute
        while q and fresh > 0:
            # Process entire level at once using the q length which is calculated only one time here so any change in q in the loop will not affect the flow
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    # Consider only fresh oranges
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # Rot the orange
                        fresh -= 1 # Reduce fresh count
                        q.append((nr, nc))
            time += 1 # Update time once a level is processed

        return time if fresh == 0 else -1