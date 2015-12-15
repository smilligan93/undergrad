import tag
import json
import os

ct = tag.ContentTagger()
#result = ct._tag_text("Most rugged luchadores from Mexico City agree that Donald Trump hates both the European Union and Mexico.")
#print(result)

#result = ct._tag_text("RT @J_Bloodworth: Wrong from the very first line &gt;&gt; Hilary Benn's Speech for Bombing Syria Was Disingenuous Bullshit https://t.co/cErkXsNDO\u2026")
#print(result)

#result = ct._tag_text("RT @RebeccaFMusic: Praying for the innocent children in Syria \ud83d\ude4f please god keep them poor babies safe \ud83d\udc94\ud83d\udc94\ud83d\udc94")
#print(result)

#with open(os.path.join(os.path.expanduser('~'),"python/new_tweets.json")) as file:
    #tweets = json.load(file)
#result = ct._tag_multi_tweets(tweets)

with open(os.path.join(os.path.expanduser('~'),"Nate/new_tweets_sample.json")) as file:
    tweets = json.load(file)
print(ct._return_tweets_with_tag(tweets, u'Syria'))

