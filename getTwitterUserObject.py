import time
import tweepy
import csv,json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
CONSUMER_KEY = 'NPaf7LeqzfL2uh4DtyX5pRDiA'
CONSUMER_SECRET = 'Jcli0JRMyNgAhybouRhiqGSKPUye5S3fnAm22dwBvBr2llXbal'
ACCESS_KEY = '2883078087-vTzc3o6RzC4oK8B2kCWaPERALTZgUjcXcQcvPWd'
ACCESS_SECRET = 'uC04FX1weZCOzFlSmzHApNqDLy2mxbT6wucQb8KPGHD1F'
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
class TweetListener(StreamListener):
    # A listener handles tweets are the received from the stream.
    #This is a basic listener that just prints received tweets to standard output

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print (status)
#search
api = tweepy.API(auth)
twitterStream = Stream(auth,TweetListener())
with open('human.csv', 'w') as csvfile:
    fieldnames = ['id', 'Id_str','Screen_name','Location','Description','Url','Followers_count','Friends_count','Listed_count','Created_at','Favourites_count','Verified','Statuses_count','Lang','Status','Default_profile','Default_profile_image','Has_extended_profile','name','Bot']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    followers = []
    users = []


    for follower in tweepy.Cursor(api.followers, screen_name="CookieJu").items():
        followers.append(follower.screen_name)
        print(follower.screen_name)
        info = api.lookup_users(screen_names=[follower.screen_name])
        #users.append(info)
        print(follower.id)
        for user in info:
            print(user.screen_name)
            try:
                status = api.get_status(id = user.id)
            except:
                status = 'null'
            writer.writerow({'id': user.id, 'Id_str': user.id_str,
                             'Screen_name': user.screen_name,'Location': user.location,
                             'Description': user.description,'Url': user.url,'Followers_count': user.followers_count,
                             'Friends_count': user.friends_count,'Listed_count': user.listed_count,
                             'Created_at': user.created_at,'Favourites_count': user.favourites_count,
                             'Verified': user.verified,'Statuses_count': user.statuses_count,
                             'Lang': user.lang,'Status': status,'Default_profile': user.default_profile,
                             'Default_profile_image': user.default_profile_image,'Has_extended_profile': 'false',
                             'name': user.name,'Bot': '1'})

        if len(followers) > 150:
            break







