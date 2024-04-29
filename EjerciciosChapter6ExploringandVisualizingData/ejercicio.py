# pip install nltk
import nltk
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews
corpus_words = movie_reviews.words()
print(len(corpus_words))
print(corpus_words)