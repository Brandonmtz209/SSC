import nltk
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Create a bar plot with a color gradient
plt.figure(figsize=(10, 6))
sns.barplot(x='Word', y='Frequency', data=df, palette='hsv') # viridis
plt.title('25 Most Common Words (excluding stopwords)')
plt.xticks(rotation=45)
plt.show()
