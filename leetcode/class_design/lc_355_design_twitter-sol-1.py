from collections import defaultdict
import heapq
from typing import List


'''
https://leetcode.com/problems/design-twitter/description/
'''
class Twitter:

    def __init__(self):
        # dict mapping user id -> set of user id they follow
        self.following = defaultdict(set)

        # dict mapping user id -> list of their tweets
        # note tweets will be (tweet count #, tweet id)
        # this will be useful to order tweets
        # by the tweet count in a heap later on
        self.user_tweets = defaultdict(list)

        # initialize the # of tweets to 0
        # this tweet count will be the priority in the
        # list heaps of tweets
        self.tweet_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # first increment the tweet count, since we are adding a tweet
        self.tweet_count += 1
        # setup our tuple of tweet with the tweet count
        tweet_with_count = (self.tweet_count, tweetId)

        # add the tweet to the list of user's tweets
        self.user_tweets[userId].append(tweet_with_count)

    def getNewsFeed(self, userId: int) -> List[int]:
        # first get the set of users that the user id follows
        following_set = self.following[userId]
        # then get the user's own tweets
        user_tweets = self.user_tweets[userId]

        # init our feed heap as an empty list
        # this will be of size 10
        feed_heap = []
        
        # loop through all user_tweets
        for tweet in user_tweets:
            # only add the 10 most recent tweets
            # to the feed heap
            if len(feed_heap) < 10:
                # if have less than 10 elements,
                # just add normally to the feed heap
                heapq.heappush(feed_heap, tweet)
            else:
                # else we need to pop the oldest tweet
                # (which has the smallest tweet count
                # -> this is why we use min heap)
                # and add the newest tweet
                heapq.heappushpop(feed_heap, tweet)

        # loop through all followers
        for followee_id in following_set:
            # get the follower tweets
            followee_tweets = self.user_tweets[followee_id]
            # loop through all follower tweets
            for tweet in followee_tweets:
                # only add the 10 most recent tweets 
                # to the feed heap
                if len(feed_heap) < 10:
                    # if have less than 10 elements,
                    # just add normally to the feed heap
                    heapq.heappush(feed_heap, tweet)
                else:
                    # else we need to pop the oldest tweet
                    # (which has the smallest tweet count
                    # -> this is why we use min heap)
                    # and add the newest tweet
                    heapq.heappushpop(feed_heap, tweet)
        
        # our final feed will basically
        # be a sorted version of our feed_heap
        # sorted by tweet count ascending using heapsort
        # initialize our final feed
        feed = []
        # loop until we have emptied the feed_heap
        while feed_heap:
            # get the tweet id, which is the 2nd element
            # in the tuple
            _, tweetId = heapq.heappop(feed_heap)
            # add the tweet id to the feed
            feed.append(tweetId)

        # now reverse the feed because we had a min heap
        # which orders from smallest tweet count to largest tweet count
        # but we want largest tweet count to smallest tweet count
        feed.reverse()

        # finally, return the feed
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # edge case to prevent a user from following themselves
        if followerId == followeeId:
            return

        # just add the followeId to the followerId's following set
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # edge case to prevent a user from unfollowing themselves
        if followerId == followeeId:
            return
        
        # just remove the followeeId from the followerId's following set
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
