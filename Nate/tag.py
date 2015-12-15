import nltk
import json
from nltk.tokenize import TweetTokenizer

#Traverse tagged word tree and identify named entities
def traverse(chunked):
    entityList = []
    for n in range(len(chunked)):
        x = chunked[n]
        l = ""
        if isinstance(x, nltk.tree.Tree):
            #I have no idea why this works
            if x.label() == 'NNP':
                print('0')
            else:
                for f in x.leaves():
                    l += f[0]
                    l += " "
                l = l[:-1]
                entityList.append(l)
    return entityList


class ContentTagger:
    #Breaks down input sentence and returns a list of all named entities
    def _tag_text(self, tweet_text):
        tokenizer = TweetTokenizer()
        tokens = tokenizer.tokenize(tweet_text)
        tagged = nltk.pos_tag(tokens)
        entities = nltk.chunk.ne_chunk(tagged)
        neList = traverse(entities)
        return neList
    
    #Takes tweet as json, identifies language, and calls _tag_text
    #Todo: add support for multi-lingual tagging
    def _tag_tweet(self, tweet_json):
        if tweet_json['lang'] == "fr":
            s = tweet_json['text_fr']
        elif tweet_json['lang'] == "de":
            s = tweet_json['text_de']
        elif tweet_json['lang'] == "ar":
            s = tweet_json['text_ar']
        elif tweet_json['lang'] == "ru":
            s = tweet_json['text_ru']
        else:
            s = tweet_json['text_en']
            
        return self._tag_text(s)
    
    #Iterates through a json containing multiple tweets and tags each one 
    #Returns a list of the list of returned _tag_text values
    def _tag_multi_tweets(self, tweet_json):
        l = []
        for n in tweet_json:
            entityList = self._tag_tweet(n)
            l.append(entityList)
        return l
        
    #Iterates through a json containing multiple tweets and tags each one, then checks for the given tag
    #Returns a list of tweets, represented by ids, that contain the given tag
    #Painfully slow
    def _return_tweets_with_tag(self, tweet_json, tag):
        l = []
        for n in tweet_json:
            entityList = self._tag_tweet(n)
            if tag in entityList:
                l.append(n['id'])
        return l
        
    
        
    

    