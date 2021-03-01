from debug_functions import *
from options import *
import bot
import sys

#log(bcolors.INFO, "Welcome to RedditBot!\n")
#Cool stuff
print(f'''{bcolors.REDDIT}    ____           __    ___ __  {bcolors.NORMAL}____        _   
{bcolors.REDDIT}   / __ \___  ____/ /___/ (_) /_{bcolors.NORMAL}| __ )  ___ | |_ 
{bcolors.REDDIT}  / /_/ / _ \/ __  / __  / / __/{bcolors.NORMAL}|  _ \ / _ \| __|
{bcolors.REDDIT} / _, _/  __/ /_/ / /_/ / / /_  {bcolors.NORMAL}| |_) | (_) | |_ 
{bcolors.REDDIT}/_/ |_|\___/\__,_/\__,_/_/\__/  {bcolors.NORMAL}|____/ \___/ \__|
''')
log(bcolors.WARNING, f"This tool has been made purely {bcolors.FAIL}for educational purposes. {bcolors.NORMAL}By using this utility you agree, that the developer of this tool {bcolors.WARNING}is not responsible for anything done with this tool.")

	
# Start
def go_to_menu():
	new_line()
	log(bcolors.INFO, "You are in the menu. What do you want to do?")
	print(f"{bcolors.SUCCESS}1 {bcolors.NORMAL}- Start bot (Options must be configured)")
	print(f"{bcolors.SUCCESS}2 {bcolors.NORMAL}- Configure bot")
	
	choice = input()
	
	if choice == "1":
		log(bcolors.WARNING, f"Are you really sure you want to continue? {bcolors.WARNING}Your account will probably get banned if you use it on some subreddits!  {bcolors.HEADER}N/y")
		choice = input()
		if choice.lower() != "y":
			go_to_menu()
			return
		else:
			bot.start(get_options())
			go_to_menu()
	elif choice == "2":
		setup_configuration_file()
		go_to_menu()
	else:
		go_to_menu()
go_to_menu()


# Slant for 'bot' and 
###

###