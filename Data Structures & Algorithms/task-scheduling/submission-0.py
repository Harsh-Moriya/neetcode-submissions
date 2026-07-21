class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        # Simulate a max heap using by using negative counts
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # Stores the count and Idle time

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap) # Adding 1 to reduce the count since here the count is a negative value
                if cnt != 0:
                    q.append([cnt, time + n]) # Add the count and the time when the task will be available again

            # Check if the first item in queue has met its idle time requirement
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0]) # Add the count/task back into the heap to process it

        return time