### Dependency

- **Python 3.4**
- **[Tweepy](https://github.com/tweepy/tweepy)**  
    Install it by running 

    ```
    pip install tweepy
    ```


Now, you are ready to use the code.

### Usage:

This code file gives three following stats for the public feeds of any account.

- The top 3 most frequently used hashtags.
- The top 3 most retweeted tweets with links in them.
- The top 3 most frequently used words in its tweets.

At line 148 in the file ```choose2t.py``` which presently is in the form,

```
user = tweepy.Cursor(api.user_timeline, id="choosetothinq")
```
one can edit the "id" parameter to any username instead of "choosetothinq" to get the above states stats for that user.
To get the results on have to do either one of the things

```
python3.4 choose2t.py
```
Above command will print the results on the terminal window. Whereas, this will redirect the results to a text file.

```
python3.4 choose2t.py > results.txt
```

### Assumptions

- In the most retweeted tweets section the frequency is determined for those tweets which were most retweeted. For that purpose, the retweets done by this public account (choosetothinq, in our case) which were retweeted by others were also considered.
- While determining the most used words among all the tweets many "stop words" like - the, to, there, is, will, has, etc were removed before determining the frequency.
- Also, interrogative words like - what, why, how, where, rt etc were not removed.