import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = list(set(stopwords.words('english')))
print(len(stop_words))
print(stop_words[0:50])
