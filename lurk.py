#!/usr/bin/python
import praw

reddit = praw.Reddit('Lurk3rB0t', user_agent='Lurk3rB0t user agent')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
print("---------------------------------\n")