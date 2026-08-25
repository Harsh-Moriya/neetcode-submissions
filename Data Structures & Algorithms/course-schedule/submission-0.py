class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency map
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        state = [0] * numCourses # 0 = Unvisited, 1 = Visiting, 2 = Visited

        def hasCycle(course):
            if state[course] == 1:
                return True  # Found a cycle
            if state[course] == 2:
                return False  # Visited node is safe, meaning for this node we have checked the prerequisites already and it is valid

            state[course] = 1

            for prereq in adj[course]:
                if hasCycle(prereq):
                    return True

            state[course] = 2
            return False

        for i in range(numCourses):
            if hasCycle(i):
                return False

        return True