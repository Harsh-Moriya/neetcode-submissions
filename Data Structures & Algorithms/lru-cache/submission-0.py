class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.usage = {}
        self.cap = capacity
        self.time = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.time += 1
        self.usage[key] = self.time

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value

        self.time += 1
        self.usage[key] = self.time

        if len(self.cache) > self.cap:
            minKey, minTime = key, self.usage[key]

            for k, t in self.usage.items():
                if t < minTime:
                    minTime = t
                    minKey = k

            self.cache.pop(minKey)
            self.usage.pop(minKey)