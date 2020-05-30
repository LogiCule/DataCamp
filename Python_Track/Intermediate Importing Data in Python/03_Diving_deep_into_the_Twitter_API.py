#API Authentication

import tweepy 
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Streaming tweets

l = MyStreamListener()
stream = tweepy.Stream(auth, l)
stream.filter(['clinton','trump','sanders','cruz'])

#Load and explore your Twitter data

import json
tweets_data_path = 'tweets.txt'
tweets_data= []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0].keys())

#Twitter data to DataFrame

import pandas as pd
df = pd.DataFrame(tweets_data, columns=["text",'lang'])
print(df.head())

#A little bit of Twitter text analysis

[clinton, trump, sanders, cruz] = [0, 0, 0, 0]
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

#Plotting your Twitter data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
cd = ['clinton', 'trump', 'sanders', 'cruz']
ax = sns.barplot(cd,[clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()

