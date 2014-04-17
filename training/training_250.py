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
import random
i=0


def process_tweet(input_tweet, randnums, i):
	tweet_json = json.loads(input_tweet)
	
	if (i  not in randnums):
		return None
		
	print(i)
	
	# Create a smaller JSON object with desired fields
	return tweet_json

def process_file(input_filename, output_filename):
	"""
	Process the file one input at a time and write the given output file
	"""
	# Create output file
	outfile = open(output_filename, 'w')
	
	
	# Process one line of the file
	with open(input_filename, 'r') as infile:
		
		global i;
		randnums = random.sample(range(1, 37020), 250)
		
		for line in infile:
			i+=1
			tweet_output = process_tweet(line, randnums, i)
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
