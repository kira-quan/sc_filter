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
j=0


def process_tweet_rand(input_tweet, randnums, i):
	tweet_json = json.loads(input_tweet)
	
	if (i  not in randnums):
		return None
		
	print(i)
	
	# Create a smaller JSON object with desired fields
	return tweet_json
	
def process_tweet(input_tweet):
	tweet_json = json.loads(input_tweet)
	
	# Create a smaller JSON object with desired fields
	return tweet_json

def process_file(input_filename):
	"""
	Process the file one input at a time and write the given output file
	"""
	# Create output file
	outfile = open("sandy_training_all.json", 'w')
	
	
	# Process one line of the file
	with open(input_filename, 'r') as infile:
		
		global i;
		randnums = random.sample(range(1, 37020), 4200)
		
		for line in infile:
			i+=1
			tweet_output = process_tweet_rand(line, randnums, i)
			if tweet_output is not None:
				json.dump(tweet_output, outfile)
				outfile.write('\n')

		infile.close()

	outfile.close()
	
	#Split the outfile into 6
	outfile1 = open("sandy_training_700_1.json", 'w')
	outfile2 = open("sandy_training_700_2.json", 'w')
	outfile3 = open("sandy_training_700_3.json", 'w')
	outfile4 = open("sandy_training_700_4.json", 'w')
	outfile5 = open("sandy_training_700_5.json", 'w')
	outfile6 = open("sandy_training_700_6.json", 'w')
	
	with open("sandy_training_all.json", 'r') as infile:
		global j;
		
		for line in infile:
			j+=1
			tweet_output = process_tweet(line)
			
			if ((j>0) and (j<=700)):
				json.dump(tweet_output, outfile1)
				outfile1.write('\n')
			if ((j>700) and (j<=1400)):
				json.dump(tweet_output, outfile2)
				outfile2.write('\n')
			if ((j>1400) and (j<=2100)):
				json.dump(tweet_output, outfile3)
				outfile3.write('\n')
			if ((j>2100) and (j<=2800)):
				json.dump(tweet_output, outfile4)
				outfile4.write('\n')
			if ((j>2800) and (j<=3500)):
				json.dump(tweet_output, outfile5)
				outfile5.write('\n')
			if ((j>3500) and (j<=4200)):
				json.dump(tweet_output, outfile6)
				outfile6.write('\n')
		infile.close()

	outfile1.close()
	outfile2.close()
	outfile3.close()
	outfile4.close()
	outfile5.close()
	outfile6.close()

if __name__ == '__main__':

	# Get arguments
	arguments = sys.argv
	arguments_len = len(arguments)

	# Data set name 
	input_filename = arguments[1]
	process_file(input_filename)
