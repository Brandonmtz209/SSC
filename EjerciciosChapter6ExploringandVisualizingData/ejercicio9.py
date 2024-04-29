import nltk
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# remove punctuation and stopwords
def clean_corpus(corpus):
    cleaned_corpus = []
    for word in corpus:
        if word.isalnum() and not word in stop_words:
            cleaned_corpus.append(word)
    return(cleaned_corpus)

# show a word cloud given a frequency distribution
def plot_freq_dist(freq_dist):
    frequency_cutoff = 50
    long_words = dict([(m, n) for m, n in freq_dist.items() if len(m) > 2])
    wordcloud = WordCloud(colormap="tab10", background_color="white").generate_from_frequencies(long_words)
    
    plt.figure(figsize=(20,15))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
stop_words = list(set(stopwords.words('english')))
corpus_neg_words = movie_reviews.words(categories="neg")
corpus_pos_words = movie_reviews.words(categories="pos")
negative_words = clean_corpus(corpus_neg_words)
positive_words = clean_corpus(corpus_pos_words)
neg_freq = nltk.FreqDist(negative_words)
pos_freq = nltk.FreqDist(positive_words)
plot_freq_dist(pos_freq)
plot_freq_dist(neg_freq)
