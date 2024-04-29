import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
languages = stopwords.fileids()
print('Stopwords for ', len(languages), ' languages are included in NLTK')
print(languages)
