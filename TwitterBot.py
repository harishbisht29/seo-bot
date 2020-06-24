from BotStorage import BotStorage
import tweepy
from Bot import Bot
import my_credentials as credentials
import requests
import json

class TwitterBot(Bot):

    def __init__(self, ckey=credentials.TWITTER_API_KEY,\
         csecret=credentials.TWITTER_API_SECRET,\
             at=credentials.TWITTER_AUTH_TOKEN,\
                 ats=credentials.TWITTER_AUTH_TOKEN_SECRET):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(at, ats)
        
        # Create API object
        self.api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
        
    def get_articles(self, search_parameter, since_id=1):
        matched_tweets= []
        for tweet in tweepy.Cursor(
            self.api.search,
            q=search_parameter,
            lang = 'en',
            rpp=100,
            since_id= since_id
            ).items():
            # print(type(tweet))
            # print(tweet.id)
            # print(tweet.text)
            # print(tweet.user.screen_name, tweet.created_at, tweet.id, tweet.text)
            matched_tweets.append({'user_name':tweet.user.screen_name,
            'tweet_id':tweet.id,
            'text':tweet.text,
            'created_at':tweet.created_at})
            # print()
        return matched_tweets

    def post_on_account(self, post):
        print("Twitter Bot Posting on account")
        self.api.update_status(post)
    
    def reply_to_tweet(self, id, reply):
        self.api.update_status(
            status = 'reply ',
            in_reply_to_status_id = id,
            auto_populate_reply_metadata=True)


if __name__ == '__main__':
    print("Inside Twitter Bot Main ")
    res= requests.get("https://www.codethemall.com/api/keyword-list?format=json")
    search_keywords = json.loads(res.text)

    res= requests.get("https://www.codethemall.com/api/post-list?format=json")
    posts= json.loads(res.text)


    config= {}
    config['filename']= 'data.json'
    storage= BotStorage(config)
    tBot= TwitterBot()

    for k in search_keywords:
        post_id= k['post']
        post_details=[ p  for p in posts if p['id']== post_id ][0]

        print(post_details)

        if not storage.postExists(post_id):
            print("Creating post unit", post_id)
            storage.createUnit(post_id)

        since_id= storage.getSinceId(post_id)
        matched_tweets= tBot.get_articles(k['keyword'], since_id)
        matched_tweets.reverse()

        for tweet in matched_tweets:
            print("Bot looking into ",tweet)
            replied_users= storage.getRepliedUsers(post_id)
            u= tweet['user_name']
            if u in replied_users:
                print("Already shared with user")
            else:
                print("replying user")
                print(post_details['title'],"->",k['url'] )
                storage.setRepliedUser(post_id,[u])
            storage.setSinceId(post_id, tweet['tweet_id'])
        

        # print(post_id, replied_users, since_id)    
            