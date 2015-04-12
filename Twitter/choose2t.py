# problem #2
# See twitter.com/choosetothinq. Analyse the tweets from this account to print:
# - the top 3 most frequently used hashtags
# - the top 3 most retweeted tweets with links in them
# - the top 3 most frequently used words in its tweets


import tweepy

auth = tweepy.OAuthHandler(
    "", "")

auth.set_access_token("",
                      "")

api = tweepy.API(auth)

for friend in tweepy.Cursor(api.friends).items():
    print(friend)
