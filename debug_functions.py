#!/usr/bin/env python3

class bcolors:
	NORMAL = '\033[0m'
	HEADER = '\033[95m'
	SUCCESS = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	DEBUG = '\033[93m'
	INFO = '\033[92m'
	REDDIT = '\x1b[38;5;124m'
	
def log(type, str):
	if type == bcolors.WARNING:
		print(f"{type}[WARNING] {bcolors.NORMAL}{str}")
	elif type == bcolors.FAIL:
		print(f"{type}[ERROR] {bcolors.NORMAL}{str}")
	elif type == bcolors.INFO:
		print(f"{type}[INFO] {bcolors.NORMAL}{str}")
	else:
		print(f"{type}{str}")
		
def new_line(count = 1):
	for _ in range(count):
		print("\n")
		print()