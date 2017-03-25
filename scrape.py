#!/usr/bin/python

import time
import random


def scrape(submission):
	log = open('data.txt','w')
	t = submission.title
	desc = submission.selftext
	comments = submission.comments.list()
	log.write(t + "\n")
	log.write(desc + "n")
	for item in comments:
		log.write(item.body + "\n")
	i = random.randint(3,120)
	print("Lurking... this may take " + str(i) + " seconds")
	log.close()
	time.sleep(i)
