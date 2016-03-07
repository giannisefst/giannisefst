import tweepy

#Credentials to access the Twitter API 
access_token = "4872755189-CTmYHqH5HvmWXGawbkka2hUErfIj31atpKhA4CY"
access_token_secret = "Xns21qYvz8lFFVeJhzuSUTumenCtfjgOYZ2RtDdINRvYA"
consumer_key = "uc28rLu4lLoXsXqhzfoR2nZUI"
consumer_secret = "LzC3vUsx6vP49jhSTXaEJuXQBMw33kfeTQnUI1PahaqOVBDRjc"

user1_name = input('Enter the 1st Twitter username: ')
user2_name = input('Enter the 2nd Twitter username: ')

skor1 = 0
skor2 = 0

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user1 = api.get_user(user1_name)
user2 = api.get_user(user2_name)

print ('Προφίλ @',user1.screen_name,'  TWEETS ', user1.statuses_count, ',  FOLLOWING ', user1.friends_count,',  FOLLOWERS ', user1.followers_count,',  LIKES ', user1.favourites_count )
print ('Προφίλ @',user2.screen_name,'  TWEETS ', user2.statuses_count, ',  FOLLOWING ', user2.friends_count,',  FOLLOWERS ', user2.followers_count,',  LIKES ', user2.favourites_count )

if user1.statuses_count > user2.statuses_count:
    skor1 = skor1 + 1
elif user1.statuses_count < user2.statuses_count:
    skor2 = skor2 + 1

if user1.friends_count > user2.friends_count:
    skor1 = skor1 + 1
elif user1.friends_count < user2.friends_count:
    skor2 = skor2 + 1

if user1.followers_count > user2.followers_count:
    skor1 = skor1 + 1
elif user1.followers_count < user2.followers_count:
    skor2 = skor2 + 1

if user1.favourites_count > user2.favourites_count:
    skor1 = skor1 + 1
elif user1.favourites_count < user2.favourites_count:
    skor2 = skor2 + 1

print ('Σκορ ', skor1,'-',skor2 )

    
