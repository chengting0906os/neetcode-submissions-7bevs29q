class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_mp = defaultdict(list) # userId: (time, tweetId)
        self.follow_mp = defaultdict(set) # followerId: set(followeeId) # 我追蹤的人

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_mp[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        self.follow_mp[userId].add(userId)

        # 先把每個人最新的推進去
        for user_id in self.follow_mp[userId]:
            if self.tweet_mp[user_id]:
                latest_idx = len(self.tweet_mp[user_id]) - 1
                time, tweetId = self.tweet_mp[user_id][latest_idx]
                max_heap.append((time, tweetId, user_id, latest_idx))


        heapq.heapify_max(max_heap)
        while len(res) < 10 and max_heap:
            time, tweetId, user_id, idx = heapq.heappop_max(max_heap)
            res.append(tweetId)
            next_idx = idx - 1
            if next_idx >= 0:
                next_time, next_tweetId = self.tweet_mp[user_id][next_idx]
                heapq.heappush_max(max_heap, (next_time, next_tweetId, user_id, next_idx))
    
        return res
                    



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_mp[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_mp[followerId].discard(followeeId)
        
