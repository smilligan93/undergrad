from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
from textblob import TextBlob
import wikipedia
import ujson

class FrequencySummarizer:
  def __init__(self, min_cut=0.1, max_cut=0.9):
    """
     Initilize the text summarizer.
     Words that have a frequency term lower than min_cut
     or higer than max_cut will be ignored.
    """
    self._min_cut = min_cut
    self._max_cut = max_cut
    self._stopwords = set(stopwords.words('english') + list(punctuation))

  def _compute_frequencies(self, word_sent):
    """
      Compute the frequency of each of word.
      Input:
       word_sent, a list of sentences already tokenized.
      Output:
       freq, a dictionary where freq[w] is the frequency of w.
    """
    freq = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in self._stopwords:
          freq[word] += 1
    # frequencies normalization and fitering
    m = float(max(freq.values()))
    for w in freq.keys():
      freq[w] = freq[w]/m
      if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
        del freq[w]
    return freq

  def summarize(self, text, n):
    """
      Return a list of n sentences
      which represent the summary of text.
    """
    sents = sent_tokenize(text)
    assert n <= len(sents)
    word_sent = [word_tokenize(s.lower()) for s in sents]
    self._freq = self._compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in self._freq:
          ranking[i] += self._freq[w]
    sents_idx = self._rank(ranking, n)
    return [sents[j] for j in sents_idx]

  def _rank(self, ranking, n):
    """ return the first n sentences with highest ranking """
    return nlargest(n, ranking, key=ranking.get)

#Function that accepts the text block and creates n summaries from that text. Returns a list of summaries
def freqsum(text,n):
    fs = FrequencySummarizer()
    summary = []
    for s in fs.summarize(text,n):
        summary.append(s)

#Function that analyzes the polarity of sentiment of the given text. It returns a tuple where the first element is the percentage of positivity of the text and the second element is the percentage of negativity
def sentiment(text):
    blob = TextBlob(text)
    polar = float(blob.sentiment.polarity + 1)/2
    pos = polar*100
    neg = 100 - pos
    #print pos, neg
    return (pos,neg)

#Returns a summary from wikipedia. Takes in query term and the language as input
def wikisummary(query, lang):
    wikipedia.set_lang(lang)
    #print wikipedia.summary(query,5)
    return wikipedia.summary(query,5)
