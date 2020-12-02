import tweepy

auth = tweepy.OAuthHandler('0iC334apitNYGuR1TPcLv6Qff', 'iRChcHbmvNySVJ8PTP3yMJqAE1yXkya1XTMDlZTQsKpI5Xy2lz')
auth.set_access_token('1328206757416546306-4O5oLNq6uek0ElR2RIN5iat2RTJMkD', 'xMTn0ITB1AykqzTC9AbquOghhun4ithWiBi6NSo9eYP1m')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)