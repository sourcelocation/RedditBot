import praw
import random
from debug_functions import *
import time
import signal
import sys

signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

def add_viewed(id):
	f = open("Resources/viewed_submissions.txt", "a")
	f.write(" " + id)
	f.close()
	
def views_contains(id):
	f = set(open("Resources/viewed_submissions.txt", "r").read().split())
	return id in f

def start(config):
	config = config["data"]
	client_id = config["client_id"]
	client_secret = config["client_secret"]
	password = config["password"]
	username = config["username"]
	
	messages_config = config["auto_messages"]
	messages = messages_config["messages"]
	subreddit = messages_config["subreddit"]
	chance = messages_config["chance"]
	
	reddit = praw.Reddit(
		client_id=client_id,
		client_secret=client_secret,
		password=password,
		user_agent="android", # Yes, android
		username=username
	)
	
	starttime = time.time()
	delay = 7.5
	while True:
#		if len(submissiosn) == 0:
#			log(bcolors.INFO, f"No new submissions to reply to.")
		for submission in reddit.subreddit(subreddit).new(limit=15):
			if not views_contains(submission.id):
				if float(random.randint(0, 100)) / 100.0 < chance:
					message = random.choice(messages)
					submission.reply(message)
					
					log(bcolors.INFO, f"Replied to submission https://www.reddit.com/r/memes/comments/{submission.id}/ with \"{message}\"")
				else:
					log(bcolors.INFO, f"Viewed submission https://www.reddit.com/r/memes/comments/{submission.id}/, but did not reply (chance).")
				add_viewed(submission.id)
				time.sleep(delay)
		# Wait 'delay' seconds
		time.sleep(delay - ((time.time() - starttime) % delay))