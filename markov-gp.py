#!/usr/bin/env python
from pymarkovchain import MarkovChain
import csv 
import codecs
import re
import sys

lang = "en"
reviews_file = sys.argv[1]
reviews = []

reviews_header = ['Package Name', 'App Version', 'Reviewer Language', 'Reviewer Hardware Model', 'Review Submit Date and Time', 'Review Submit Millis Since Epoch', 'Review Last Update Date and Time', 'Review Last Update Millis Since Epoch', 'Star Rating', 'Review Title', 'Review Text', 'Developer Reply Date and Time', 'Developer Reply Millis Since Epoch', 'Developer Reply Text']
review_lang_index = reviews_header.index('Reviewer Language')
review_title_index = reviews_header.index('Review Title')
review_text_index = reviews_header.index('Review Text')

reviews_file_utf8 = reviews_file + ".utf8"
with codecs.open(reviews_file, 'rU', 'UTF-16') as infile:
    with open(reviews_file_utf8, 'wb') as outfile:
        for line in infile:
            outfile.write(line.encode('utf8'))

alphanum_pattern = re.compile('[\W_]+', re.UNICODE)
with open(reviews_file_utf8, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar=None)
    header = reader.next()

    for row in reader:
        lang = row[review_lang_index]
        if lang == 'en':
            title = re.sub(alphanum_pattern, ' ', row[review_title_index].strip().lower())
            text = re.sub(alphanum_pattern, ' ', row[review_text_index].strip().lower())
            if len(title) > 0: reviews.append(title)
            if len(text) > 0: reviews.append(text)

mc = MarkovChain(".markov")
mc.generateDatabase("\n".join(reviews))

print mc.generateString()
