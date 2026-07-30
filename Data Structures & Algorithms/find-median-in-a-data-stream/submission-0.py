class MedianFinder:

    def __init__(self):
        # Maintain two heaps which form two halves of the entire number list
        self.small = [] # A Max heap, Implemented using sign inversion
        self.large = [] # A Min heap

    def addNum(self, num: int) -> None:
        small = self.small
        large = self.large

        # 1) Push the number into the small heap regardless of its value
        heapq.heappush(small, -num)

        # 2) Take the largest element from the small heap and push it to the large
        heapq.heappush(large, -heapq.heappop(small))

        # 3) With just the previous steps the small heap will always stay empty, we need to ensure that doesn't happen and also balance the heaps, To achieve this we'll check if large has more elements than small, if yes then we'll simply take the smallest and put it back in the small heap, with this we can ensure both and we'll also know that the small will either have the same or one more element
        if len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))



    def findMedian(self) -> float:
        small = self.small
        large = self.large

        if len(small) > len(large):
            return -small[0]

        return (-small[0] + large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()