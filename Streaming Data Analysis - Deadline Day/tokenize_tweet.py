# -*- coding: utf-8 -*-

import re
import operator
import json
from collections import Counter
from nltk.corpus import stopwords
from nltk import bigrams
import string
from collections import defaultdict
import sys


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    # URLs
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')',
                       re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$',
                         re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(
            token) else token.lower() for token in tokens]
    return tokens


punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', '3', '25', '5', '6', '7', '8', '9', ':/', 'Don\'t', '10', '4', '1', '2', 'us', 'It\'s', 'via', 'ा', '', 'RT',
                                                   '…', 'I', '’', 'The', 'what', 'What', 'You', 'Your', 'A', 'new', 'https', 'Hi', 'We', 'My', 'Now', 'please', 'get', 'amp', 'like', '#SmallBizSaturday', '#smallbizsaturday', 'How', 'first']

com = defaultdict(lambda: defaultdict(int))
fname = 'data/stream__DeadlineDay.json'
with open(fname, 'r') as f:
    # search_word = sys.argv[1] # pass a term as a command-line argument
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        # terms_hash
        # terms_hash= [term for term in preprocess(tweet['text'])
        #       if term.startswith('#')]
        # terms_mentions = [term for term in preprocess(tweet['text'])
        #                   if term.startswith('@')]
        terms_only = [term for term in preprocess(
            tweet['text']) if term not in stop and not term.startswith(('@', '#'))]
        # terms_bigram = bigrams(terms_only)
        # if search_word in terms_only:
        #    count_all.update(terms_only)
        # Build co-occurrence matrix
#         """for i in range(len(terms_only)-1):
#             for j in range(i+1, len(terms_only)):
#                 w1, w2 = sorted([terms_only[i], terms_only[j]])
#                 if w1 != w2:
#                     com[w1][w2] += 1
# com_max = []
# # For each term, look for the most common co-occurrent terms
# for t1 in com:
#     t1_max_terms = max(com[t1].items(), key=operator.itemgetter(1))[:5]
#     for t2 in t1_max_terms:
#         com_max.append(((t1, t2), com[t1][t2]))
# # Get the most frequent co-occurrences
# terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
# print(terms_max[:5])"""
        # Update the counter
        count_all.update(terms_only)
        # Print the first 5 most frequent words
    print(count_all.most_common(15))
