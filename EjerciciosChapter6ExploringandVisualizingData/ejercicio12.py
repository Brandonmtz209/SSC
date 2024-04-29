import nltk
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD

nltk.download('stopwords')
nltk.download('movie_reviews')

stop_words = list(set(stopwords.words('english')))
corpus_words = movie_reviews.words()

# Remove punctuation and stopwords
words_no_punct = [word for word in corpus_words if word.isalnum() and word not in stop_words]

frequency_cutoff = 25
all_fdist = nltk.FreqDist(words_no_punct).most_common(frequency_cutoff)

# Convert the frequency distribution to a Pandas DataFrame
df = pd.DataFrame(all_fdist, columns=['Word', 'Frequency'])

# Prepare the features for clustering
df_featuresets = df['Frequency'].values.reshape(-1, 1)

true_k = 2
kmeans = KMeans(n_clusters = true_k,
                init='k-means++',
                max_iter=100,  # Maximum iterations
                n_init=10)     # Number of times to run the k-means algorithm

result = kmeans.fit(df_featuresets)
labels = result.labels_
cm = plt.get_cmap('Accent')

# plot clusters in different colors
for cluster in range(true_k):
    current_color = cm(1.*cluster/true_k)
    plt.scatter(df_featuresets[labels == cluster, 0], np.zeros_like(df_featuresets[labels == cluster]),
                color = current_color, label='cluster ' + str(cluster))

plt.rcParams["figure.figsize"] = (20,20)
plt.rcParams['font.size'] = '12'
plt.show()

