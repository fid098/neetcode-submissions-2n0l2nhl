class Twitter:
    """
    followmap = {userid: set(followeeid)}
    tweetmap = {userid: list([count, tweetid])}
    """

    def __init__(self):
        self.count = 0
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap: 
                index = len(self.tweetmap[followeeId]) - 1   #get the last tweet position of the followee
                count, tweetId = self.tweetmap[followeeId][index]  # get the last tweet count and tweetid
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) #push the count, tweetid , follower id and the index of the next tweet 

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap) #get the earliest tweets
            res.append(tweetId)
            if index >= 0: #if there is another tweet after it, add it to the minHeap
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
