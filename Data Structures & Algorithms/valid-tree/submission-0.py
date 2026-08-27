class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid true with n nodes must have n - 1 edges
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)

        return len(visited) == n