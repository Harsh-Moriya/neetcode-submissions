class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = set(self.following.get(userId, set()))
        followees.add(userId)

        minHeap = []

        for followeeId in followees:
            if followeeId in self.tweets and self.tweets[followeeId]:
                lastId = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][lastId]

                # Append followee id and last element id to get the previous tweet from the same person
                minHeap.append([time, tweetId, followeeId, lastId])

        heapq.heapify(minHeap)

        res = []

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, lastId = heapq.heappop(minHeap)
            res.append(tweetId)

            if lastId > 0:
                prevId = lastId - 1
                time, tweetId = self.tweets[followeeId][prevId]
                heapq.heappush(minHeap, [time, tweetId, followeeId, prevId])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)