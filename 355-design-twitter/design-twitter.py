class MaxHeap:
    def __init__(self):
        self.heap_arr = [-1]   # 1-indexed
        self.size = 0

    def heapify(self, arr):
        # TC: O(n) | SC: O(n)
        self.heap_arr = [-1] + arr
        self.size = len(arr)
        n = self.size
        for i in range(n // 2, 0, -1):
            curr = i
            while True:
                largest = curr
                left = 2 * curr
                right = 2 * curr + 1

                if left < n and self.heap_arr[largest] < self.heap_arr[left]:
                    largest = left
                if right < n and self.heap_arr[largest] < self.heap_arr[right]:
                    largest = right

                if curr == largest:
                    break

                self.heap_arr[largest], self.heap_arr[curr] = self.heap_arr[curr], self.heap_arr[largest]
                curr = largest

    def heappush(self, val):
        # TC: O(log n) | SC: O(1)
        self.size += 1
        self.heap_arr.append(val)
        current_idx = self.size
        parent_idx = current_idx // 2
        # Sift up: swap with parent while larger than parent
        while parent_idx > 0 and self.heap_arr[parent_idx] < self.heap_arr[current_idx]:
            self.heap_arr[current_idx], self.heap_arr[parent_idx] = self.heap_arr[parent_idx], self.heap_arr[current_idx]
            current_idx = parent_idx
            parent_idx = current_idx // 2

    def heappop(self):
        # TC: O(log n) | SC: O(1)
        n = self.size
        self.heap_arr[1], self.heap_arr[n] = self.heap_arr[n], self.heap_arr[1]
        pop_value = self.heap_arr.pop()
        self.size -= 1
        n -= 1

        parent_idx = 1
        while True:
            smallest = parent_idx  # candidate for swap
            left = parent_idx * 2
            right = parent_idx * 2 + 1

            if left <= n and self.heap_arr[smallest] < self.heap_arr[left]:
                smallest = left
            if right <= n and self.heap_arr[smallest] < self.heap_arr[right]:
                smallest = right

            if parent_idx == smallest:
                break

            self.heap_arr[parent_idx], self.heap_arr[smallest] = self.heap_arr[smallest], self.heap_arr[parent_idx]
            parent_idx = smallest

        return pop_value

class Twitter:

    def __init__(self):
        self.userConnections = {}
        self.userTweets = {}
        self.currentTime = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId] = self.userTweets.get(userId, [])
        self.userTweets[userId].append((self.currentTime, tweetId))
        self.currentTime += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        usersToCheck = [userId]
        usersToCheck.extend(list(self.userConnections.get(userId, set())))
        tweets = MaxHeap()
        retTweets = []
        for user in usersToCheck:
            if user not in self.userTweets or len(self.userTweets[user]) <= 0:
                continue
            time, tweetId = self.userTweets[user][-1]
            tweets.heappush([time, tweetId, user, len(self.userTweets[user]) - 1])
        while tweets.size > 0 and len(retTweets) < 10:
            tweet = tweets.heappop()
            userId = tweet[2]
            idx = tweet[3]
            retTweets.append(tweet[1])
            if idx > 0:
                print(idx, self.userTweets[userId])
                time, tweetId = self.userTweets[userId][idx - 1]
                tweets.heappush([time, tweetId, userId, idx - 1])
        print("\n"*3)
            
        return retTweets
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userConnections[followerId] = self.userConnections.get(followerId, set())
        self.userConnections[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userConnections[followerId] = self.userConnections.get(followerId, set())
        if followeeId in self.userConnections[followerId]: 
            self.userConnections[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)