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
    Takes in a dictionary of frequencies and the hashtags' data and records the
    frequencies of the hashtags in the dictionary.

    Returns None.
    """
    if hashes:
        hash_t = hashes[0]["text"]
        if hash_t not in freq:
            freq[hash_t] = 1
        else:
            freq[hash_t] += 1


def link_retweets(tweet):
    """
    Takes in the tweet json data, checks of the tweet contains any link and
    returns a dictionary with the retweet_count information.
    """
    retweet = {}

    if tweet["entities"]["urls"] and tweet["retweet_count"] > 0:
        retweet["id"] = tweet["id_str"]
        retweet["retweet_count"] = tweet["retweet_count"]
        retweet["text"] = tweet["text"]

    return retweet


def clean(sentence):
    """
    Takes the tweet as an input, cleans it using the regular expression
    defined and explained below and returns the cleaned string.

    All the "stop words" are removed by using the below list of regexs. Of the
    following the regex r"http[s]*://\S+", selects all the links in the sentence.
    r" q.\d+", selects the strings like q.1653 from the sentence.
    r"[#@]\w+", selects the @ mentions and hashtags in the sentence.
    r"[^A-Za-z0-9]", selects all the special characters in the sentence.
    r"\w+[-']\w+" selects all the words with "-" or "'" in between them.
    """

    common = [r"\bi\b", r"\bi[nfs]\b", r"\bo[nfr]\b", r"\ba\b", r"\ba[nts]\b",
              r"^i", r"\bother\b", r"\bhe\b", r"\bhave\b", r"\bus\b",
              r"\b[gdtsn]o\b", r"\bnot\b", r"\b[wb]e\b", r"\byour[s]*\b",
              r"\bwhich\b", r"\bthat\b", r"\bha[sd]\b", r"\band\b", r"\bby\b",
              r"\bthe[y]*\b", r"\b[t]*his\b", r"\bit[s]*\b", r"\bfor\b", r"\byou\b",
              r"\bwill\b", r"\bg[eo]t\b", r"\bbut\b", r"\bour\b", r"\bwas\b",
              r"\bcan\b", r"\balso\b", r"\byet\b", r"\bafter\b", r"\bwith\b",
              r"\bthem\b", r"\bdid\b", r"\bare\b", r"\bfrom\b", r"http[s]*://\S+",
              r" q.\d+", r"[#@]\w+", r"[^A-Za-z0-9]", r"\w+[-']\w+"]

    pattern = r"(" + r"|".join(common) + r")"
    p = re.compile(pattern)

    sentence = p.sub(" ", sentence)

    p = re.compile("  +")
    sentence = p.sub(" ", sentence).strip()

    return sentence


def word_freq(words, text):
    """
    Takes a dictionary and a string and does the frequency analysis of the words
    from the tweet string. It removes the stop words from the string by calling
    the clean() method.

    Returns None.
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
    Takes in the tweepy object using which the tweets will be fetched for the
    account and then the analysis is done to get the following 3 stats-

    - the top 3 most frequently used hashtags
    - the top 3 most retweeted tweets with links in them
    - the top 3 most frequently used words in its tweets

    Returns None.

    """
    freq = {}
    retweets = []
    words = {}

    for status in user.items():
        # Contains all the data of a tweet
        temp = status._json

        # Calculates the frequencies of hashtags
        hash_freq(freq, temp["entities"]["hashtags"])

        # Gets the retweeted tweets
        retweet = link_retweets(temp)
        if retweet:
            retweets.append(retweet)

        # Calculates the frequencies of words
        word_freq(words, status.text.lower())

    print("Most frequently used hashtags-")
    for tag in reversed(sorted(freq, key=freq.__getitem__)[-3:]):
        print(tag, "\t: ", freq[tag], " tweets")

    print()

    print("Most retweeted tweets with links in them-")
    for tweet in sorted(retweets, key=lambda k: k["retweet_count"],
                        reverse=True)[:5]:
        print(json.dumps(tweet, separators=(',', ':'), indent=4), "\n")

    print()

    print("Most frequently used words-")
    for word in reversed(sorted(words, key=words.__getitem__)[-4:]):
        print(word, "\t: ", words[word], " times")


if __name__ == "__main__":
    user = tweepy.Cursor(api.user_timeline, id="choosetothinq")
    statuses(user)
