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
#common words
print("Common Words:", freq.most_common(50))