#!/usr/bin/python

import time
import random


def shuffle_word(word):
	word = list(word)
	random.shuffle(word)
	return ''.join(word)


def load_template(t,desc_html):
	template_read = open("template.html","r")
	template_write = open("lurk.html","w")
	for line in template_read:
		if line.find("##title##") != -1:
			line = line.replace("##title##", t)
		elif line.find("##content##") != -1:
			line = line.replace("##content##",desc_html)
		template_write.write(line)
	
	
def scrape(submission):
	
	t = submission.title
	desc = submission.selftext
	desc_html = ""
	if desc is not None:
		for line in desc.split("\n"):
			desc_html = desc_html + "<br>" + line + "\n"
	load_template(t,desc_html)
	time.sleep(3)
	