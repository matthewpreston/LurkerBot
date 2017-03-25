#!/usr/bin/python
import praw
import scrape

reddit = praw.Reddit('Lurk3rB0t', user_agent='Lurk3rB0t user agent')


while True:
#	try:
#		scrape.scrape(reddit.random_subreddit().random())
#	except Exception:
#		pass
	print("lurkin")
	scrape.scrape(reddit.random_subreddit().random())
