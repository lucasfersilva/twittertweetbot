import tweepy
import time
import os

auth = tweepy.OAuthHandler('RNH1uViOzzIWgqZi7GdCIiP5L', 'CeA3W1XeE7goOG3gZADXG8fvDGcP9U9awE9tcXEIdMAp69thZW')
auth.set_access_token('911141129378193409-kB1VgLqGpArrkaf8v9EpGxy80yb8L0S', '0HUnqAdfZemrdLFjfTAr2y9EVK7lqkZTgB9L5JUUtTUwS')

api = tweepy.API(auth)

class Twitter_posting_deleting():
    
    def public_tweets(self):
        
        public_tweets2 = api.home_timeline()
        #path to your img
        media = api.media_upload("img/work.jpg")
        #your message here
        tweet = '''Use #Binance #Futures Code1 : “cashback10 '''
        
        for status in api.user_timeline(count=1):
            
            status_list = status.id
            print(str(status_list))
            api.destroy_status(status_list)
        
        time.sleep(30)
        api.update_status(status=tweet, media_ids=[media.media_id])


        
        

a = Twitter_posting_deleting()
        
    
while True:
    a.public_tweets()
    #modify the number inside the  () in seconds 
    time.sleep(1800)
