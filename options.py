import ast
from debug_functions import *
import json

def get_options():
	try:
		text = open("Resources/configuration.txt", "r").read()
		return ast.literal_eval(text)
	except IOError:
		return None
	
def save_options(data):
	f = open("Resources/configuration.txt", "w")
	f.write(json.dumps(
		data,
		sort_keys=True,
		indent=4,
		separators=(',', ': '),
		ensure_ascii=False
	))
	f.close()
	
def setup():
	config = {}
	
	log(bcolors.INFO, "You are currently in the configuration mode.")
	
	log(bcolors.NORMAL, f"Do you want your bot to reply to submissions? {bcolors.SUCCESS} Y/N")
	choice = input().lower()
	new_line()
	if choice == "y":
		config["auto_messages"] = {}
		log(bcolors.NORMAL, f"On what percentage of submissions do you want your bot to reply? Enter {bcolors.SUCCESS}just the number (0.01-100)")
		chance = float(input()) / 100
		config["auto_messages"]["chance"] = chance
		new_line()
		log(bcolors.NORMAL, f"Now let's set up actual messages to reply to submissions. Enter your messages on below. {bcolors.SUCCESS}If you want to add another message, press \"Enter\" key. {bcolors.HEADER} When you are done, leave new line empty and press \"Enter\" key")
		message = " "
		config["auto_messages"]["messages"] = []
		while message != "":
			message = input()
			if message != "":
				config["auto_messages"]["messages"].append(message)
		
		new_line()
		log(bcolors.NORMAL, f"On what subreddit do you want your bot to post comments? (enter without r/)")
		config["auto_messages"]["subreddit"] = input()
		log(bcolors.INFO, "Great! Now let's go to the next step.")
	log(bcolors.NORMAL, f"Do you want your bot to respond to replies of the bot's comments? (Eg. Submission <- Bot (Nice post!) <- User (Thanks!) <- Bot (No problem!) ) {bcolors.SUCCESS} Y/N")
	
	choice = input().lower()
	new_line()
	if choice == "y":
		log(bcolors.FAIL, "Soon... Sorry for inconvenience.")
		
	log(bcolors.NORMAL, "Enter client_id and client_secret below (space separated) (if you don't have them, follow the guide at https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps. Setup an application as a script)")
	
	client_id, client_secret = map(str, input().split())
	config["client_id"] = client_id
	config["client_secret"] = client_secret
	
	log(bcolors.NORMAL, f"Now this tool must know your account's username and account's password. (space separated) {bcolors.WARNING}If you don't trust this utility, you can look at it's code. Or you can just press Control+C to exit. {bcolors.NORMAL}")
	username, password = map(str, input().split())
	
	config["username"] = username
	config["password"] = password
	
	log(bcolors.SUCCESS, "Configuration complete! You may now start the bot.")
	save_options({"data":config})
def setup_configuration_file():
	new_line(2)
	if get_options() != None:
		log(bcolors.WARNING, f"You had already configured bot. In the current version it is not possible to edit bot's configuration via this tool, but you can manually edit it in {bcolors.WARNING}RedditBot/Resources/configuration.txt. ")
		log(bcolors.HEADER, "Do you want to overwrite configuration file? Y/n")
		if input().lower() != "y":
			print("\n")
			log(bcolors.INFO, "Leaving configuration file as it is.")
		else:
			new_line()
			setup()
	else:
		# TODO
		setup()