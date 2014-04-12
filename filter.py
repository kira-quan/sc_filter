import json
import re
import sys

def process_tweet(input_tweet):
	tweet_json = json.loads(input_tweet)

	# Remove Retweets, Modified Tweets 
	tweet_text = tweet_json['text']
	if (tweet_json['retweeted'] is True) or ("RT" in tweet_text) or ("MT" in tweet_text):
		return None

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
	output_tweet = [{'id': tweet_json['id'], 'coordinates': tweet_coords, 'created_at': tweet_json['created_at'], 'user': {'id': tweet_json['user']['id'], 'screen_name': tweet_json['user']['screen_name']}, 'text': tweet_text}]

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