import nltk
# pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#nltk.download('stopwords')
#nltk.download('movie_reviews')

stop_words = list(set(stopwords.words('english')))
corpus_words = movie_reviews.words()

# Remove punctuation and stopwords
words_no_punct = [word for word in corpus_words if word.isalnum() and word not in stop_words]

frequency_cutoff = 200
all_fdist = nltk.FreqDist(words_no_punct).most_common(frequency_cutoff)
all_fdist = pd.Series(dict(all_fdist))

long_words = dict((m, n) for m, n in all_fdist.items() if len(m) > 2)
wordcloud = WordCloud(colormap="tab10", background_color="white").generate_from_frequencies(long_words)

plt.figure(figsize=(20,15))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
