"""Retrieve Tweets, embeddings, and persist in the database."""
import basilica
import tweepy
from decouple import config
from models import DB, Tweet, User

TWITTER_AUTH = tweepy.OAuthHandler(config('kh1UW5a3NpMMq1cbXQ9SVhZLk'),
                                   config('1A5mxJDcn0MntyztyCdZDL3EhyxCVdjcOcYs2crOQJ1Xo1oJtW'))
TWITTER_AUTH.set_access_token(config('458923343-rII6VPPB4WuMvctPfrAXYA8TqRTiqzWQAJ161wQ1'),
                              config('rFbK5nHWm0IvFsh82hSzg6PX5Ojjq4iy2llfuvu5MkCAS'))
TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(config('fa04efb6-e097-2b42-55a6-eea04224396b'))

TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo']


def add_or_update_user(username):
  """ Add or update user and their tweets else error if not a Twitter User"""
  try:
    twitter_user = TWITTER.get_user(username)#from api
    ## Getting picture, follower count, etc. you get that info here.
    db_user = (User.query.get(twitter_user.id) or 
               User(id=twitter_user.id, name=username))#add or update
    #try to get the user from database first so hey does user exist already exist
    #so not overrides
    #if does not exist returns none and evaluates to the second line
    DB.session.add(db_user)#add to database
    #We want as many recent non-retweet/reply statuses as we can get
    # Limit is 250
    tweets = twitter_user.timeline(
      count=250, exclude_replies=True, include_rts=False,
      tweet_mode='extended', since_id=db_user.newest_tweet_id)#from api
    #we pull tweets since the id of the latest tweet
    if tweets:
        db_user.newest_tweet_id = tweets[0].id#fails if there are no tweets, so if there are tweets do this
    for tweet in tweets:
        # Get embedding for tweet, and store in db
        embedding = BASILICA.embed_sentence(tweet.full_text,
                                            mode='twitter')#tweet returned by twitter
        db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:500], embedding=embedding)#500 character limit
        db_user.tweets.append(db_tweet)#append tweet to user
        DB.session.add(db_tweet)#add tweet to database session
  except Exception as e:
      print("Error processing {}: {}".format(username, e))
      raise e#exception will keep going, whoever called this will also get the exeception
  #so will show on the website
  #raise means propagate, it casts exception but keeps going
  else:
      DB.session.commit()

def add_users(users=TWITTER_USERS):
    """
    Add/update a list of users (strings of user names).
    May take awhile, so run "offline" (flask shell).
    """
    for user in users:
        add_or_update_user(user)


      
