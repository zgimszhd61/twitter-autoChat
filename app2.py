import tweepy

# 填写你的Twitter API密钥
dict_twitter_api = {
    "consumer_key": '' ,
    "consumer_secret": '',
    "access_token": "", 
    "access_token_secret": ""
}

# 使用API密钥创建客户端
client = tweepy.Client(**dict_twitter_api)

# 检查客户端是否正确连接
print(client.get_me().data.username)

# 上传图片并获取media_id
def upload_media(api, media_file_path):
    media = api.media_upload(media_file_path)
    return media.media_id

# 发送带有图片的文字推文
def tweet_with_image(api, text, media_file_path):
    media_id = upload_media(api, media_file_path)
    client.create_tweet(text=text, media_ids=[media_id])

# 创建tweepy API对象
auth = tweepy.OAuth1UserHandler(
    dict_twitter_api["consumer_key"], dict_twitter_api["consumer_secret"],
    dict_twitter_api["access_token"], dict_twitter_api["access_token_secret"]
)
api = tweepy.API(auth)

# 示例：发送带有图片的文字推文
tweet_text = "Hello with an image!"
media_file_path = "path_to_your_image.jpg"  # 替换为你的图片文件路径
tweet_with_image(api, tweet_text, media_file_path)
