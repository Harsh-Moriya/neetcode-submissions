class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        state = [0] * numCourses
        order = []

        def hasCycle(course):
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False

            state[course] = 1

            for prereq in adj[course]:
                if hasCycle(prereq):
                    return True

            state[course] = 2
            order.append(course)

            return False

        for course in range(numCourses):
            if state[course] == 0 and hasCycle(course):
                return []

        return order