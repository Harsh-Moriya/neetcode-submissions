class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = high

        while low <= high:
            mid = (low + high) // 2

            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / mid)

            if hrs <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1

        return k