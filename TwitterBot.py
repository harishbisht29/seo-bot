import tweepy
from Bot import Bot
import my_credentials as credentials

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
        
    def get_articles(self):
        for tweet in tweepy.Cursor(
            self.api.search,
            q="(virtualenv OR venv python activate)",
            rpp=100,
            since_id=1
            ).items():
            # print(type(tweet))
            print(tweet.id)
            print(tweet.text)
            print(tweet.user.name)

            

    def post_on_account(self, post):
        print("Twitter Bot Posting on account")
        self.api.update_status(post)
    

        

if __name__ == '__main__':
    print("Inside Twitter Bot Main ")
    tb= TwitterBot()
    tb.get_articles()
    tb.api.update_status(status = 'test reply ', in_reply_to_status_id = 1265546985077170178, auto_populate_reply_metadata=True)

    
