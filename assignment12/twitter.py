#Q.3- Using Tweepy library try to extract tweets from Twitter.
import tweepy
consumer_key = "wvrvuirpt5YjpoXloAlhpnI0p"
consumer_secret = "9uYJR3N36GRFDZGS4yLA8daj5xKrU9y4hPg1KCgmMc42uLUvom"
access_key = "823162405588865024-CW0cURBdvh8UGHlM0ElF7QWjdp1FsN5"
access_secret = "UjFkwo1iEm4jK7VLs4qjmXvMBDCcUW6jp1D7H0Lf1KRF9"


user = tweepy.OAuthHandler(consumer_key,consumer_secret)
user.set_access_token(access_key,access_secret)

api = tweepy.API(user)
tweets = api.search("#worldcup")
for i in tweets:
    print(i)