import os
import urllib
import urllib2
import json
import sys

user_url = 'http://api.twitter.com/1/users/lookup.json'

users_folder = 'users/'

# def LoadUser(user_filename):
#	with open(user_filename) as f:
		

def GetUserJSonByName(user_names):
	names = user_names.split(',')
        uncached_names = []

	for name in names:
		filename = users_folder + name + '.json'
	
		if os.path.exists(filename):
			print u'[{username}] in cache'.format(username=name)

		else:
			uncached_names.append(name)

	if not uncached_names:
		print 'Nothing to do...'
		quit() 

	names_to_lookup = ','.join(['%s' % uncached_name for uncached_name in uncached_names])

	users_form_fields = {
		'screen_name' : names_to_lookup,
		'include_entities' : 0
	}

	users_form_data = urllib.urlencode(users_form_fields)

	users_request = urllib2.Request(user_url, data=users_form_data)

	try:
		users_result = urllib2.urlopen(users_request)

		users_json = users_result.read()

		users = json.loads(users_json)

		for user in users:
			id_filename = str(user['id']) + '.json'
			id_filepath = users_folder + id_filename
			filename = users_folder + user['screen_name'] + '.json'

			with open(id_filepath, 'w+') as f:
				json.dump(user, f)

			os.symlink(id_filename, filename)
			print u'[{username}] saved in cache'.format(username=user['screen_name'])

	except:
		print 'Exception: Possibly no users found?', sys.exc_info()[0] 

users = sys.argv[1]

GetUserJSonByName(users)

