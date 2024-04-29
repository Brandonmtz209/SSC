import nltk
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
nltk.download('stopwords')
nltk.download('movie_reviews')
stop_words = list(set(stopwords.words('english')))
corpus_words = movie_reviews.words()
words_no_punct = [word for word in corpus_words if word.isalnum() and not word in stop_words]
freq = nltk.FreqDist(words_no_punct)
freq.plot(50, cumulative=False)
freq.plot(50, cumulative=True)
freq.plot(150, cumulative=False)
freq.plot(150, cumulative=True)
