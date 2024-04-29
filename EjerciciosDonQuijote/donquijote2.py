from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import PyPDF2
import re

# Función para extraer texto de un archivo PDF y quitar signos de puntuación
def extract_text_from_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    
    # Remover signos de puntuación
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

# Nombre del archivo PDF
pdf_file = "donquijote.pdf"

# Extraer texto del PDF
text = extract_text_from_pdf(pdf_file)

# Tokenizar el texto en palabras
words = word_tokenize(text)

# Eliminar palabras vacías (stop words)
stop_words = set(stopwords.words("spanish"))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Convertir la lista de palabras filtradas en una cadena de texto
filtered_text = " ".join(filtered_words)

# Calcular TF-IDF usando sklearn
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([filtered_text])

# Obtener los nombres de las características (palabras)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Obtener los valores de TF-IDF para cada palabra
tfidf_values = tfidf_matrix.toarray()[0]

# Crear un diccionario que mapee cada palabra a su valor de TF-IDF
tfidf_dict = dict(zip(feature_names, tfidf_values))

# Filtrar palabras que consisten completamente de caracteres alfabéticos
tfidf_dict = {word: tfidf for word, tfidf in tfidf_dict.items() if word.isalpha()}

# Mostrar las 10 palabras con los mayores valores de TF-IDF
top_tfidf_words = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print("Palabras con los mayores valores de TF-IDF:")
for word, tfidf in top_tfidf_words:
    print(f"{word}: {tfidf}")

# Mostrar las 10 palabras con los valores de TF-IDF más bajos
bottom_tfidf_words = sorted(tfidf_dict.items(), key=lambda x: x[1])[:10]
print("\nPalabras con los valores de TF-IDF más bajos:")
for word, tfidf in bottom_tfidf_words:
    print(f"{word}: {tfidf}")
