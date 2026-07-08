class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            distSq = x**2 + y**2
            min_heap.append((distSq, [x, y]))

        heapq.heapify(min_heap)

        res = []

        while k:
            dist, point = heapq.heappop(min_heap)
            res.append(point)
            k -= 1

        return res