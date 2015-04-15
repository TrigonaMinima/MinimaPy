# See twitter.com/choosetothinq. Analyse the tweets from this account to print:
# - the top 3 most frequently used hashtags
# - the top 3 most retweeted tweets with links in them
# - the top 3 most frequently used words in its tweets


import tweepy
import json
import re

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def hash_freq(freq, hashes):
    """

    """
    if hashes:
        hash_t = hashes[0]["text"]
        if hash_t not in freq:
            freq[hash_t] = 1
        else:
            freq[hash_t] += 1


def link_retweets(tweet):
    """
    """
    retweet = {}

    if tweet["entities"]["urls"] and tweet["retweet_count"] > 0:
        retweet["id"] = tweet["id_str"]
        retweet["retweet_count"] = tweet["retweet_count"]
        retweet["text"] = tweet["text"]

    return retweet


# common = [r"\bi\b", r"\bin\b", r"\bif\b", r"\bis\b", r"\bon\b", r"\bof\b", r"\ba\b", r"\ban\b", r"\bat\b",
#           r"\bas\b", r"\bus\b", r"\bgo\b", r"[ ]+do[ ]+", r"\bto\b", r"\bnot\b", r"\bwe\b", r"\bbe\b", r"\byour\bs ",
#           r"\byour\b", r"\band\b", r"\bby\b", r"[ ]+the[ ]+", r"\bthis\b", r"\bits\b", r"\bfor\b", r"\byou\b",
#           r"\bbut\b", r"\bour\b", r"\bwas\b", r"\bcan\b", r"\balso\b", r"\byet\b", r"\bafter\b", r"\bwith\b", r"\bdid\b",
# r"^i", r"\bother\b", r"\bno\b", r"\bwhich\b", r"\bare\b", r"\bthey\b",
# r"\bhis\b", r"\bfrom\b", r"\bso\b"]

common = [r"\bi\b", r"\bi[nfs]\b", r"\bo[nfr]\b", r"\ba\b", r"\ba[nts]\b", r"^i", r"\bother\b", r"\bhe\b", r"\bhave\b",
          r"\bus\b", r"\b[gdtsn]o\b", r"\bnot\b", r"\b[wb]e\b", r"\byour[s]*\b ", r"\bwhich\b", r"\bthat\b", r"\bha[sd]\b"
          r"\band\b", r"\bby\b", r"\bthe[y]*\b", r"\b[t]*his\b", r"\bit[s]*\b", r"\bfor\b", r"\byou\b", r"\bwill\b", r"\bg[eo]t\b",
          r"\bbut\b", r"\bour\b", r"\bwas\b", r"\bcan\b", r"\balso\b", r"\byet\b", r"\bafter\b", r"\bwith\b", r"\bthem\b",
          r"\bdid\b", r"\bare\b", r"\bfrom\b", r"http[s]*://\S+", r" q.\d+", r"[#@]\w+", r"[^A-Za-z0-9]", r"\w+[-']\w+"]


def clean(sentence):
    """
    """

    pattern = r"(" + r"|".join(common) + r")"
    p = re.compile(pattern)

    sentence = p.sub(" ", sentence)

    p = re.compile("  +")
    sentence = p.sub(" ", sentence).strip()

    return sentence


def word_freq(words, text):
    """
    """

    temp = clean(text).split()
    for word in temp:
        word = word.strip()
        if len(word) > 1:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1


def statuses(user):
"""
"""
    freq = {}
    retweets = []
    words = {}

    for status in user.items():
        temp = status._json

        hash_freq(freq, temp["entities"]["hashtags"])

        retweet = link_retweets(temp)
        if retweet:
            retweets.append(retweet)

        word_freq(words, status.text.lower())

    print("Most frequently used hashtags-")
    for tag in reversed(sorted(freq, key=freq.__getitem__)[:10]):
        print(tag, "\t: ", freq[tag], " tweets")

    print()

    print("Most retweeted tweets with links in them-")
    for tweet in sorted(retweets, key=lambda k: k["retweet_count"], reverse=True)[:5]:
        print(json.dumps(tweet, separators=(',', ':'), indent=4), "\n")

    print()

    print("Most frequently used words-")
    for word in reversed(sorted(words, key=words.__getitem__)[:10]):
        print(word, "\t: ", words[word], " times")


# User data
# user = api.get_user('TrigonaMinima')
# print(json.dumps(user._json, separators=(',', ':'), indent=4))


# test statuses
# for status in tweepy.Cursor(api.user_timeline, id="choosetothinq").items(20):
#     print(json.dumps(status._json, separators=(',', ':'), indent=4))

if __name__ == "__main__":
    user = tweepy.Cursor(api.user_timeline, id="choosetothinq")
    statuses(user)
