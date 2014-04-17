"""
A filter file for the Sandy dataset

Currently:
- Removes RT, MT
- Removes tweets that do not have a specific set of hashtags. 
- Replaces user mentions and urls in tweet text
- Condenses JSON to the following fields: id, coordinates, created_at, user.id, user.screen_name, text
"""

import json
import re
import sys

def process_tweet(input_tweet):
	tweet_json = json.loads(input_tweet)

	# Remove Retweets, Modified Tweets 
	tweet_text = tweet_json['text']
	if (tweet_json['retweeted'] is True) or ("RT" in tweet_text) or ("MT" in tweet_text):
		return None
	
	# Remove non-english tweets
	if ("en" not in tweet_json['lang']):
		print("Not English!" , tweet_json['lang'])
		return None
		
	'''
	# Remove tweets that do not have a desired hashtag
	tweet_hashs = str(tweet_json.get('entities').get('hashtags')).lower()
	
	if (("sandy" not in tweet_hashs) and ("hurricanesandy" not in tweet_hashs) and ("frankenstorm" not in tweet_hashs) and ("nyc" not in tweet_hashs) and ("hurricane" not in tweet_hashs)
	and ("storm" not in tweet_hashs) and ("fall" not in tweet_hashs) and ("sandyde" not in tweet_hashs) and ("sandynj" not in tweet_hashs) 
	and ("sandyabc7" not in tweet_hashs) and ("njsandy" not in tweet_hashs) and ("stormde" not in tweet_hashs) and ("weather" not in tweet_hashs)
	and ("breaking" not in tweet_hashs) and ("irene" not in tweet_hashs) and ("mittstormtips" not in tweet_hashs) and ("perfectstorm" not in tweet_hashs)):
		return None
	'''
		
	# Coordinate Check
	if tweet_json.get('coordinates') is not None:
		tweet_coords = tweet_json.get('coordinates').get('coordinates')
	elif tweet_json.get('geo') is not None:
		tweet_coords = tweet_json.get('geo').get('coordinates')
	else:
		tweet_coords = None

	# Replace usernames and urls
	tweet_text = re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "<user>", tweet_text)
	tweet_text = re.sub(r"(?P<url>https?://[^\s]+)", "<url>", tweet_text)
		
	# Create a smaller JSON object with desired fields
	output_tweet = {'id': tweet_json['id'], 'coordinates': tweet_coords, 'created_at': tweet_json['created_at'], 'user': {'id': tweet_json['user']['id'], 'screen_name': tweet_json['user']['screen_name']}, 'text': tweet_text}

	return output_tweet

def process_file(input_filename, output_filename):
	"""
	Process the file one input at a time and write the given output file
	"""
	# Create output file
	outfile = open(output_filename, 'w')

	# Process one line of the file
	with open(input_filename, 'r') as infile:
		for line in infile:
			tweet_output = process_tweet(line)
			if tweet_output is not None:
				json.dump(tweet_output, outfile)
				outfile.write('\n')

		infile.close()

	outfile.close()

if __name__ == '__main__':

	# Get arguments
	arguments = sys.argv
	arguments_len = len(arguments)

	# Data set name 
	input_filename = arguments[1]
	output_filename = arguments[2]
	process_file(input_filename, output_filename)
