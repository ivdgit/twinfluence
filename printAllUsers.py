import os
import glob
import json
import sys

def LoadUser(user_filename):
	with open(user_filename) as f:
		user = json.loads(f.read())
		return user;

	raise Exception('User not found');

def PrintUserJson(user):
	print u'================================'
	print u'{username} ({followers})'.format(username=user['screen_name'], followers=user['followers_count'])
	print u'{description}'.format(description=user['description'])
	print

def PrintUsers(folder):
	all_files = glob.glob(folder + '*.json')
	real_files = [filename for filename in all_files if os.path.islink(filename)]
	for filename in real_files:
		PrintUserJson(LoadUser(filename))

folder = sys.argv[1]

PrintUsers(folder)
