import wordcloud
import matplotlib.pyplot as plt
import re


std_strings = re.compile(r"\b[haHA]+\b|\b[oOhH]+\b")

url_regex = re.compile(
    r"https?:\/\/[a-zA-Z0-9\./\-=_\)\(\*&\^%\$#@!<>\?{},|\+:~\[\]]+|\
            www\.[a-zA-Z0-9\./\-=_\)\(\*&\^%\$#@!<>\?{},|\+\:~[\]]+"
)

reddit_regex = re.compile(r"/?[ur]/[a-z]+")
twitter_regex = re.compile(r"@[A-Za-z0-9_-]+")
email_regex = re.compile(
    r"[a-zA-Z0-9_\.\+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-\.]+")

space_regex = re.compile(r"  +")
number_junk_regex = re.compile(r"\b[0-9]+\b|_+")
words_regex = re.compile(r"\w+['-]?\w+|\w{1}")
lang_regex = re.compile(r"[^\u0000-\u007F]+|[\w]+")
numeric_word_regex = re.compile(r"\b[0-9][a-zA-Z0-9]+\b|\b[a-zA-Z0-9]+[0-9]\b")


def words(text):
    """
    Takes a text and returns an iterator of individual words (tokens).
    """
    text = url_regex.sub("", text.lower())
    text = std_strings.sub("", text)

    text = reddit_regex.sub("", text)
    text = email_regex.sub("", text)
    text = twitter_regex.sub("", text)

    text = number_junk_regex.sub(" ", text)
    text = numeric_word_regex.sub(" ", text)
    text = space_regex.sub(" ", text)
    words = words_regex.findall(text)
    words = filter(lambda x: 1 < len(x) < 25, words)
    return words


def gen_wordcloud(text):
    text = words(text)
    text = " ".join(text)
    wc = wordcloud.WordCloud(
        height=400,
        width=800,
        background_color="white",
        stopwords=wordcloud.STOPWORDS
    )
    wc = wc.generate(text)
    wc.to_file("temp.png")


text = open("a.txt").read()
gen_wordcloud(text)
