import nltk
import random
import pandas as pd
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords

# remove punctuation and stopwords
def clean_corpus(corpus):
    cleaned_corpus = []
    for word in corpus:
        if word.isalnum() and not word in stopwords.words('english'):
            cleaned_corpus.append(word)
    return cleaned_corpus

# get the words from the movie reviews
corpus_words = movie_reviews.words()

# clean the corpus
cleaned_corpus = clean_corpus(corpus_words)

all_words = nltk.FreqDist(w for w in cleaned_corpus)
max_words = 1000
word_features = list(all_words)[:max_words]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in document_words)
    return features

# make a list of documents
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# collect features, that is, words that occur in a document
featuresets = [(document_features(document), category) for (document,category) in documents]

#remove categories for display
docnumber = 0
new_featuresets = {}
for featureset in featuresets:
    new_featureset = featureset[0]
    new_featuresets[docnumber] = new_featureset;
    docnumber += 1

# display the words that occur in the first 10 documents, the bag of words
df_featuresets = pd.DataFrame.from_dict(data = new_featuresets, orient = 'index', columns = word_features)
df_featuresets.head(10)
print(df_featuresets.head(10))