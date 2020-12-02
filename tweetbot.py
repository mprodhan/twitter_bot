import tweepy
import time

auth = tweepy.OAuthHandler('0iC334apitNYGuR1TPcLv6Qff', 'iRChcHbmvNySVJ8PTP3yMJqAE1yXkya1XTMDlZTQsKpI5Xy2lz')
auth.set_access_token('1328206757416546306-4O5oLNq6uek0ElR2RIN5iat2RTJMkD', 'xMTn0ITB1AykqzTC9AbquOghhun4ithWiBi6NSo9eYP1m')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

# Limit handler helper function
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
    except StopIteration:
        time.sleep(300)


# Following back followers
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
# Tech Debt: Figure out a way to stop the while loop besides, ctrl+c
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 50:
        follower.follow()
        break
    # print(follower.name)

