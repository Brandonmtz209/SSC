import nltk
from nltk.util import ngrams
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# remove punctuation and stopwords
def clean_corpus(corpus):
    cleaned_corpus = []
    for word in corpus:
        if word.isalnum() and not word in stop_words:
            cleaned_corpus.append(word)
    return cleaned_corpus

# get the words from the movie reviews
corpus_words = movie_reviews.words()

# Define the stop words
stop_words = list(set(stopwords.words('english')))

# clean the corpus
cleaned_corpus = clean_corpus(corpus_words)

# collect the bigrams in the corpus
bigrams = ngrams(cleaned_corpus, 2)

# make a list from the bigrams
list_bigrams = list(bigrams)

# put together the bigrams into a single string
consolidated_bigrams = []
for bigram in list_bigrams:
    consolidated_bigram = bigram[0] + " " + bigram[1]
    consolidated_bigrams.append(consolidated_bigram)

# make a frequency distribution from the bigrams
freq_bigrams = nltk.FreqDist(consolidated_bigrams).most_common(25)

# Convert to a Pandas series
all_fdist = pd.Series(dict(freq_bigrams))

# set figure and axis variables and set sizes for the x and y axes
fig, ax = plt.subplots(figsize=(50,40))

# create a bar graph using Seaborn
sns.set(font_scale=2)

# display the bigrams on the y-axis and the counts on the x-axis
all_plot = sns.barplot(x=all_fdist.values, y=all_fdist.index, ax=ax, palette='hsv')

plt.show()
