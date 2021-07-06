# tweet.py file
#Author  : 	Viral Parmar   
#Github  : 	https://github.com/vral-parmar
#Twitter : 	https://twitter.com/vral_parmar
#live Bot:	https://twitter.com/TaelynCorb

import tweepy
from time import sleep
from Cred import *
import logging
from multiprocessing import Process
logging.basicConfig(filename="Twlog.log", format='%(asctime)s %(message)s', filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.INFO)
print('You can Check twitted Log in Project Root directory')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
def one():                                  #change keyword written in hashtags Dont remove OR operator and you can also change geo variable and define kilometer radious at the end.
    for tweet in tweepy.Cursor(api.search, q=('#love OR #friends OR #Cyber OR #dost -filter:retweets'), lang='en',geo='22.0354768,76.5775322,5.25z,2500km').items(5): #item is number of item to be fetched
        try:
            print('\nTweet by: @' + tweet.user.screen_name + tweet.text + '\n')
            logger.info('\nTweet by: @' + tweet.user.screen_name + tweet.text + '\n')
            sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def two():                                  #change keyword written in hashtags Dont remove OR operator and you can also change geo variable and define kilometer radious at the end.
    for tweet in tweepy.Cursor(api.search, q=('#boys OR #girls OR #picture OR #photo -filter:retweets'),lang='en',geo='22.0354768,76.5775322,5.25z,2500km').items(5): #item is number of item to be fetched
            try:
                print('\nTweet by: @' + tweet.user.screen_name + tweet.text + '\n')
                logger.info('\nTweet by: @' + tweet.user.screen_name + tweet.text + '\n') 
                #sleep for 5 second
                sleep(5)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

if __name__ == '__main__':
    Process(target=one).start()
    Process(target=two).start()
    #process created for faster responce youcan create more on your own
