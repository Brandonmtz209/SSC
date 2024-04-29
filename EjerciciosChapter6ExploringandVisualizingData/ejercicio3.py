import nltk
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews
corpus_words = movie_reviews.words()
# remove punctuation
words_no_punct = []
for word in corpus_words:
    if word.isalnum():
        words_no_punct.append(word)
freq = nltk.FreqDist(words_no_punct)
# pip install matplotlib
freq.plot(50, cumulative=False)
freq.plot(50, cumulative=True)
freq.plot(150, cumulative=False)
freq.plot(150, cumulative=True)