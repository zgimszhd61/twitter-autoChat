import tweepy

## https://developer.twitter.com/en/portal/products

dict_twitter_api = {
    "consumer_key": '' ,
    "consumer_secret": '',
    "access_token": "", 
    "access_token_secret": ""
}
client = tweepy.Client(**dict_twitter_api)

print(client.get_me().data.username)  # <-- this works well
client.create_tweet(text="hello") # <-- this works too
