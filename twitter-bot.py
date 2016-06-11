# coding: utf-8
import twitter
import json
import urllib
import Image
import time
import math
import random
import re
import threading

	
class tweetBot(threading.Thread):	
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
		if self.threadID == 1:
			auto_tweet()
		if self.threadID == 2:
			interactive()
	
def auto_tweet():
		all_accounts = twitter.get_all_accounts()
		if len(all_accounts) >= 1:
			account = all_accounts[1]
			parameters = {'screen_name': account['username']}
			status, data = twitter.request(account, 'https://api.twitter.com/1.1/users/show.json', 'GET', parameters)
			if status == 200:
				user_info = json.loads(data)
				last_value = twitter.get_home_timeline(account, count = 0, parameters=None)[0].get('text')
				print(last_value)
				last_value = int(last_value)
				value = int(math.log(last_value, 2))
				print(value)
				for value in range(value, 1000):
					tweet = last_value * 2
					twitter.post_tweet(account, str(tweet), parameters=None)
					print('Tweet Successful:' + str(tweet) + '. Next tweet in: ')
					last_value = tweet
					time.sleep(5)
				
			else:
				print 'Could not retrieve profile image (status: %i)' % (status,)
		else:
			print 'You don\'t have any Twitter accounts (or haven\'t given permission to access them)'

beginning = ["That\'s ", "That would be ", "That'd be ", "The answer is ", "My sources indicate that the answer is ", "It's "]
def interactive():
	all_accounts = twitter.get_all_accounts()
	if len(all_accounts) >= 1:
		account = all_accounts[1]
		parameters = {'screen_name': account['username']}
		status, data = twitter.request(account, 'https://api.twitter.com/1.1/users/show.json', 'GET', parameters)
		if status == 200:
			user_info = json.loads(data)
			initial_mention = twitter.get_mentions_timeline(account, count=0, parameters=None)[0].get('text')
			print(latest_mention)
			#while latest_mention is twitter.get_mentions_timeline(account, count = 0, parameters=None)[0]:
			take_questions = True
			while take_questions: 
				if latest_mention is not twitter.get_mentions_timeline(account, count = 0, parameters=None)[0]:
					new_mention = twitter.get_mentions_timeline(account, count = 0, parameters=None)[0]
					query = re.search('.\^(\d+)', new_mention).groups()[0]
					print(query)
					if query == None:
						pass
					else:
						twitter.post_tweet(account, str(beginning[random.randint(0, len(beginning))] + 2**query + "."))
					latest_mention = new_mention			
			
		else:
			print 'Could not retrieve profile image (status: %i)' % (status,)
	else:
		pri nt 'You don\'t have any Twitter accounts (or haven\'t given permission to access them).'	
#thread1 = tweetBot(1)
thread2 = tweetBot(2)

#thread1.start()
#print('Thread One Initiated')
thread2.start(),